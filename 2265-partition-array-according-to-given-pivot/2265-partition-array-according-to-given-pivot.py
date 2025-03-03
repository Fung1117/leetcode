class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater_list = []
        lesser_list = []
        pivot_list = []
        for i in nums:
            if i > pivot:
                greater_list.append(i)
            
            elif i < pivot:
                lesser_list.append(i)

            else:
                pivot_list.append(i)
        return lesser_list + pivot_list + greater_list