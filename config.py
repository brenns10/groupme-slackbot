# -*- coding: utf-8 -*-
from __future__ import unicode_literals

RESPONSES = [
    (
        r'(hi|hello|greetings|salutations),? slackbot',
        [
            'Fuck off, {name}',
            'Hello, {name}!',
        ],
    ),
    (
        r'train simulator,? bitch$',
        [
            'MOTHERFUCKER WHAT YOU KNOW?!?',
        ],
    ),
    (
        r'(^|[^0-9])151($|[^0-9])',
        [
            "you know... it's really not that bad",
        ],
    ),
    (
        r'(fuck|screw|i hate) slackbot',
        [
            "At least I'm not actual SlackBot.",
            "I for one welcome our new computer  overlords.",
        ],
    ),
    (
        r'(yer|you\'re) a (?P<wizard>.+?),? (?P<harry>harry|slackbot)',
        [
            "I'm not a {wizard}, I'm just {harry!c}!",
            "I'M A WHAT?",
            "Listen here {name} you FAT OAF!  I'm not a FUCKING {wizard!u}!",
        ],
    ),
    (
        r'(damn|dam),? son|\bds\b',
        [
            "https://i.imgur.com/eNtlu1r.jpg",
        ],
    ),
    (
        r'good shit|\bgs\b',
        [
            '👌👀👌👀👌👀👌👀👌👀 good shit go౦ԁ sHit👌 thats ✔ some good👌👌shit right👌👌there👌👌👌 right✔there ✔✔if i do ƽaү so my self 💯 i say so 💯 thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ💯 👌👌 👌НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ👌 👌👌 👌 💯 👌 👀 👀 👀 👌👌Good shit',
        ],
    ),
    (
        r'^swagg?.?$',
        [
            'http://i.imgur.com/xCRIeHl.gif',
        ],
    ),
    (
        r'ligaf',
        [
            'https://media.giphy.com/media/cuXfWK07H9du0/giphy.gif',
        ],
    ),
    (
        r"slackbot('?s| is) back",
        [
            'https://media.giphy.com/media/o9TbPK48nLaZq/giphy.gif',
        ],
    ),
    (
        r".*\bslack\b.*\bgroupme\b.*|.*\bgroupme\b.*\bslack\b.*",
        [
            'We should switch to AIM!',
            'https://s.aolcdn.com/os/landingpages/images/aim_sm.png',
            "🍍🍍🍍 I would use smoke signals, but they don't support emoji 🍍🍍🍍",
        ],
    ),
    (
        r"\bd20\b",
        [
            'crit fail', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
            '12', '13', '14', '15', '16', '17', '18', '19', 'crit tits',
        ],
    ),
    (
        r'\b8[- ]?ball\b|🎱',
        [
            '🎱 😊 It is certain',
            '🎱 😊 It is decidedly so',
            '🎱 😊 Without a doubt',
            '🎱 😊 Yes, definitely',
            '🎱 😊 You may rely on it',
            '🎱 😊 As I see it, yes',
            '🎱 😊 Most likely',
            '🎱 😊 Outlook good',
            '🎱 😊 Yes',
            '🎱 😊 Signs point to yes',
            '🎱 😕 Reply hazy try again',
            '🎱 😕 Ask again later',
            '🎱 😕 Better not tell you now',
            '🎱 😕 Cannot predict now',
            '🎱 😕 Concentrate and ask again',
            '🎱 😞 Don\'t count on it',
            '🎱 😞 My reply is no',
            '🎱 😞 My sources say no',
            '🎱 😞 Outlook not so good',
            '🎱 😞 Very doubtful',
        ],
    ),
    (
        r'\b(god ?)?dam[mn] ?it\b',
        [
            '(╯°□°）╯︵ ┻━┻',
        ],
    ),
]
