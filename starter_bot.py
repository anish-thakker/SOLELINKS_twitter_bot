import tweepy
print('he')

CONSUMER_KEY = '9q5VscYk1YTIIfgJRqjAYcegT'
CONSUMER_SECRET = 'Sh5yJ6yFl1zsqTMWD54uuo4tUNiobTY7moYLBElDjytWgbp4lG'
ACCESS_KEY = '1113227752788897793-YjV5oXprVKS9utbCpVqKHVkVRRDnMI'
ACCESS_SECRET = 'eixfndSl3laXwkjmUM7VgQs1gWPuDLqgmqLwiN2t08ZAN'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

last_id = ''
timeline = api.mentions_timeline(last_id)
#print(timeline[0].text)
for mention in reversed(timeline):
    print(mention.text)
    if '#GoodMorning' in mention.full_text.lower():
        print('responding...')
        api.update_status('@' + mention.user.screen_name + ' Good Morning!!!', mention.id)
