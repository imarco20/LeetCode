"""
2. Count Primes
https://leetcode.com/problems/count-primes/
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        numbers = [1]*n

        numbers[0] = 0
        numbers[1] = 0

        count = 0
        m = int(sqrt(n))

        for i in range(0, m+1):
            if numbers[i] == 1:
                for j in range(i*i, n, i):
                    numbers[j] = 0

        return sum(numbers)
