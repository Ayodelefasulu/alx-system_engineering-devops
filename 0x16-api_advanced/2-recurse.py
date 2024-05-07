#!/usr/bin/python3
"""
Contains the recurse function
"""

import requests

def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store hot article titles (default=[]).

    Returns:
        list: List containing titles of all hot articles for the subreddit. Returns None if no results found.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None
    
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {'User-Agent': 'python-requests/2.22.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            return None
        
        for post in posts:
            title = post.get("data", {}).get("title", "")
            hot_list.append(title)
        
        after = data.get("data", {}).get("after")
        if after:
            return recurse(subreddit, hot_list)  # Recursive call with updated after parameter
        else:
            return hot_list
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
