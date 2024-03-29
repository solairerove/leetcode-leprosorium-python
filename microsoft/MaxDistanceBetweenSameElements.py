#
# We are given a string S consisting of N lowercase letters.
# A sequence of two adjacent letters inside a string is called a digram.
# The distance between two digrams is the distance between the first letter of the first digram
# and the first letter of the second digram.
#
# For example, in string S "akcmz" the distance between digrams "k" and "mz" is 2.
#
# We want to find the maximum distance between the furthest identical digrams inside string S.
#
# If there are no two identical digrams inside S, your function should S return -1.
#
# Examples:
#
# 1. Given S = "aakmaakmakda" your function should return 7.
# The furthest identical digrams are "ak's, starting in positions 2 and 9.
#
# 2. Given S = "aaa" your function should return 1.
# The furthest identical digrams are "aa's starting at positions 1 and 2.
#
# 3. Given S = "civic" your function should return -1.
# There are no two identical digrams in S.
#
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range (2..300,000];
# string S is made only of lowercase letters (a-z).
#

# O(n) time | O(n) space
def maximum_identical_adjacent_distance(self, s: str) -> int:
    if len(s) == 2:
        return -1

    pair_to_idx, distance = {}, -1
    for i in range(len(s) - 1):
        pair = s[i] + s[i + 1]
        if pair in pair_to_idx:
            distance = max(distance, i - pair_to_idx[pair])
        else:
            pair_to_idx[pair] = i

    return distance
