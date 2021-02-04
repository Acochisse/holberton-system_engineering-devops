#!/usr/bin/python3
"""
Module that queries the Reddit API
"""


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed"""

    endpoint = "https://reddit.com/r/{}.json?sort=hot&libit=10"
    headers = {'User-Agent': 'Blake'}
    subs = r.get(endpoint.format(subreddit), headers=headers)

    if subs.status_code != 200:
        print(None)
        return 0

    subs = subs.json()
    subs = subs.get('data')
    subs = subs.get('children')

    for key in subs:
        print(key.get('data').get('title'))
