class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = 0
        pointer2 = 0

        while (pointer1 < (m + n)) and (pointer2 < n):
            # print("Before: ", nums1[pointer1], nums2[pointer2])
            if nums1[pointer1] > nums2[pointer2]:
                for i in range(m+n-1, pointer1, -1):
                    nums1[i] = nums1[i - 1]
                    # print("in the loop1", nums1)
                nums1[pointer1] = nums2[pointer2]
                pointer1 += 1
                pointer2 += 1
            else:
                if nums1[pointer1] == 0 and pointer1 >= m and( m+n - pointer1) <= (n-pointer2):
                    nums1[pointer1] = nums2[pointer2]
                    pointer1 += 1
                    pointer2 += 1
                else:
                    if nums1[pointer1 + 1] > nums2[pointer2]:
                        for i in range(m+n-1, pointer1 + 1, -1):
                            nums1[i] = nums1[i - 1]
                            # print("in the loop2", nums1)
                        nums1[pointer1 + 1] = nums2[pointer2]
                        pointer1 += 1
                        pointer2 += 1
                    else:
                        pointer1 += 1
                # print(nums1)

                
            
        
