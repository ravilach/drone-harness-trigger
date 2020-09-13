import os
import requests
import logging
import json

#Example Python Application to call Harness Trigger
#Leverages Requests and OS
#@Authors Luis Redda and Ravi Lachhman

#Harness CI / Drone Pipeline Variables
ACCOUNT_ID = os.environ.get('PLUGIN_ACCOUNTID')
API_KEY = os.environ.get('PLUGIN_APIKEY')
APPLICATION_ID = os.environ.get('PLUGIN_APPLICATIONID')
ARTIFACT_VERSION = os.environ.get('PLUGIN_ARTIFACTVERSION')
HARNESS_WEBHOOK_ID = os.environ.get('PLUGIN_HARNESSWEBHOOKID')
HARNESS_SERVICE_NAME = os.environ.get('PLUGIN_HARNESSSERVICENAME')
HARNESS_ARTIFACT_NAME = os.environ.get('PLUGIN_HARNESSARTIFACTNAME')

log = logging.getLogger("harness-trigger-plugin")
log.debug('Starting Plug-in')

#Harness HTTP API URL
PostURL = "https://app.harness.io/gateway/api/webhooks/" + HARNESS_WEBHOOK_ID + '?accountId=' + ACCOUNT_ID
log.debug('Post URL: ' + PostURL)

#Formulate Payload
# Python Object of Payload
pythonPayload = {
  "application": APPLICATION_ID,
  "artifacts": [
        {"artifactSourceName": HARNESS_ARTIFACT_NAME, "buildNumber": ARTIFACT_VERSION, "service" : HARNESS_SERVICE_NAME}
  ]
}

#Convert the Payload to JSON
jsonPayload = json.dumps(pythonPayload)

#Fire Off Request
response = requests.post(PostURL, headers={'x-api-key': API_KEY,'content-type' : 'application/json'},  data=jsonPayload)

#Get and print Response
jsonResponse = response.json()
print(jsonResponse)

log.debug('End Plug-in')
