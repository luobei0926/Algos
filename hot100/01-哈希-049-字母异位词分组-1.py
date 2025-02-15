"""
@Time: 2025/2/15 21:09
@Author: yanzx
@Desc:
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        先切分每个单词为单个字母的形式，排序，再用dict
        """
        d = {}
        for s in strs:
            str_d = sorted(s)
            str_d = ''.join(str_d)
            print(str_d)
            if str_d not in d:
                d[str_d] = []

            d[str_d].append(s)
        res = []
        for k, v in d.items():
            res.append(v)
        return res



