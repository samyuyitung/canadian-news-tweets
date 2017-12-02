# encoding: utf-8
import tweepy
import csv
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count

from auth import consumer_key, consumer_secret
from accounts import all_accounts


def get_all_tweets(screen_name):
  print "++++ Fetching tweets for user %s" % (screen_name)
  all_tweets = []
  api = tweepy.API(tweepy.OAuthHandler(consumer_key, consumer_secret))
  
  new_tweets = api.user_timeline(screen_name = screen_name,count=200,tweet_mode='extended')
  all_tweets.extend(new_tweets)
  
  oldest = all_tweets[-1].id - 1
  
  while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest,tweet_mode='extended')
    all_tweets.extend(new_tweets)
    
    oldest = all_tweets[-1].id - 1
  outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")] for tweet in all_tweets]
  
  with open('tweets/%s_tweets.csv' % screen_name, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["id","created_at","text"])
    writer.writerows(outtweets)
  pass
  print "---- Wrote %d tweets to user %s" % (len(all_tweets), screen_name)


if __name__ == '__main__':
  pool = ThreadPool(cpu_count()) 
  results = pool.map(get_all_tweets, all_accounts)
