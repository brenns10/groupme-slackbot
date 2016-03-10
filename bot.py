"""
Python GroupMe Bot.

Run on port 30151.
"""

import re
import random
import json

from groupy import Bot
from flask import Flask, request

app = Flask(__name__)
log = app.logger


class SlackBot(object):
    """A simple slackbot clone."""

    def __init__(self, post):
        self.post = post
        self.responses = []
        self.context = {}

    def register(self, regex, responses):
        self.responses.append((re.compile(regex, re.I), responses))

    def callback(self):
        print(request.data)
        data = json.loads(request.data.decode('utf8'))

        if 'system' in data and data['system']:
            log.info('Got system message, will not respond.')
            return 'No response (system message)'

        context = self.context.copy()
        context['name'] = data['name']
        log.debug(data['text'])

        for expr, responses in self.responses:
            if expr.search(data['text']) is not None:
                response = random.choice(responses).format(**context)
                log.info('Matched pattern %r, returning "%s".' %
                         (expr, response))
                self.post(response)
                return response

        return 'No response.'


if __name__ == '__main__':
    bot = Bot.list()[1]  # TESTING
    slackbot = SlackBot(bot.post)

    slackbot.register(r'hi slackbot', ['fuck off, {name}', 'hello, {name}!'])

    # TESTING
    app.route('/callback_test', methods=['POST'])(slackbot.callback)
    app.run('0.0.0.0', port=30151)
