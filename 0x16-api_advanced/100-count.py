#!/usr/bin/python3
"""
This module contains the count_words function.
"""

import requests

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count in the titles.
        after (str): The 'after' parameter for pagination. Defaults to None.
        counts (dict): A dictionary to store the counts of keywords. Defaults to None.
        
    Returns:
        None
    """
    if counts is None:
        counts = {}
        
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditApp/0.1 by u/YourRedditUsername"}
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    if not data:
        return None

    for child in data.get("children", []):
        title = child.get("data").get("title").lower()
        for word in word_list:
            word_lower = word.lower()
            count = title.split().count(word_lower)
            if count > 0:
                if word_lower in counts:
                    counts[word_lower] += count
                else:
                    counts[word_lower] = count

    if data.get("after"):
        return count_words(subreddit, word_list, data.get("after"), counts)

    if counts:
        sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
    return None
