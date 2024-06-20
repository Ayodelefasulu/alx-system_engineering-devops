#!/usr/bin/python3
"""This Reddit api request gets number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot"}  # Set a custom User-Agent to avoid Too Many Requests errors

    try:
        response = requests.get(url, headers=headers)
        response_content = response.content.decode("utf-8")

        if response.status_code == requests.codes.ok:
            # Check if the response is "success" or valid JSON
            if response_content.strip() == "success":
                return 0
            else:
                data = json.loads(response_content)
                return data["data"]["subscribers"]
        else:
            # Handle other status codes (e.g., 404 for invalid subreddit)
            return 0
    except (requests.RequestException, json.JSONDecodeError):
        return 0
