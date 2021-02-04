#!/usr/bin/python3
"""
Module that queries Reddit API
"""
import requests as r


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Blake'}
    endpoint = 'https://reddit.com/r/{}/about.json'

    sub = r.get(endpoint.format(subreddit), headers=headers)

    if subs.status_code is not 200:
        return 0
    else:
        return subs.json().get('data').get('subscribers')
