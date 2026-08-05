"""
Problem: Longest Substring Without Repeating Characters
LeetCode #: 3
Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Topic: Sliding Window

Approach:
    Variable sliding window with a HashSet.
    Expand right pointer, shrink left when a duplicate is found.
    Track max window size throughout.

Time Complexity:  O(n)
Space Complexity: O(min(n, 128)) — at most 128 unique ASCII chars
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


# ── Tests ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb")    == 1
    assert sol.lengthOfLongestSubstring("pwwkew")   == 3
    assert sol.lengthOfLongestSubstring("")          == 0
    print("All test cases passed ✅")
