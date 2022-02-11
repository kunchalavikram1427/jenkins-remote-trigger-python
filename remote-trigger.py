import requests  # pip install requests
import os 
import json

try:
    # Load current directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    configFile = open(dir_path + "/config.json", "r") 
    # Read configuration file
    configContent = configFile.read()
    # Convert string to Python dict 
    jsonConfigContent = json.loads(configContent)
    # Parse configuration
    jenkins_url = jsonConfigContent['jenkins_url']
    user = jsonConfigContent['user']
    user_token = jsonConfigContent['user_token']
    job_name = jsonConfigContent['job_name']
    job_token = jsonConfigContent['job_token']
    isTheJobParametrized = jsonConfigContent['isTheJobParametrized']

except Exception as e:
    print(f"[Exception]: In using the configuration file: {e}")

# Form the URL
if not isTheJobParametrized:
    url = jenkins_url+'/job/'+job_name+'/build?token='+job_token
    my_data = None
else:
    url = jenkins_url+'/job/'+job_name+'/buildWithParameters?token='+job_token
    my_data = jsonConfigContent['my_data']

print(f"[Info]: Triggering the job: {url}")
# Send the HTTP Request
result = requests.post(url, auth = (user, user_token), data=my_data)

if int(result.status_code) != 201: 
    print(f"[Error]: Triggering remote job failed with status_code: {result.status_code}")
    exit(1)
print(f"[Success]: Remote job triggered successfully with status_code: {result.status_code}")


