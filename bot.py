# -*- coding: utf-8 -*-
"""
A GroupMe bot that does auto-responses like Slackbot. Runs on AWS Lambda.
"""
from __future__ import print_function

import base64
import re
import random
import json
import string

import requests
import boto3

from config import RESPONSES

API_URL = 'https://api.groupme.com/v3/bots/post'

# Kind of annoying to create. First, on AWS console, create key.
# Install aws cli, run 'aws configure' (if you haven't already)
# $ aws kms encrypt --plaintext ID_HERE --key-id alias/KEY_ALIAS_HERE
# The base64-encoded CiphertextBlob is what you want.
ENCRYPTED_BOT_ID = 'AQECAHhntcgbgv4UZX6JXua2kg8IhT6cbre0WCSiz7xcx7nC8AAAAHgwdgYJKoZIhvcNAQcGoGkwZwIBADBiBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDAZkSTizbKK+SI8otgIBEIA1B4n/BZN2FK8VcAQtpL6jmNbTJ+Wamv25+GxpqCeDfyhhL7tfemPWP7Gi8BDrNczREoEksYs='


class CustomFormatter(string.Formatter):
    """
    This formatter will convert fields to string and apply an upper/lower case
    operation on them, so that the field looks precisely the way you want it.
    """

    def convert_field(self, value, conversion):
        try:
            return super(CustomFormatter, self).convert_field(value, conversion)
        except ValueError as e:
            if conversion == 'u':
                return str(value).upper()
            elif conversion == 'l':
                return str(value).lower()
            elif conversion == 'w':
                return str(value).swapcase()
            elif conversion == 'c':
                return str(value).capitalize()
            else:
                raise e


def post(msg):
    """Post to GroupMe. Super easy. Except for the encrypted bot ID."""
    blob = base64.b64decode(ENCRYPTED_BOT_ID)
    client = boto3.client('kms')
    bot_id = client.decrypt(CiphertextBlob=blob)['Plaintext']
    body = {
        'bot_id': bot_id,
        'text': msg,
    }
    return requests.post(API_URL, json=body)


def handle(event, context):
    # Data is a JSON object which was stashed into another JSON object...
    data = json.loads(event['body'])

    if 'system' in data and data['system']:
        print('Got system message, will not respond.')
        return

    if 'sender_type' in data and data['sender_type'] == 'bot':
        print('Got bot message, will not respond.')
        return

    context = {
        'name': data['name']
    }

    for expr, responses in RESPONSES:
        if re.search(expr, data['text'], re.I) is not None:
            match = re.search(expr, data['text'], re.I)
            context.update(match.groupdict())
            response = CustomFormatter().format(random.choice(responses),
                                                **context)
            post(response)
            print(response)

    print('No response.')
