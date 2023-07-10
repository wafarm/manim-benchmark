#!/usr/bin/env bash

cd current
poetry build
pip install dist/*.whl --force-reinstall --no-deps