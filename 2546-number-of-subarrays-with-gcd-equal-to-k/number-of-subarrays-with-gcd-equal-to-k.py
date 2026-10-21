import math
class Solution(object):
    def subarrayGCD(self, nums, k):
        c=0
        for i in range(len(nums)):
            gcd=0
            for j in range(i,len(nums)):
                gcd=math.gcd(gcd,nums[j])
                if gcd==k:
                    c=c+1
                elif gcd<k:
                    break
        return c