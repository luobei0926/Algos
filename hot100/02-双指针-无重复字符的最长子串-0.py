"""
@Time: 2025/2/15 22:51
@Author: yanzx
@Desc:
给定一个字符串 s ，请你找出其中不含有重复字符的 最长
子串的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串
"""
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        right就是i，判断当前i与left
        :param s:
        :return:
        """
        n = len(s)
        if n == 0:
            return n
        left, right = 0, 0
        res = 1
        for i in range(1, n):
            right = i
            while s[i] in s[left:right] and left < right:
                left += 1

            res = max(res, right - left + 1)
        return res



if __name__ == '__main__':
    s = Solution()
    ss = "pwwkew"
    res = s.lengthOfLongestSubstring(ss)
    print(res)
