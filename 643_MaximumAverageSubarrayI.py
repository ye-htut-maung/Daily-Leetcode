class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        p1 = 0
        p2 = p1 + k - 1
        total = 0
        
        for i in range(p1, p2+1, 1):
            total += nums[i]
        
        max_average = total /k
        p1 += 1
        p2 += 1


        
        while p2 < len(nums):

            average = 0.0   
            total = total - nums[p1 -1] + nums[p2]
            average = total / k
            if average > max_average:
                max_average = average
            p1 += 1
            p2 += 1
        
        return max_average
            