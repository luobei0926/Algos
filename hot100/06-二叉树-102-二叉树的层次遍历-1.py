"""
@Time: 2025/2/17 15:07
@Author: yanzx
@Desc:
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
"""

# Definition for a binary tree node.
from typing import  List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """

        """
        if root == None:
            return []
        res = []
        tmp_res = []
        d = deque
        d.append(root)
        while d:
            for _ in range(len(d)):
                item = d.popleft()
                tmp_res.append(item.val)
                if item.left:d.append(item.left)
                if item.right:d.append(item.right)
            res.append(tmp_res)
        return res



if __name__ == '__main__':
    s = Solution()
    root = [3,9,20,null,null,15,7]

    res = s.levelOrder(root)
    print(res)
