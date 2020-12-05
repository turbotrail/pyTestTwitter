import requests

def getRest(endpoint,authObj): # common GET call method to fetch values from an endpoint
    response=requests.get(endpoint,auth=authObj)
    print(response.status_code)
    check(endpoint,str(response.status_code),response.json())
    return response.json()

def postRest(endpoint,authObj,header,payload):  # common POST call method to post values to an endpoint
    response=requests.post(endpoint,headers=header,auth=authObj,params=payload)
    print(response.status_code)
    check(endpoint,str(response.status_code),response.json())
    return response.json()

def check(endpoint,status,res): # Assertion method to check for most commont http status ( additional error status code can be added futher for more details)
    statusCheck={"400":"The request was invalid or cannot be otherwise served.",
                "403":"The request is understood, but it has been refused or access is not allowed.","404":"The URI requested is invalid or the resource requested, such as a user, does not exist.","429":"Returned when a request cannot be served due to the App's rate limit having been exhausted for the resource.",
                "500":"Internal Server error","502":"Bad Gateway","503":"Service Unavailable as servers are oveloaded"}
    if(status in statusCheck):
        print(res)
        assert 0 , status+" "+statusCheck[status]+" for "+endpoint
    elif(status=="200"):
        print("Post/get call successful with 200 ok")
    else:
        assert 0 , status+" response: "+res+" for "+endpoint
       
        