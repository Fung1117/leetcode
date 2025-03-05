class Solution:
    def coloredCells(self, n: int) -> int:
        # 1, 5, 13, 
        # 1, 2, 3,

        # 1, 3, 5, 7, 9, 11
        # (1 + 2(n - 1)   )* 2 + 2
        # (2n - 1 )
        # 4n - 2 + 2
        # 4n
        cells = [0, 1, 5]
        
        for i in range(3, n + 1):
            cell = cells[i - 1] + 4 * (i - 1)
            cells.append(cell)

        return cells[n] 
            
