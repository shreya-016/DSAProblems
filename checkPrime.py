class Solution(object):
    def checkPrime(self, num):
        if num <= 1:
            return False
        else:
            for i in range(2, num):
                if num > 1:
                    if (num%i) == 0:
                        return True
                    else:
                        return False
print(Solution().checkPrime(35))
