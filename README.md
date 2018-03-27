# Wheel-Of-Lunch-Slack-Bot
A bot to feed the slackers


## Quick Start Guide

#### Installation
##### Python
- Clone this repository
    - `git clone https://github.com/wimo7083/Wheel-Of-Lunch-Slack-Bot.git`
- (Optional, but recommended) Create a new virtual environment using something like [virtualenv](https://virtualenv.pypa.io/en/stable/) or [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- Install dependencies
    - In the root project directory: `pip install -r requirements.txt`

##### Slack
As most of our functionality deals with interactions with the slack API the easiest way to setup a development environment is to create a test Slack Workspace.

- Click the `Get Started` button on https://slack.com
- Click `Create a new workspace`
- Create your workspace
- Go to https://api.slack.com/
    - sign in to your workspace if you aren't already
-  Click Your Apps in the upper right
- Select Create New App
    - Enter the App name and select your development workspace

At this point you'll need a few pieces of information to correctly configure the application.
- Click the `Install App` tab under settings and install the app to your workspace
- Find the following in your slack app    
    - `Verification Token` on the Basic Information page


Go ahead and run the `run.py` file, the server should successfully start.

The only thing left to do is configure a public facing URL that slack can use to send events.
You could use a hosting service to accomplish this but we frequently use [ngrok](https://ngrok.com/) to create a temporary URL that forwards
all traffic to your localhost.

After downloading ngrok create a temporary url on port 5000 using `ngrok http 5000` (or a similar command depending on your OS and where you saved the file)

We now need to create a slash command endpoint and forward all events to a certain endpoint.

We now need to tell Slack to send all events to your forwarding URL.

Back in the Slack App console select the `Event Subscription` tab and click the enable events slider.

Our app is listening for events at the `/event_endpoint` url, until you add more events this is only used for app verification.

Under the `Slash Commands` tab, click the `Create New Command` button and add your `ngrokurl/lunch` entry.  More details [here](https://api.slack.com/slash-commands#what_are_commands)
