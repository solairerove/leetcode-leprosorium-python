import collections


# O(n) time | O(1) space
def max_consecutive_answers(self, answer_key: str, k: int) -> int:
    max_f = i = 0
    cnt = collections.Counter()
    for j in range(len(answer_key)):
        cnt[answer_key[j]] += 1
        max_f = max(max_f, cnt[answer_key[j]])
        if j - i + 1 > max_f + k:
            cnt[answer_key[i]] -= 1
            i += 1

    return len(answer_key) - i
