import tweepy

CONSUMER_KEY = '9q5VscYk1YTIIfgJRqjAYcegT'
CONSUMER_SECRET = 'Sh5yJ6yFl1zsqTMWD54uuo4tUNiobTY7moYLBElDjytWgbp4lG'
ACCESS_KEY = '1113227752788897793-YjV5oXprVKS9utbCpVqKHVkVRRDnMI'
ACCESS_SECRET = 'eixfndSl3laXwkjmUM7VgQs1gWPuDLqgmqLwiN2t08ZAN'
F_NAME = 'latest_id.txt'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

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

#This method implements the functionality of replying to tweets.
def reply():
    last_id = get_latest_id(F_NAME)
    timeline = api.mentions_timeline(last_id) #obtains a list of tweets starting from the tweet with last_id

    #Starts in reverse(most recent tweet) and iterates through the list and determines if the tweet warrants a reply
    for mention in reversed(timeline):
        print(mention.text) #for testing purposes
        last_id = mention.id
        set_latest_id(last_id, F_NAME) #updates id storage file
        if '#GoodMorning' in mention.text.lower(): #Checks reply condition
            print('responding...')
            api.update_status('@' + mention.user.screen_name + ' Good Morning!!!', mention.id) #api call to reply to tweet

while True:
    reply()
    sleep(30)
