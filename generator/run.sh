#!/bin/sh

virtualenv generator/venv -ppython3.9
(
    source generator/venv/bin/activate
    pip install -r generator/requirements.txt
    wget "https://raw.githubusercontent.com/drakkan/sftpgo/main/httpd/schema/openapi.yaml" -O generator/openapi.yaml
    openapi-python-client --config=generator/config.yaml update --path=generator/openapi.yaml
)
