# Hit the Twitter API to list my tweets going back to the beginning
# of time.  This is a bit of a hack, but it works.
#
# This is a Python script, so you'll need to install Python and
# the Python Twitter library.  See the README for more details.
#
# This script is released under the MIT license.  See the LICENSE
# file for more details.
#

import twitter
import sys
import time
import datetime

# This is the number of tweets to fetch per API call.  The Twitter
# API limits this to 200, so don't change it.
TWEETS_PER_PAGE = 200

# This is the number of seconds to wait between API calls.  The
# Twitter API limits this to 15 calls per 15 minutes, so don't
# change it.
WAIT_TIME = 15 * 60 / 15

# Define functions

def get_tweets(api, max_id):
    """Get the tweets from the Twitter API."""
    if max_id:
        return api.GetUserTimeline(count=TWEETS_PER_PAGE, max_id=max_id)
    else:
        return api.GetUserTimeline(count=TWEETS_PER_PAGE)

def print_tweets(tweets):
    """Print the tweets to stdout."""
    for tweet in tweets:
        print tweet.created_at, tweet.text.encode('utf-8')

def main():
    """Main function."""
    # Get the Twitter API object
    api = twitter.Api()

    # Get the tweets
    tweets = get_tweets(api, None)
    print_tweets(tweets)

    # Get the ID of the last tweet
    max_id = tweets[-1].id

    # Loop until we get no more tweets
    while len(tweets) > 0:
        # Wait for the rate limit to reset
        time.sleep(WAIT_TIME)

        # Get the tweets
        tweets = get_tweets(api, max_id)
        print_tweets(tweets)

        # Get the ID of the last tweet
        max_id = tweets[-1].id

if __name__ == '__main__':
    main()


