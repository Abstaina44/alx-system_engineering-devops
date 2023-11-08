#!/usr/bin/python3
""" Queries top 10 posts in a subreddit """
from requests import get, exceptions


def count_words(subreddit, word_list, nxt=None, hash_count=None):
    """ Queries top 10 posts in a subreddit recursively"""
    words = [word.lower() for word in word_list]
    if hash_count is None:
        hash_count = {}
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if nxt:
        url += "&after={}".format(nxt)
    try:
        res = get(url, headers={'User-Agent': 'Safari 20'},
                  allow_redirects=False)
        res.raise_for_status()
        if res.status_code == 200:
            data = res.json()
            if data.get('data').get('children'):
                posts = data.get('data').get('children')
                if len(posts) == 0:
                    print(hash_count)

                for key in words:
                    for x in [post['data']['title'] for post in posts]:
                        if key in x:
                            if hash_count.get(key):
                                hash_count[key] += 1
                            else:
                                hash_count[key] = 1
                if data.get('data').get('after'):
                    nxt = data['data']['after']
                    return count_words(subreddit, word_list, nxt, hash_count)
                else:
                    print(hash_count)
    except exceptions.HTTPError:
        return None
