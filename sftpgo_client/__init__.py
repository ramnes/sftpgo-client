import functools
import importlib
import pkgutil
from datetime import datetime

import httpx

from sftpgo_client.base import api
from sftpgo_client.base.api.token.get_token import _build_response
from sftpgo_client.base.client import AuthenticatedClient


class Client(AuthenticatedClient):
    def __init__(self, base_url, user, password, *args, **kwargs):
        self.user = user
        self.password = password
        kwargs["token"] = ""
        super().__init__(base_url, *args, **kwargs)

    @property
    def token_expired(self):
        return self.token_expires_at >= datetime.utcnow()

    def _get_token__get_kwargs(self):
        return {
            "url": f"{self.base_url}/token",
            "headers": self.headers,
            "timeout": self.timeout,
            "auth": httpx.BasicAuth(username=self.user, password=self.password),
        }

    def _get_token__parse_response(self, response):
        response.raise_for_status()
        response = _build_response(response=response)
        return response.parsed

    def get_token(self):
        response = httpx.get(**self._get_token__get_kwargs())
        return self._get_token__parse_response(response)

    def _set_token(self, token):
        self.token = token.access_token
        self.token_expires_at = token.expires_at.replace(tzinfo=None)

    @classmethod
    def _make_proxy_method(cls, function):
        @functools.wraps(function)
        def proxy_method(self, *args, **kwargs):
            if not self.token or self.token_expired:
                token = self.get_token()
                self._set_token(token)

            kwargs["client"] = self
            return function(*args, **kwargs)

        return proxy_method

    @classmethod
    def _add_proxy_method(cls, method_name, function):
        proxy_method = cls._make_proxy_method(function)
        if not hasattr(cls, method_name):
            setattr(cls, method_name, proxy_method)


class AsyncClient(Client):
    async def get_token(self):
        async with httpx.AsyncClient() as _client:
            response = await _client.get(**self._get_token__get_kwargs())
        return self._get_token__parse_response(response)

    @classmethod
    def _make_proxy_method(cls, function):
        @functools.wraps(function)
        async def proxy_method(self, *args, **kwargs):
            if not self.token or self.token_expired:
                token = await self.get_token()
                self._set_token(token)

            kwargs["client"] = self
            return await function(*args, **kwargs)

        return proxy_method


for module_info in pkgutil.walk_packages(api.__path__):
    module_name = f"{api.__name__}.{module_info.name}"
    module = importlib.import_module(module_name)
    for submodule_info in pkgutil.walk_packages(module.__path__):
        submodule_name = f"{module_name}.{submodule_info.name}"
        submodule = importlib.import_module(submodule_name)
        if hasattr(submodule, "asyncio"):
            AsyncClient._add_proxy_method(submodule_info.name, submodule.asyncio)
        if hasattr(submodule, "sync"):
            Client._add_proxy_method(submodule_info.name, submodule.sync)
