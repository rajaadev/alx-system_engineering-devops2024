#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Custom User Agent'
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 302:
            # Redirect error code; assume invalid subreddit
            return 0
        else:
            # Other HTTP errors
            return 0
    except requests.RequestException:
        # Handle network or request errors
        return 0
