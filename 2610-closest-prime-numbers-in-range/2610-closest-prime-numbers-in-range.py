class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def SieveOfEratosthenes(left, right):
            n = right
            
            prime = [True for i in range(n+1)]
            p = 2
            while (p * p <= n):
                if (prime[p] == True):
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1
            
            return [ i for i in range(max(2, left), right + 1) if prime[i] ]
            

        primes = SieveOfEratosthenes(left, right)
        primes_pair = [-1, -1]
        min_diff = 99999
        print(primes)
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                primes_pair[0] = primes[i]
                primes_pair[1] = primes[i + 1]

        return primes_pair
