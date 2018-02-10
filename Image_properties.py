##################################

########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, os, string, time

def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "a") as f:
        f.write(contents)
url = ""
userdata = []
###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = 'cae00ff136464a76b449169724a91876'

# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,accessories,blur,exposure,noise',
}

path = "ProfImages"
#url = "https://github.com/Mochael/ProfessorDoppleganger/blob/master/ProfImages/profile.png?raw=true"
body = {'url': url}
print(url)

try:
    # Execute the REST API call and get the response.
    response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)
    userdata = json.loads(response.text)
    #print(parsed[0]["faceAttributes"]["hair"])
    #writeFile('test.txt',(json.dumps(parsed, sort_keys=True, indent=2)))
        
except Exception as e:
    print('Error:')
    print(e)
'''
x = 0
y = 20
for j in range(20):
    for i in range(x,y):
        filename = os.listdir(path)[i]
        url = "https://github.com/Mochael/ProfessorDoppleganger/blob/master/ProfImages/" + filename.replace(" ", "%20") +"?raw=true"
        # Body. The URL of a JPEG image to analyze.
        body = {'url': url}
        print(url)
        
        try:
            # Execute the REST API call and get the response.
            response = requests.request('POST', uri_base + '/face/v1.0/detect', json=body, data=None, headers=headers, params=params)
        
        # print ('Response:')
            parsed = json.loads(response.text)
            writeFile('data.txt',(json.dumps(parsed, sort_keys=True, indent=2)))
        
        except Exception as e:
            print('Error:')
            print(e)
        print(i)
    print(x,y)
    x += 20
    y += 20
    time.sleep(61)
####################################  
'''  
'''
https://github.com/Mochael/ProfessorDoppleganger/blob/master/ProfImages/Aaron%20Johnson.png?raw=true
https://github.com/Mochael/ProfessorDoppleganger/blob/master/ProfImages/Alan%20McGaughey.png?raw=true
https://github.com/Mochael/ProfessorDoppleganger/blob/master/ProfImages/Alan%20McGaughey.png?raw=true
'''