from typing import List


# O(n) time || O(1) space
def find_duplicate(self, nums: List[int]) -> int:
    slow = fast = nums[0]
    while True:
        slow, fast = nums[slow], nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]

    return slow
