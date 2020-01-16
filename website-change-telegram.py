# UrlChange
# Checks for an updates to a given list of urls, and reports changes

# Tested with Python version 3.7.6

import requests
import re
import os
import schedule
import time

# Send a message via a telegram bot
def telegram_bot_sendtext(bot_message):
    bot_token = 'YOUR_BOT_TOKEN'
    bot_chatID = 'TELEGRAM_USER_CHAT_ID'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def report_change(url):
    html_response = str(requests.get(url))
    file_name = ''.join(x for x in url if x.isalpha()) + ".txt"

    # Check if file exists that matches the page's content
    if os.path.exists(file_name):
        cache_file = open(file_name, "r")
        html_cache = cache_file.read()
        # If the updated set is not equal to the stored set, update and report change
        if html_response != html_cache:
            cache_file = open(file_name, "w")
            cache_file.write(html_response)
            print("website change reported!")
            # Send the message (such as with a telegram bot provided below)
            telegram_bot_sendtext("Website change detected at url: " + url)
        else:
            print("no change")
    else:
        # save the url's html content to a file
        print("no cache file for " + url + " found, creating one...")
        cache_file = open(file_name, "w")
        cache_file.write(html_response)

# Read liust of urls from file
def scan_url():
    # Get list of urls from file:
    with open("urls.txt") as urls_file:
        urls_list = urls_file.readlines()
    urls_list = [x.strip() for x in urls_list]
    # Check each url for changes
    for url in urls_list:
        report_change(url)
        time.sleep(1)

# Initalize script to run every 2 minutes
scan_url()
schedule.every(2).seconds.do(scan_url)
while True:
    schedule.run_pending()
    time.sleep(1)