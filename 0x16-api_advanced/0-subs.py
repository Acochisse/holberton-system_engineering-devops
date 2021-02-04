#!/usr/bin/python3
"""
Module that queries Reddit API
"""
import requests as r


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'user'}
    endpoint = 'https://reddit.com/r/{}/about.json'.format(subreddit)

    sub = r.get(endpoint, headers=headers, allow_redirects=False)

    if subs.status_code is not 200:
        return 0
    else:
        return subs.json().get('data').get('subscribers')
