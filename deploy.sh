#!/bin/bash
# Usage: ./deploy.sh

# Create zip package.
rm package.zip
zip package.zip bot.py config.py
mkdir libs
pip2 install -t libs requests
pushd libs
zip -r ../package.zip *
popd
rm -rf libs

# Set your lambda function's code.
aws lambda update-function-code \
    --function-name Slackbot \
    --zip-file fileb://package.zip
