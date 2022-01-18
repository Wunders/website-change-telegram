# website-change-telegram
Deploying your own

#### The Easiest Way [Heroku ONLY 👾]

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Python script that detects updates to urls, and sends a message via telegram.

You can use whatever you would like to transmit a message with the update, a telegram bot message is provided as a base.

## Installation

Just clone the script onto your machine using:

```
git clone https://github.com/Wunders/website-change-telegram.git
```

Install dependencies (create a virtual environment first if you need it):
```
pip install -r requirements.txt
```
https://heroku.com/deploy?template=https://github.com/craziks-creator/website-change-telegram/
## Usage

Create a `.env` file with your bot token and the chat id. 

Make a `urls.txt` file in the same directory as the script. Paste in any urls you would like to check, line by line.

For example:
```
https://www.github.com
https://twitter.com/github
```

You can further run regex espressions on the html of the page to find a specific change.
