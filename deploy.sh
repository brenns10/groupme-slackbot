#!/bin/bash

# Usage: ./deploy.sh FunctionName

# Create actual bot
cat $1.py bot.py > botgen.py

# Create zip package.
rm package.zip
zip package.zip botgen.py config.py
mkdir libs
pip2 install -t libs requests
pushd libs
zip -r ../package.zip *
popd
rm -rf libs

# Set your lambda function's code.
aws lambda update-function-code \
    --function-name $1 \
    --zip-file fileb://package.zip

# cleanup
rm botgen.py
