class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = set()
        repeated = 0
        int_range = set(range(1, n**2 + 1))
        
        for row in grid:
            for i in row:
                if i in nums:
                    repeated = i
                nums.add(i)
        
        missed = list(int_range - nums)[0]

        return [repeated, missed]
                
        
        