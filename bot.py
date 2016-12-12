from __future__ import print_function
from __future__ import unicode_literals

import base64
import re
import random
import json
import string

import requests
import boto3

from config import RESPONSES, SPECIFIC_RESPONSES

API_URL = 'https://api.groupme.com/v3/bots/post'

# Maps group IDs to bots within those groups, so we can serve multiple bots.
BOT_IDS = {
    # SlackbotCleveland
    '24993946': 'AQECAHhntcgbgv4UZX6JXua2kg8IhT6cbre0WCSiz7xcx7nC8AAAAHgwdgYJKoZIhvcNAQcGoGkwZwIBADBiBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDIWNMj7bSbS+2Elk7AIBEIA19kIxY963r1FKvLPCGkxBWO8eeoXcCO328F5ETVssZWpwA0yGpTS4+d33tvmKy5fBwbF/WjA=',
    # SlackbotCult
    '10081119': 'AQECAHhntcgbgv4UZX6JXua2kg8IhT6cbre0WCSiz7xcx7nC8AAAAHgwdgYJKoZIhvcNAQcGoGkwZwIBADBiBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDAZkSTizbKK+SI8otgIBEIA1B4n/BZN2FK8VcAQtpL6jmNbTJ+Wamv25+GxpqCeDfyhhL7tfemPWP7Gi8BDrNczREoEksYs=',
    # SlackbotTest
    '20457310': 'AQECAHhntcgbgv4UZX6JXua2kg8IhT6cbre0WCSiz7xcx7nC8AAAAHgwdgYJKoZIhvcNAQcGoGkwZwIBADBiBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDN+mwLRa+fibbLkFugIBEIA14FM7+iYQcGzZFElfnQgnEFxaYL3Oaz7U+mFu+OHP6ZQ8XgNd3H5sKIdmF8SDmPYFWOuQjSM=',
    # Fairy Godmother
    '27402712': 'AQECAHhntcgbgv4UZX6JXua2kg8IhT6cbre0WCSiz7xcx7nC8AAAAHgwdgYJKoZIhvcNAQcGoGkwZwIBADBiBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDBUWE3rGbzAa6JsuWQIBEIA1eJ4aSmjpF+9G+BzF7Ce2blpMm0VK/UI63lbPD6d4Ot3RRtTP6sqyDMgmlEkfLQFM54sPiSc=',
    # Apartment
    '10203366': 'AQECAHhntcgbgv4UZX6JXua2kg8IhT6cbre0WCSiz7xcx7nC8AAAAHgwdgYJKoZIhvcNAQcGoGkwZwIBADBiBgkqhkiG9w0BBwEwHgYJYIZIAWUDBAEuMBEEDFuCMccp1Cy7MEYPbgIBEIA11NjJven2fcOHmcwS5CTucEMcnIccj97qKKNOhkX5aeJurCWLaMDUVyU7t8EIrDt+iGRJ/To=',
}

# For tests. Not actually sent to.
DEFAULT_GROUP = '20457310'


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


def post(msg, bot_id):
    """Post to GroupMe. Super easy. Except for the encrypted bot ID."""
    body = {
        'bot_id': bot_id,
        'text': msg,
    }
    return requests.post(API_URL, json=body)


def get_bot_id(group):
    """Get the bot ID for a group."""
    blob = base64.b64decode(BOT_IDS[group])
    client = boto3.client('kms')
    bot_id = client.decrypt(CiphertextBlob=blob)['Plaintext']
    return bot_id.decode('ascii')


def reply(message, context, group):
    """Reply to a message that isn't a system/bot message."""
    bot_id = get_bot_id(group)
    all_responses = RESPONSES + SPECIFIC_RESPONSES.get(group, [])

    for tup in all_responses:
        # Unpack response tuple.
        expr = tup[0]
        responses = tup[1]
        probability = tup[2] if len(tup) > 2 else 1.0

        # Try to match the message.
        match = re.search(expr, message, re.I | re.U)

        # We reply if the pattern matched and the odds are with us.
        if match and random.random() <= probability:
            # Make a copy of the context to isolate any modifications.
            ctxcpy = context.copy()

            # Update the context with anything captured by the regex.
            if match:
                ctxcpy.update(match.groupdict())

            # Generate and post a response.
            response = CustomFormatter().format(random.choice(responses),
                                                **ctxcpy)
            post(response, bot_id)


def handle(event, context):
    """Main AWS Lambda entry point, handles a callback from GroupMe."""
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
    reply(data['text'], context, data['group_id'])


if __name__ == '__main__':
    import sys
    post = lambda x, y: print(x)
    reply(sys.argv[1], {'name': 'stdin'}, DEFAULT_GROUP)
