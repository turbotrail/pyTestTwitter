from . import setCache
from . import rest
import requests_oauthlib

header={"content-type":"application/json"}

#seperate methods to access the different twitter API calls for validation - all the methods have username and redis obj for fetching oauth creds

def getTweetStatus(redisObj,username,id):
    endpoint="https://api.twitter.com/1.1/statuses/show.json?id="+id
    return rest.getRest(endpoint,init_auth(redisObj,username))

def reTweet(redisObj,username,id):
    endpoint="https://api.twitter.com/1.1/statuses/retweet/"+id+".json"
    return rest.postRest(endpoint,init_auth(redisObj,username),header,{})

def getReTweetId(redisObj,username,id):
    endpoint="https://api.twitter.com/1.1/statuses/retweeters/ids.json?id="+id+"&count=100&stringify_ids=true"
    return rest.getRest(endpoint,init_auth(redisObj,username))["ids"]

def unReTweet(redisObj,username,id):
    endpoint="https://api.twitter.com/1.1/statuses/unretweet/"+id+".json"
    return rest.postRest(endpoint,init_auth(redisObj,username),header,{})

def deleteTweet(redisObj,username,id):
    endpoint="https://api.twitter.com/1.1/statuses/destroy/"+id+".json"
    return rest.postRest(endpoint,init_auth(redisObj,username),header,{})

def postTweet(redisObj,username,status):
    endpoint="https://api.twitter.com/1.1/statuses/update.json"
    response=rest.postRest(endpoint,init_auth(redisObj,username),header,{"status":status})
    return response["id_str"]

def verifyReTweetId(redisObj,username,id):
    endpoint="https://api.twitter.com/1.1/statuses/retweeters/ids.json?id="+id+"&count=100&stringify_ids=true"
    return rest.getRest(endpoint,init_auth(redisObj,username))["ids"]

# Method to fetch the keys , secret and tokens which were loaded into redis cache from key.json in data folder
def init_auth(redisObj,username): 

	(CONSUMER_KEY,
     CONSUMER_SECRET,
     OAUTH_TOKEN,
     OAUTH_TOKEN_SECRET) = (setCache.setCache.getValue(redisObj,username,"apikey").decode("utf-8"),setCache.setCache.getValue(redisObj,username,"apisecretkey").decode("utf-8"),
     setCache.setCache.getValue(redisObj,username,"accesstoken").decode("utf-8"),setCache.setCache.getValue(redisObj,username,"accesstokensecret").decode("utf-8"))
	 
	auth_obj = requests_oauthlib.OAuth1(
	CONSUMER_KEY, CONSUMER_SECRET,
	OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	return auth_obj
    
