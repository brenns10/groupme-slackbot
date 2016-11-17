# -*- coding: utf-8 -*-

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
        r'(damn|dam),? son',
        [
            "https://i.imgur.com/eNtlu1r.jpg",
        ],
    ),
    (
        r'good shit',
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
]
