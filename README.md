# Harness CI / Drone Plug-in Example

Welcome to your first Harness CI / Drone Plug-in example. In this example
can learn the basics in creating a Drone Plug-in. This example assumes
that you have a running Harness CI / Drone instance and access to a 
Harness CD Account. 

If you are looking to get started with Harness CI/Drone, Feel free
to Fork or Clone the [First Drone Project](https://github.com/ravilach/firstdrone).

There are several really great tutorials in getting up and started. The
[Drone Project](https://docs.drone.io/plugins/golang/) has an excellent example
for creating a GoLang plug-in.

This example is written in Python. All that is required to build is the Python File
and the PIP Requirements.txt. The Dockerfile is a minimum Dockerfile to create a
Docker Image of the plug-in which is needed for Drone to execute. 

The main mechanism of getting information from your Drone YAML to the plug-in
follows the below syntax in the Python File. 

```
#Harness CI / Drone Pipeline Variables
ACCOUNT_ID = os.environ.get('PLUGIN_ACCOUNTID')
API_KEY = os.environ.get('PLUGIN_APIKEY'
```

This example project utilizies the Harness CD Webhook integration. Can learn more about
how a [Webhook Trigger in Harness](https://docs.harness.io/article/xerirloz9a-add-a-trigger-2#payload_and_event_type_matrix)
is created. 

## Usage
The usage can follow the [example snippet](https://github.com/ravilach/drone-harness-trigger/blob/master/plug-in-snippet.yaml). Make sure to replace the values with yours. For sensitive
IDs, will leverage the Harness CI / Drone secrets manager. 

```
- name: harness-deploy
  image: rlachhman/drone-harness-trigger:1.0.0
  settings:  
    accountid:
      from_secret: harness_accountid
    apikey: 
      from_secret: harness_apikey
    applicationid: 
      from_secret: harness_applicationid
    harnesswebhookid: 
      from_secret: harness_webhookid
    harnessartifactname: "rlachhman_amazingapp"
    artifactversion: "1.0.1"
    harnessservicename: "Amazing App"
```
## Harness CD Field Mapping
For the plugin can take a look at a detailed example in this [Harness Blog](https://harness.io/2020/09/your-first-cicd-plugin/)
which describes setting up Harness CD. The field mapping below is what the plugin expects and where to find in Harness CD. 

| Field          | Where to find| 
| :------------- | :---------- | 
| Account_ID | In Harness CD, your Harness Account ID, in the URL of your account, or the Manual Trigger view of your Harness Trigger.   | 
| API_Key   | In Harness CD, under Security -> Access Management -> API Keys |
| Application_ID | In Harness CD, in the Manual Trigger view of your Harness Trigger.  |
| Artifact_Version | Either defined by what you want to deploy. Usually in your Docker Registry or Harness CI / Drone configuration.  |
| Harness_Webhook_ID  | In Harness CD, in the Manual Trigger view of your Harness Trigger.  |
| Harness_Service_Name  | Your Service you are deploying to. In this example was “Amazing App”. |
| Harness_Artifact_Name   | The artifact name given to your Service. In this example was “rlachhman_amazingapp” representing the repository and image.  |

Happy plugin-ing!
