# website-change-telegram
Python script that detects updates to urls, and sends a message via telegram.

You can use whatever you would like to transmit a message with the update, a telegram bot message is provided as a base.

## Installation

Just clone the script onto your machine using:

```
git clone https://github.com/Wunders/urlcheck.git
```

## Usage

Make a `urls.txt` file in the same directory as the script. Paste in any urls you would like to check, line by line.

For example:
```
https://www.github.com
https://twitter.com/github
```

You can further run regex espressions on the html of the page to find a specific change.
