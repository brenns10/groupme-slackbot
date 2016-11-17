#!/bin/bash

# Usage: ./deploy.sh FunctionName

# Create zip package.
rm package.zip
zip package.zip bot.py config.py
pushd venv/lib/python2.7/site-packages
zip -r ../../../../package.zip *
popd

# Set your lambda function's code.
aws lambda update-function-code \
    --function-name $1 \
    --zip-file fileb://package.zip
