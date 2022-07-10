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


## Useful Links
```
https://www.geeksforgeeks.org/reading-writing-text-files-python/
```
