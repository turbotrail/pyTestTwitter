import redis

# redis Cache class to get and set HashMap values to redis so that user creds in key.json can be stored and accessed

class setCache:
    value=""
    key=""
    r=redis.Redis()
    def __init__(self):   
        self.r = redis.Redis(host='localhost',port='6379') # redis server to be hosted in local - can also be a remote redis server with auth


    def setValue(self,username,key):
        self.r.hmset(username,key)
    
    def getValue(self,username,key):
        return(self.r.hget(username,key))

    def __del__(self): # flush all will clear the redis cache of all credentials
        self.r.flushall()

