import collections
import heapq
import itertools
from typing import List


class Twitter:

    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def post_tweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets[user_id].appendleft((next(self.timer), tweet_id))

    def get_news_feed(self, user_id: int) -> List[int]:
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[user_id] | {user_id}))

        return [t for _, t in heapq.nsmallest(10, tweets)]

    def follow(self, follower_id: int, followee_id: int) -> None:
        self.followees[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.followees[follower_id].discard(followee_id)
