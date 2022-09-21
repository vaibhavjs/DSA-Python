# Leetcode - 3
# Longest Substring Without Repeating Characters:
# Sliding Window Technique:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tempSet = set()
        ans = 0
        l = 0

        for r in range(len(s)):
            while s[r] in tempSet:
                tempSet.remove(s[l])
                l += 1
            tempSet.add(s[r])
            ans = max(ans, r-l+1)

        return ans
