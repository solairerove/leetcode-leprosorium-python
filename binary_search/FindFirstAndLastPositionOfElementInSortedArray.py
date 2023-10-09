from typing import List


# O(log(n)) time || O(1) space
def search_range(self, nums: List[int], target: int) -> List[int]:
    def find_bound(is_first):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                if is_first:
                    if mid == low or nums[mid - 1] < target:
                        return mid

                    high = mid - 1
                else:
                    if mid == high or nums[mid + 1] > target:
                        return mid

                    low = mid + 1

        return -1

    lower_bound = find_bound(True)
    if lower_bound == -1:
        return [-1, -1]

    upper_bound = find_bound(False)

    return [lower_bound, upper_bound]
