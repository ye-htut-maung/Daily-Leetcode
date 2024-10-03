class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet = set()
        temp = []
        for i in nums:
            if i not in mySet:
                temp.append(i)
            mySet.add(i)
            
        k = 0
        for j in temp:
            nums[k] = j
            k+= 1
        
        return len(mySet)