# pyTestTwitter
Simple pyTest example to test twitter api's like post tweets, retweets, delete tweets etc.

Coverage:
Steps covered as part of this sample pytest frame work

1.Have your twitter login details in a file and use the same to achieve the following. Make sure you remove your login details before sending it to us.
The tests should run if we give our login details in the file.
2.Make a new tweet with the text "We welcome you to MSD family :)"
3.Now retweet the same tweet.
4.Now get the retweet count & retweeters ID and validate the correctness of the data.
5.Now revert the previous retweet (un retweet the above tweet) and get the retweet count & retweeters ID and validate the correctness of the data.
6.Now finally delete the tweet.

Technolgies Used:

Testing Frame work used = Pytest

Other technologies used = Redis OSS cache, Python

Reference for Twitter Rest api's:
https://developer.twitter.com/en/docs/twitter-api/v1/tweets/post-and-engage/api-reference/post-statuses-update

Twitter api's Authentication = OAuth v1.0 (All details can be obtained when you sign up for twitter developer access with an sample app)

Redis service is used as an cache for loading User credentials for OAuth like apikey,apikeySecret,accesstoken,accesstokenSecret.

Why Redis?

Redis cache is fast and is used for realtime data caching - Redis cache can be Flushed after the run time which make zero visibility of sensitive data - Redis makes it very easy to store and retrive hashmaps,key:values etc


Structure:
Tests are defined and available in the root folder , other useful functions and supporting methods are defined as seperate packages in /utility/* folder

Requirements:

All the requirements are mentioned in the requirements.txt file which can be installed using pip

Redis remote/local server should be up an running in port 6379 - Rdis for windows can  be installed using "https://github.com/tporadowski/redis/releases", Linux using "https://redis.io/download"

Execution :

The tests can be executed when you run the following command

"pytest --html=reports/report.html" in the project folder

BDD like Cucumber can aslo be integrated with this simple frame work

Analysis:

pytest-html module is used so the reports genrated are stored as HTML in reports/ folder

HTML report provides all the console logs and assertion failure details if any step by step

Note: Source code is appended with appropriate comments explaining the methods and their functionality






