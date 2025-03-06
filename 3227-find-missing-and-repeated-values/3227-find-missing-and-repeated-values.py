class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        repeated = 0
        nums = set()
        int_range = set(range(1, n**2 + 1))
        print(int_range)
        
        for row in grid:
            for i in row:
                if i in nums:
                    repeated = i
                nums.add(i)
        missed = list(int_range - nums)[0]
        print(missed)
        return [repeated, missed]
                
        
        