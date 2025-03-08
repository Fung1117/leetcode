class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int: 
        operation = min_operation = blocks[:k].count('W')
        lt_pt = 0
        rt_pt = k
        while rt_pt < len(blocks):
            if blocks[lt_pt] == 'W' and operation > 0:
                operation -= 1
            if blocks[rt_pt] == 'W':
                operation += 1
            min_operation = min(operation, min_operation)
            lt_pt += 1
            rt_pt += 1
        return min_operation