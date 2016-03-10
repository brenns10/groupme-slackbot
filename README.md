SlackBot for GroupMe
====================

GroupMe lacks many features of Slack, the least useful of which being the
SlackBot response.  Not surprisingly, the least useful feature is also the
easiest to implement.  I present to you - SlackBot responses for GroupMe!

What?
-----

GroupMe and Slack are both group messaging services.  Slackbot is a bot in Slack
that (among many other features) can automatically reply to messages that match
a pattern with a response chosen randomly from a list.  This project just
implements that part of SlackBot, but for GroupMe.

This particular repository contains both the code for this bot, as well as the
responses associated with an instance I currently run.  Chances are if you want
to use this, you'll need to fork it and change the responses.

Basics
------

GroupMe provides a neat API for creating bots, which can be used in Python
through [Groupy][groupy].  You create a "Bot" object associated with a group,
complete with a callback URL.  Whenever a message is posted in the group,
GroupMe will POST it to your URL.  Your bot can also send messages to the group.
So, this program just waits for callbacks from GroupMe.  When a message matches
a pattern, the bot selects a reply and sends it to the group.

Adding Responses
----------------

The responses are added near the bottom, using the function
`slackbot.register()`.  My implementation of SlackBot's responses is much more
feature rich than the one that Slack comes with (thanks to Python!).

The first argument of the `register()` function is a regular expression, which
means that this bot can match much more powerfully than Slackbot can.  Matching
is done case insensitively.  When testing expressions against messages, the bot
checks to see if the string contains a match at any index (not just index 0), so
`pace` would match the message `blank space` unless you used the `\b` notation
for "word boundary".

The second argument is a list of responses, which will be randomly selected
from.  The response will be formatted using the `string.format()` method, with
the following items defined:
- `name`: The name of the user sending the message.
- Any named capture from the regular expression (neat, right?)
- Anything else you might want to stash away in the `context` dictionary in the
  bot.

So, for a regex like `you're a (?P<something>\w+),? harry`, you could have a
response like `I'm not a {something}, I'm just Harry!`.  Then, when the message
`You're a wizard, Harry` comes in, the bot might reply, `I'm not a wizard, I'm
just Harry!`

Setup/Deploy
------------

I always hate code without instructions.  So here is how to get this running.
First, you'll need Python and Pip installed.  You'll want to install the
required packages with the command (`pip install -r requirements.txt`).  I'd
recommend using a VirtualEnv.

Next, make sure you have a computer you can deploy to which can accept HTTP
requests on a public hostname or IP address.  A home computer hooked up to a
home ISP probably won't cut it.

Go to the [GroupMe API][api] site and log in.  Get your access token, and save
it in a file named `.groupy.key` on any computer you're going to run this code.
I'd recommend restricting read permissions on this file, since your access token
is pretty sensitive.

Now, go to the bots section of the [GroupMe API][bots].  Create one.  Give it a
good name, since that's what will show up in the chat.  You'll probably want an
avatar.  In order to do this, you have to upload an avatar to GroupMe's image
hosting service, and then paste that URL in the form.  There is no public upload
form for this, so you'll have to do `curl -F "file=@[filename.png]"
"https://image.groupme.com/pictures?access_token=[your_token_here]"` (fill out
the bracketed stuff yourself).  Finally, you'll want to set the callback URL to
be `http://[your-hostname-here]/callback`.  Also, make sure you set the correct
chat for this bot.

Now, after all that setup, you can run `python bot.py` on your deploy computer
and everything should go swimmingly.

[api]: https://dev.groupme.com/
[bots]: https://dev.groupme.com/bots
[groupy]: https://pypi.python.org/pypi/GroupyAPI
