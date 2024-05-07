#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return
    
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'python-requests/2.22.0'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if not posts:
            print("No posts found.")
        else:
            for post in posts:
                title = post.get("data", {}).get("title", "")
                print(title)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
