0x16. API advanced Python - Scripting - Back-end - API

Tasks 0. How many subs?

Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:

Prototype: def number_of_subscribers(subreddit) If not a valid subreddit, return 0. NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
