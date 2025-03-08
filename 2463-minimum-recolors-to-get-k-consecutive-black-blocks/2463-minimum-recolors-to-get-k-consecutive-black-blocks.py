class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int: 
        min_operation = float("inf")
        for i in range(len(blocks) - k + 1):
            min_operation = min(min_operation, blocks[i : i + k ].count('W'))
        return min_operation