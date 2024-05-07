import requests

def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit. Returns 0 for invalid subreddits.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'python-requests/2.22.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

if __name__ == '__main__':
    subreddit_name = input("Enter the subreddit name: ")
    subscribers = number_of_subscribers(subreddit_name)
    print(f"Subscribers: {subscribers}")
