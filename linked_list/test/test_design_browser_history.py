import unittest

from linked_list.DesignBrowserHistory import BrowserHistory


class MyTestCase(unittest.TestCase):
    def test_design_browser_history(self):
        browser_history = BrowserHistory("leetcode.com")
        # You are in "leetcode.com". Visit "google.com"
        browser_history.visit("google.com")
        # You are in "google.com". Visit "facebook.com"
        browser_history.visit("facebook.com")
        # You are in "facebook.com". Visit "youtube.com"
        browser_history.visit("youtube.com")
        # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
        self.assertEqual("facebook.com", browser_history.back(1))
        # You are in "facebook.com", move back to "google.com" return "google.com"
        self.assertEqual("google.com", browser_history.back(1))
        # You are in "google.com", move forward to "facebook.com" return "facebook.com"
        self.assertEqual("facebook.com", browser_history.forward(1))
        # You are in "facebook.com". Visit "linkedin.com"
        browser_history.visit("linkedin.com")
        # You are in "linkedin.com", you cannot move forward any steps.
        self.assertEqual("linkedin.com", browser_history.forward(2))
        # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
        self.assertEqual("google.com", browser_history.back(2))
        # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
        self.assertEqual("leetcode.com", browser_history.back(7))


if __name__ == '__main__':
    unittest.main()
