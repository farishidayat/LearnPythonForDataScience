import tweepy
from textblob import TextBlob
import csv

# Step 1 - Authenticate
consumer_key= 'DsWgtWDOEFocIdB8tswOYOdu8'
consumer_secret= 'Kx8XfPb68LMIGKlFwCgUx8cdvIZ2CJr8BJI8rkAJpCCKEy1J1u'

access_token= '1096674744642854912-AF8Lc6czgcGUaho0OTWXLijQllfST7'
access_token_secret= '9h1qhqASO5ajaOzDb4SnTnvMKHbzrc1HUByRe5Xf3FoRx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')

csvfile = open('scraped_tweets.csv','w', encoding="utf-8")
csvwriter = csv.writer(csvfile, delimiter=';', lineterminator='\n')
csvwriter.writerow(["Tweet","Sentiment"])

#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:

    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    
    if analysis.sentiment.polarity > 0:
        sentiment = "Positive"
    elif analysis.sentiment.polarity == 0:
        sentiment = "Netral"
    else:
        sentiment = "Negative"
    csvwriter.writerow([tweet.text,sentiment])