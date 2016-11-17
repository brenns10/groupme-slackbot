rm package.zip
zip package.zip bot.py config.py
cd venv/lib/python2.7/site-packages
zip ../../../../package.zip *
cd ../../../..
