import tweepy
import time
from twilio.rest import Client

#Twilio API keys and tokens
account_sid = "AC7462e15d3dc7de55f35fa1971f32ce5b"
auth_token  = "f4bbe4412129a90edf1fb09a0279a2d9"
client = Client(account_sid, auth_token)

#Twitter API keys and tokens
CONSUMER_KEY = '9q5VscYk1YTIIfgJRqjAYcegT'
CONSUMER_SECRET = 'Sh5yJ6yFl1zsqTMWD54uuo4tUNiobTY7moYLBElDjytWgbp4lG'
ACCESS_KEY = '1113227752788897793-YjV5oXprVKS9utbCpVqKHVkVRRDnMI'
ACCESS_SECRET = 'eixfndSl3laXwkjmUM7VgQs1gWPuDLqgmqLwiN2t08ZAN'

#Sets up twitter API keys
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

solelinks_id = '2698270332' #user id of the solelinks twitter account
F_NAME = 'latest_id.txt' #latest_id file name

#Will obtain the ID of the latest tweet on the user's timeline from the specified file. Used for filtering of timeline.
def get_latest_id(F_NAME):
    to_read = open(F_NAME, 'r')
    last_id = int(to_read.read().strip())
    to_read.close()
    return last_id

#Saves the ID to the specified file for future comparison.
def set_latest_id(last_id, F_NAME):
    to_write = open(F_NAME, 'w')
    to_write.write(str(last_id))
    to_write.close()
    return

#This method implements the functionality of timeline searching, filtering, and ultimately alerting the user.
def alert():
    last_id = get_latest_id(F_NAME)
    timeline = api.user_timeline(solelinks_id, since_id = last_id) #obtains a list of tweets starting from the tweet with last_id

    #Starts in reverse(most recent tweet) and iterates through the list
    for tweet in reversed(timeline):
        #Updates the latest id file with the greatest ID that has been processed
        last_id = tweet.id
        set_latest_id(last_id, F_NAME) #updates id storage file

        #Filters the tweets by which athlete shoe brands/jerseys I am interested(in this case Jordan, LeBron, Kyrie)
        if 'jordan' in tweet.text.lower() or 'lebron' in tweet.text.lower() or 'kyrie' in tweet.text.lower(): #Checks reply condition
            print('Alerting...')

            #Uses the Twilio API to send a message to my phone from my Twilio free trial phone number
            message = client.messages.create(
                to="+12404447747",
                from_="+12029156653",
                body="Here is a deal you may be interested in! Hurry, deals sell out quick!! https://twitter.com/SOLELINKS/status/" + str(tweet.id))
            print(message.sid)

#Accesses twitter API every 30 seconds as to not exceed the api access limit imposed by Twitter API for developers
while True:
    alert()
    time.sleep(30)
