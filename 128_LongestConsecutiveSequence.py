class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        longest = 0
        for num in nums:
            count = 1
            if num - 1 not in mySet:
                temp = num + 1

                while (temp in mySet):
                    count += 1
                    temp += 1
                longest = max(longest, count)
        
        return longest