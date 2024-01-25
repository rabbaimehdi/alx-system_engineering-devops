#!/usr/bin/python3
"""
number of subscribers
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
