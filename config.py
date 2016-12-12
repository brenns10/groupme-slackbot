# -*- coding: utf-8 -*-
"""Slackbot response configuration.

This module should contain a list named RESPONSES. Each entry should be either
a two or three tuple. The first element is a regular expression to be searched
for in a message. The second element is a list of responses to be chosen and
"formatted" before sending to the group. The last (optional) element is a
probability that the response will be used (assumed to be 1 if not present).

This module should also contain a dict named SPECIFIC_RESPONSES. This should
map a group ID (as a string) to a response list (similar to RESPONSES). These
responses will be included only when a message is from that group.

"""

from __future__ import unicode_literals

RESPONSES = [
    (
        r'(hi|hello|greetings|salutations|sup),? slackbot',
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
        r'(?P<verb>fuck|screw|i hate|shame on)( you,?)? slackbot',
        [
            'https://media.giphy.com/media/urvsFBDfR6N32/giphy.gif',
            'https://media.giphy.com/media/134CbbASMeRPDa/giphy.gif',
            'Well {verb!l} you too, {name}.\n\n{verb!c} you too.',
            'https://s-media-cache-ak0.pinimg.com/originals/a5/1e/9f/a51e9fc7bf72610357d84b25cc689527.jpg',
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
    (
        r'^(and )?i said,? bi+tch',
        [
            'http://25.media.tumblr.com/tumblr_ma07gxDjOw1r02fd4o1_500.gif',
        ],
    ),
    (
        r'^yeah,? sure,? ok(ay)?$',
        [
            'http://sugarscape.cdnds.net/16/03/1453384969-tumblr-m3xrtsmgs11rn435g.gif',
        ],
    ),
    (
        r'^[ .]*(wtf|the fuck|what the fuck|da phuc)\?*$',
        [
            'https://s-media-cache-ak0.pinimg.com/originals/7d/4e/02/7d4e02c83c3faf809d43c8df656223db.gif',
            'http://i.imgur.com/wnYTz7L.jpg?1',
            'https://media.giphy.com/media/nt82bdEUj9jKE/giphy.gif',
            'http://www.reactiongifs.us/wp-content/uploads/2016/06/whaaat_bernie_sanders.gif',
            'http://mrwgifs.com/wp-content/uploads/2013/05/WTF-Are-You-Doing-Puppy-Reaction-Gif.gif',
        ]
    ),
    (
        r"she doesn't even go here",
        [
            'https://66.media.tumblr.com/6dd8c1d37ee3e5e3828649453ea6e0b8/tumblr_mqhmm3F7FA1s8scfko1_500.gif',
        ],
    ),
    (
        r'shopping|get in,? loser',
        [
            'http://media0.giphy.com/media/4CP58gxwbBy2Q/giphy.gif',
        ],
    ),
    (
        r'chuffed as nuts',
        [
            'http://marketingforcarpetcleaners.org/wp-content/uploads/2016/09/chuffed-as-nuts-guarantee-150x150.jpg',
        ],
    ),
    (
        r'joe?partment',
        [
            'I think you mean Stepartment.',
            "We're calling it the Steplex now.",
            'Karl lives there too!',
            "Karlpartment? It just doesn't have the same ring to it.",
        ],
    ),
    (
        r'dank',
        [
            'http://cdn.yourepeat.com/media/gif/000/060/981/3e1bcb7030bd2a8a46af871bde336d52.gif',
        ],
    ),
    (
        r"^(fuck.?|i'?m fucked up|(.*you )?drunk (bitch|hoe|whore|motherfucker|slob))$",
        [
            'https://media.giphy.com/media/gPLXXmObaJCW4/giphy.gif'
        ],
    ),
    (
        r'gumbo joe',
        [
            'http://weldbham.com/wp-content/uploads/2015/11/unnamed-17.jpg',
            'http://myrecipemagic.com/uploads/recipes/72003/1423583772_gumbo-sloppy-joes.jpg',
        ],
    ),
    (
        r'(.*\bsloppy\b.*\bjoe\b.*|.*\bjoe\b.*\bsloppy\b.*)',
        [
            'https://cdn.meme.am/cache/instances/folder101/48979101.jpg',
            'http://myrecipemagic.com/uploads/recipes/72003/1423583772_gumbo-sloppy-joes.jpg',
        ],
    )
]


SPECIFIC_RESPONSES = {
    # SlackbotTest
    '20457310': [
        (
            '.*',
            [
                'Are you testing me?  Why don\'t you just trust me?',
            ],
            0.2,
        ),
    ],
}
