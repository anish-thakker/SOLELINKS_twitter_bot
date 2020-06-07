# SOLELINKS Twitter Bot
This python script functions as a bot for the SOLELINKS twitter page. The SOLELINKS twitter page actively posts exclusive deals on sneakers throughout the day. Often times, these deals go fast and are time-sensitive. This bot was made to help me get a jump on these deals when they come out. The bot sends a text message to my phone every time SOLELINKS tweets about a deal that involves a particular set of shoe brands specified by me(my favorites such as Jordan, LeBron, Kyrie). I used the Twitter API for twitter monitoring and the Twilio API for SMS messaging alerts.

# starter_bot.py file
The starter_bot.py file is the actual script that performs the twitter scraping through the SOLELINKS twitter page for the shoe brands that I specify. I get alerted immediately via text whenever a deal involving the specified shoe brands is posted.

# latest_id.txt file
Text file which stores the id of the most recent tweet. This avoids processing the same tweets again when successive API calls are made. Instead, only tweets after the latest tweet that was processed will be dealt with

# Using the Bot
This bot requires Python3, the Tweepy library, and the Twilio module to be installed.
Python3 can be installed from the Python website, and Tweepy and Twilio can be installed using the pip command.
Run the script locally by typing "python3 starter_bot.py" in your local terminal.

# Twitter API
In order to use the Twitter API, a developer account is needed. Currently, the script contains the old authorization tokens from my developer account, so to run the script please create a developer account, generate your own API keys, and enter the credentials where I have pointed them out in the script.

# Twilio API
In order to send SMS texts through Python, I created a Twilio account. You can create one for free at www.twillio.com.
Once you have created your account, enter the API keys and phone number given to you by Twilio, as well as your real phone number into the python script where I have pointed out.


