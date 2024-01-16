class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dicts = {}
        for i in nums:
            if i not in nums_dicts:
                nums_dicts[i] = 1
            else:
                nums_dicts[i] += 1

        for key, value in nums_dicts.items():
            if value > 1:
                return True
            
        return False