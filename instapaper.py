# Hit the Instapaper API
# http://www.instapaper.com/api/full
# http://www.instapaper.com/api/simple
# http://www.instapaper.com/api/developer

# Usage:
# python instapaper.py http://www.google.com

import urllib
import urllib2
import json


with open("instpaper_credentials.txt") as f:
    username = f.readline().strip()
    password = f.readline().strip()


class Instapaper:
    """Instapaper API wrapper."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add(self, url, title=None, description=None, folder_id=None):
        """Add a URL to the user's unread list."""

        params = {
            "username": self.username,
            "password": self.password,
            "url": url,
            "title": title,
            "description": description,
            "folder_id": folder_id,
        }
        return self._request("https://www.instapaper.com/api/add", params)

    def _request(self, url, params):
        data = urllib.urlencode(params)
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        return json.loads(response.read())


if __name__ == "__main__":
    # Add a URL to the user's unread list.
    import sys

    instapaper = Instapaper("username", "password")
    print(instapaper.add(sys.argv[1]))
