import tweepy

# tweepy configuration.
consumer_key = 'wK46iy5YQWsyleVUjkHog6N2K'
consumer_secret = '2mE6hTuO2bSEocxbiI7xYfzuQcXV18mw3sXC9PUHniWZPy27Ye'
access_token = '974887504267505665-cSXX2y3oyIpJY1SdhlSL0A54He4jKGg'
access_token_secret = 'iIfksvy9PlqPgQ7Z8yxUSdXMDDVA9FMXyk7Xhd6s4It0K'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

twitter_id='617215483176222720'

tweet=api.get_status(twitter_id)

print 123