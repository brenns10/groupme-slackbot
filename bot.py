"""
Python GroupMe Bot.

Run on port 30151.
"""

import re
import random
import json
import sys

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

        if 'sender_type' in data and data['sender_type'] == 'bot':
            log.info('Got bot message, will not respond.')
            return 'No response (bot message)'

        context = self.context.copy()
        context['name'] = data['name']
        log.debug(data['text'])

        for expr, responses in self.responses:
            if expr.search(data['text']) is not None:
                match = expr.search(data['text'])
                context.update(match.groupdict())
                response = random.choice(responses).format(**context)
                log.info('Matched pattern %r, returning "%s".' %
                         (expr, response))
                self.post(response)
                return response

        return 'No response.'


if __name__ == '__main__':

    # This prompts the user for the bot they'd like to use.
    bots = Bot.list()
    if len(bots) == 1:
        bot = bots.first
    else:
        print(bots)
        bot = bots[int(input('Which bot index? '))]
    slackbot = SlackBot(bot.post)

    # In this section, we register regexes with responses.
    slackbot.register(r'(hi|hello|greetings|salutations),? slackbot',
                      ['Fuck off, {name}', 'Hello, {name}!'])
    slackbot.register(r'train simulator,? bitch$',
                      ['MOTHERFUCKER WHAT YOU KNOW?!?'])
    slackbot.register(r'(^|[^0-9])151($|[^0-9])',
                      ["you know... it's really not that bad"])
    slackbot.register(r'(fuck|screw|i hate) slackbot',
                      ["At least I'm not actual SlackBot."])
    slackbot.register(r'(yer|you\'re) a wizard,? harry',
                      ["I'M A WHAT?", "I'm just Harry",
                       "A wizard? I'm just Harry",
                       "Listen here Hagrid, you FAT OAF!  I'm not a FUCKING WIZARD"])
    slackbot.register(r'(yer|you\'re) a (?P<something>\w+),? harry',
                      ["I'm not a {something}, I'm just Harry"])

    # Here, we determine the callback.
    if len(sys.argv) <= 1:
        route = '/callback'
    else:
        route = sys.argv[1]

    # And, run the application.
    app.route(route, methods=['POST'])(slackbot.callback)
    app.run('0.0.0.0', port=30151)
