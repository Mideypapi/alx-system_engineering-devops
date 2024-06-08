#!/usr/bin/python3
"""module that contains a function that queries the Reddit API and prints
the titles of the first 10 hot posts listed for a given subreddit."""


import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
    try:
        response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10")
        if response.status_code == 200:
            posts = response.json()["data"]["children"]
            for post in posts:
                print(post["data"]["title"])
        else:
            print(None)
    except Exception:
        print(None)
