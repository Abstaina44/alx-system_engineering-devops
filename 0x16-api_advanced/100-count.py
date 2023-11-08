#!/usr/bin/python3
""" recursive function that queries the Reddit API """
import requests


def count_words(subreddit, word_list, passed_after="", word_dict={}):
    """ returns title of 10 hot posts """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {"user-agent": 'me'}
    after = passed_after
    params = {"after": after}
    data = requests.get(url, headers=headers, params=params,
                        allow_redirects=False)
    if data.status_code != 200:
        return
    data = data.json()
    try:
        for item in data['data']['children']:
            full_title = item['data']['title']
            title_list = full_title.split()
            for title in title_list:
                for word in word_list:
                    if title.lower() == word.lower():
                        if word.lower() in word_dict:
                            word = word.lower()
                            word_dict[word] = word_dict[word] + 1
                        else:
                            word_dict[word.lower()] = 1
        passed_after = data['data']['after']
        if passed_after is None:
            sorted_list = sorted(word_dict.items(), key=lambda a: a[1],
                                 reverse=True)
            for item in sorted_list:
                print("{}: {}".format(item[0], item[1]))
            return
        else:
            count_words(subreddit, word_list, passed_after, word_dict)
    except Exception:
        return None
