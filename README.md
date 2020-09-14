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

Happy plugin-ing!
