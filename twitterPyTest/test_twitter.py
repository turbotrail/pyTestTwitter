from utility import loadKeys,setCache,twitterAPI  # ---- all the support modules are available in this utility folder
import json
import time


credobj=setCache.setCache()          # ---- creating an cache object which instantiates redis cache connection
username="user1"                     # ---- passing the user key to identify the values from key.json - can also be fetched from external source dynamically
id=""

# ---- different test/requisite steps are in the below methods

def test_loadCred():
    loadKeys.loadCreds(credobj,username)

def test_createTweet():
    global id
    id=twitterAPI.postTweet(credobj,username,"We welcome you to MSD family :)")
    print("Tweet with id: "+id+" created successfully")

def test_reTweet():
    rtweetId=twitterAPI.reTweet(credobj,username,id)
    data=twitterAPI.getTweetStatus(credobj,username,id)
    print("Tweet status after retweet tweetId="+str(data["id"])+" reTweet count"+str(data["retweet_count"]))
    assert data["retweet_count"]==1,"ReTweet count is not updated correctly"
    ids=twitterAPI.verifyReTweetId(credobj,username,id)
    if(rtweetId["user"]["id_str"] in ids):
        print("ReTweeted userid matches with actual reTweeted user")
    else:
        assert 0 , "There is a mismatch in reTweet id"
    if(len(ids)==data["retweet_count"]):
         print("ReTweets count matches with total reTweeters")
    else:
        assert 0 , "There is a mismatch in reTweet id and reTweet count"

def test_unReTweet():
    twitterAPI.unReTweet(credobj,username,id)
    data=twitterAPI.getTweetStatus(credobj,username,id)
    print("Tweet status after Unretweet tweetId="+str(data["id"])+" reTweet count"+str(data["retweet_count"]))

def test_deleteTweet():
    twitterAPI.deleteTweet(credobj,username,id)
    data=""
    try:
        data=twitterAPI.getTweetStatus(credobj,username,id)
    except AssertionError:
        print("Tweet deleted")

# html reports are generated and stored in reports folder using pytest-html - command to execute tests "pytest --html=reports/report.html"
#Sample report already available in reports folder
