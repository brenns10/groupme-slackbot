SlackBot for GroupMe
====================

Have you ever wanted to have a Slackbot in your GroupMe chat? If so, you're in
luck. This is a Python 2/3 implementation of a Slackbot that runs on AWS Lambda,
which is a cheap and efficient way to handle webhooks without going through the
hoops of setting up your own server to handle them.

Setup
-----

This assumes you already have an AWS account with billing info set up, as well
as the AWS CLI installed and an IAM set up on your computer with plenty of
permissions (in particular, you'll want all permissions for Lambda). You'll also
want to be running Linux.

You can start by forking this repository, because you'll need your own copy to
truly make it your own.

### AWS: Create Lambda Function

The first step is to create an empty Lambda function. Go to Lambda in your
Console, and click the blue "create a lambda function" button. Start from the
Python Hello World template.

It will ask you for a trigger. Click the dotted box to create a new one. Select
API Gateway, choose Lambda Microservice, and set the security to Open. In the
next screen, you configure the function itself. Name it `Slackbot`. Type an
informative sentence for the description. You don't need to edit the code,
because we'll provide it from the command line later. Set the handler to
`bot.handle` and under Role, just create a new role without many permissions.
Click next, go over your summarized settings, and then create the function.

You should be presented with an API endpoint. Copy the URL for the next step.

### GroupMe: Create Bot

GroupMe has a Bot API that is tailor made for this sort of thing. You can log
into their [developer site](https://dev.groupme.com), click on Bots in the menu,
and create a new bot. You can use whatever name you'd like... Slackbot is again
a good choice. Make sure you select the correct group for it to join. Paste the
API endpoint from Lambda into the callback URL. Finally, you can set an
avatar... see the GroupMe docs for that. It's not required.

Create the bot and copy its ID.

### AWS: Encrypt Bot ID

The bot ID you have is the only piece of sensitive information standing between
the world and unlimited posting in your GroupMe channel. So you should treat it
like an API key.

In the AWS console, go to the KMS section and create a new key. Make sure your
Lambda role has access to encrypt and decrypt, as well as your normal role. Make
a note of the name of the key.

In your terminal, use the following to encrypt the Bot ID. The key alias is the
name of your key (include the `alias/` part).

```bash
$ aws kms encrypt --plaintext ID_HERE --key-id alias/KEY_ALIAS_HERE
```

The `CiphertextBlob` in the returned JSON object should be copied now!

### Configure The Bot

The Lambda function can handle several different bots, under the assumption that
you have one bot per group. If that's not the case... well you'll need to figure
some stuff out on your own. For most of us, that's not a problem.

GroupMe's callbacks include the ID of the group a message came in, but they
don't include any other identifying information such as the bot ID. This is
likely because the Bot ID is sensitive; anybody in possession of your Bot ID can
spam your group. So in order for your bot to service all the groups, there is a
dictionary mapping group IDs to encrypted Bot IDs, which are decrypted at
runtime.

Within the `BOT_IDS` dict, delete all the entries (they're useless without my
KMS key) and add your own, mapping the group ID (as a string) to the encrypted
Bot ID you created above.

### Deploy!

At this point, you can run my `deploy.sh` script. This zips up our code along
with the requests library, and deploys via the AWS CLI. You will need to have
the AWS tool set up in order to use it.

```bash
$ ./deploy.sh
```

Now, you can talk in GroupMe and get responses from the bot. I'd recommend using
a private group for testing your bot so you don't annoy your friends too much.
You can also test locally using:

```bash
$ python bot.py 'message'
```

This will print out responses on the terminal rather than posting to GroupMe.

Configure Responses
-------------------

The responses are in [config.py]() which you'll certainly want to edit. They
take the form of a list. The list contains a tuple for each response. The first
element of this tuple is a regular expression that must be *found* within the
message (the whole message need not match the regex--if you want that, anchor
your regex with `^REGEX$`). The second element of the tuple is a list of
responses the bot may choose to respond with. These responses will be formatted
before being shown. You can insert:

- `{name}` - the name of the person who sent the message
- `{key}` - where key is the name of any captured field from the regular
  expression

Furthermore, you can apply some formatting elements to make formatted text fit
in more naturally with the text from your response:

- `{name!u}` puts the name in upper case (e.g. "Stephen" to "STEPHEN")
- `{name!l}` puts the name in lower case (e.g. "Stephen" to "stephen")
- `{name!c}` capitalizes the first letter of each word in the name (e.g.
  "stephen" to "Stephen")
- `{name!w}` swaps the case of each letter in the name (this one's mainly just
  for fun) (e.g. "Stephen" to "sTEPHEN")
