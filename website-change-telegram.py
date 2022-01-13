# UrlChange
# Checks for an updates to a given list of urls, and reports changes

# Tested with Python version 3.7.10

import requests
import re
import os
import schedule
import time
from lxml import html

# Send a message via a telegram bot
def telegram_bot_sendtext(bot_message):
    bot_token = '1675779827:AAE9YVNAjz4A0LiA0TDaewTvYLLfWn9_HTo'
    bot_chatID = '744730993'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def report_change(url):
    html_response = page_content(url)
    file_name = './cache/' + ''.join(x for x in url if x.isalnum()) + ".txt"

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

def to_str(data):
    try:
        return data.decode('UTF-8')
    except (UnicodeDecodeError, AttributeError):
        return data


def stringify_children(node):
    from lxml.etree import tostring
    from itertools import chain
    parts_raw = ([node.text] +
            list(chain(*([c.text, tostring(c), c.tail] for c in node.getchildren()))) +
            [node.tail])
    # We have byte strings in parts_raw
    parts = map(to_str,parts_raw)
    # filter removes possible Nones in texts and tails
    return ''.join(filter(None, parts))

def page_content(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    content_element = tree.xpath('//div[@class="scrollingNotifications_New scrollbar"]')[0]
    return stringify_children(content_element)

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
TELEGRAM_USER_CHAT_ID = os.getenv('TELEGRAM_USER_CHAT_ID')

# Initalize script to run every 2 minutes
scan_url()
schedule.every(2).seconds.do(scan_url)
while True:
    schedule.run_pending()
    time.sleep(1)
