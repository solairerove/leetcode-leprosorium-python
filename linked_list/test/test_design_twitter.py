import unittest

from linked_list.DesignTwitter import Twitter


class MyTestCase(unittest.TestCase):
    def test_design_twitter(self):
        twitter = Twitter()
        # User 1 posts a new tweet (id = 5).
        twitter.post_tweet(1, 5)
        # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
        self.assertEqual([5], twitter.get_news_feed(1))
        # User 1 follows user 2.
        twitter.follow(1, 2)
        # User 2 posts a new tweet (id = 6).
        twitter.post_tweet(2, 6)
        # User 1's news feed should return a list with 2 tweet ids -> [6, 5].
        # Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
        self.assertEqual([6, 5], twitter.get_news_feed(1))
        # User 1 unfollows user 2.
        twitter.unfollow(1, 2)
        # User 1's news feed should return a list with 1 tweet id -> [5],
        # since user 1 is no longer following user 2.
        self.assertEqual([5], twitter.get_news_feed(1))
        twitter.get_news_feed(1)


if __name__ == '__main__':
    unittest.main()
