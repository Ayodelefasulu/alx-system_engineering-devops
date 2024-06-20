#!/usr/bin/python3
"""
This module contains the recurse function.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list containing the titles of all hot articles
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list of hot article titles. Defaults to an empty list.
        after (str): The 'after' parameter for pagination. Defaults to None.

    Returns:
        list: A list of titles of hot articles, or None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditApp/0.1 by u/Ayodelefasulu"}
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    if not data:
        return None

    hot_list.extend([child.get("data").get("title") for child in data.get("children", [])])

    if data.get("after"):
        return recurse(subreddit, hot_list, data.get("after"))
    return hot_list
