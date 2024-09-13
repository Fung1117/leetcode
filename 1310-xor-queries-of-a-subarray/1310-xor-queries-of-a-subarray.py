class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix_sum = [0] * n
        current = 0
        for i in range(n):
            current ^= arr[i]
            prefix_sum[i] = current
        result = []
        for query in queries:
            if query[0] == 0:
                answer = prefix_sum[query[1]]
            else:
                answer = prefix_sum[query[1]] ^ prefix_sum[query[0] - 1]
            result.append(answer)
        return result