class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)

            val = 0
            while n > 0:
                digit = n % 10
                val += digit * digit
                n //= 10

            n = val

        return n == 1