"""
@Time: 2025/2/16 15:56
@Author: yanzx
@Desc:
给定两个字符串 s 和 p，找到 s 中所有 p 的
异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

示例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

示例 2:
输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
"""
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        通过双指针结合dict频率的方法
        具体来说，当你尝试访问 Counter 中不存在的键时，它会自动将该键的计数初始化为 0，然后再加 1。
        :param s:
        :param p:
        :return:
        """
        count_p = Counter(p)
        res = []
        n_p = len(p)
        n_s = len(s)
        count_s_n_p = Counter(s[:n_p])
        if count_s_n_p == count_p:
            res.append(0)
        for i in range(n_p, n_s):
            count_s_n_p[s[i - n_p]] -= 1
            if count_s_n_p[s[i - n_p]] == 0:
                del count_s_n_p[s[i - n_p]]
            count_s_n_p[s[i]] += 1
            if count_s_n_p == count_p:
                res.append(i - n_p + 1)
        return res


if __name__ == '__main__':
    so = Solution()
    s = "abab"
    p = "ab"
    res = so.findAnagrams(s, p)
    print(res)
