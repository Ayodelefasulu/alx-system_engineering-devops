#!/usr/bin/python3
"""
Contains the count_words function
"""

import requests

def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively counts the occurrences of keywords in hot articles of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count occurrences of.
        after (str): Reddit API parameter for pagination (default=None).
        counts (dict): Dictionary to store keyword counts (default={}) - used for recursive calls.

    Returns:
        dict: Dictionary containing counts of each keyword. Keys are lowercase keywords, values are counts.
    """
    if subreddit is None or not isinstance(subreddit, str) or not word_list:
        return counts

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {'User-Agent': 'python-requests/2.22.0'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            return counts
        
        for post in posts:
            title = post.get("data", {}).get("title", "").lower()
            for word in word_list:
                if title.count(word.lower()) > 0:
                    counts[word.lower()] = counts.get(word.lower(), 0) + title.count(word.lower())
        
        after = data.get("data", {}).get("after")
        if after:
            return count_words(subreddit, word_list, after, counts)  # Recursive call with updated after parameter
        else:
            return counts
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return counts

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [word.lower() for word in sys.argv[2].split()]
        counts = count_words(subreddit, word_list)
        if counts:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
        else:
            print("No posts match or the subreddit is invalid.")
