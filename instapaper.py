# List Your Instapaper bookmarks
# http://www.instapaper.com/api/full
# http://www.instapaper.com/api/simple
# http://www.instapaper.com/api/developer

# This scripts uses your Instapaper username and password to
# authenticate to the Instapaper API and then list everything
# in your Instapaper account.

# This script requires the requests library
# http://docs.python-requests.org/en/latest/

# This script requires the BeautifulSoup library
# http://www.crummy.com/software/BeautifulSoup/

# This script requires the lxml library
# http://lxml.de/

# This script requires the html2text library


import requests
import getpass
import sys
import os
import json
import html2text
from bs4 import BeautifulSoup

# Get your Instapaper username and password
username = raw_input("Instapaper username: ")

# Get your Instapaper password
password = getpass.getpass("Instapaper password: ")

# Get your Instapaper API key
api_key = raw_input("Instapaper API key: ")

# Get your Instapaper API secret
api_secret = raw_input("Instapaper API secret: ")

# Get your Instapaper API URL
api_url = raw_input("Instapaper API URL: ")

# Get your Instapaper API URL
api_url = raw_input("Instapaper API URL: ")

# Step through all your bookmarks:

# Get the first page of bookmarks
r = requests.get(api_url + '/api/1/bookmarks/list', auth=(username, password), params={'limit': 500})

# Get the number of bookmarks
bookmarks = r.json()
bookmark_count = bookmarks['bookmark_count']

# Get the number of pages
page_count = bookmarks['page_count']

# Get the number of bookmarks per page
bookmarks_per_page = bookmarks['bookmarks_per_page']

# Page through all the bookmarks
for page in range(1, page_count + 1):

    # Get the next page of bookmarks
    r = requests.get(api_url + '/api/1/bookmarks/list', auth=(username, password), params={'limit': 500, 'page': page})

    # Get the bookmarks
    bookmarks = r.json()

    # Loop through the bookmarks
    for bookmark in bookmarks['bookmarks']:

        # Get the bookmark ID
        bookmark_id = bookmark['bookmark_id']

        # Get the bookmark title
        bookmark_title = bookmark['title']

        # Get the bookmark URL
        bookmark_url = bookmark['url']

        # Get the bookmark description
        bookmark_description = bookmark['description']

        # Get the bookmark time
        bookmark_time = bookmark['time']


