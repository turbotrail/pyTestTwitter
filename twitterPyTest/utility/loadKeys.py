from . import setCache
import json
def loadCreds(obj,username): # function to load user creds(oAuth) from key json to a redis serverThat can be used as a cache
    with open("data/key.json") as file:
        keys=json.load(file)
        if(username in keys):
            setCache.setCache.setValue(obj,username,keys[username])
        else:
            username=list(keys.keys())[0]
            print(username)
            print(keys[username])
            setCache.setCache.setValue(obj,username,keys[username])

# Note: key.json will contain seperate json objects for different users - users are parametrized to load them to redis
# key.json can also be hosted/fetched as an remote service so the auth credentials can be masked