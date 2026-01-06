# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        else:
            queue = deque()
            queue.append(root)

            max_sum = float('-inf')
            max_depth = 0
            depth = 0

            while queue:
                depth += 1
                level_sum = 0
                n = len(queue)

                for _ in range(n):
                    node = queue.popleft()
                    level_sum += node.val

                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

                if level_sum > max_sum:
                    max_sum = level_sum
                    max_depth = depth

            return max_depth
