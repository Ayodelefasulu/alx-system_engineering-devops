#!/usr/bin/python3
import requests

def get_user_agent():
    url = 'https://httpbin.org/user-agent'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['user-agent']
    else:
        return 'Error fetching User-Agent'

if __name__ == '__main__':
    print(get_user_agent())
