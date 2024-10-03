class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        count = 0
        for i in nums:
            if i != val:
                temp.append(i)
                count += 1
        for j in range(len(temp)):
            nums[j] = temp[j]
                    
        return count