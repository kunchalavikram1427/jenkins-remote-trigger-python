# jenkins-remote-trigger-python
Trigger jenkins job remotely through python scripts


## OS & JSON Python Library
```
# Get PWD
dir_path = os.path.dirname(os.path.realpath(__file__))
# Open file
configFile = open(dir_path + "/config.json", "r") 
# Read configuration file
configContent = configFile.read()
# Convert string to Python dict 
jsonConfigContent = json.loads(configContent)
# Parse configuration
jenkins_url = jsonConfigContent['jenkins_url']
```
## Run the script
Modify the config.json and run the script as `python remote-trigger.py`

## Other way
config.json
```
{
    "jenkins_url": "JENKINS_URL",
    "username": "JENKINS_USER",
    "token": "JENKINS_USER_TOKEN",
    "job_name": "JOB_NAME",
    "job_token": "JOB_TOKEN",
    "isTheJobParamaterized": true,
    "my_data" : {
        "DOCKERHUB_USERNAME" : "dme",
        "TAG" : "8.88",
        "PUSH": false,
        "DEPLOY_TO": "PROD"
    }
}
```
main.py
```
import requests
import json
from requests.auth import HTTPBasicAuth

with open('config.json', 'r') as f:
  data = json.load(f)

JENKINS_URL = data["jenkins_url"]
USER = data["username"]
TOKEN = data["token"]
JOB_NAME = data["job_name"]
JOB_TOKEN = data["job_token"]
PARAMETERIZED = data["isTheJobParamaterized"]

if not PARAMETERIZED:
  URL =  JENKINS_URL+'/job/'+JOB_NAME+'/build?token='+JOB_TOKEN
  my_data = None
else:
  URL =  JENKINS_URL+'/job/'+JOB_NAME+'/buildWithParameters?token='+JOB_TOKEN
  my_data = data["my_data"]

result = requests.post(URL, auth = HTTPBasicAuth(USER, TOKEN), data=my_data)

if int(result.status_code) != 201:
  print("[Error]: Job failed")
  exit(1)
else:
  print("[Info]: Job executed")
```
## Useful Links
```
https://www.geeksforgeeks.org/reading-writing-text-files-python/
https://www.geeksforgeeks.org/read-json-file-using-python/
```
