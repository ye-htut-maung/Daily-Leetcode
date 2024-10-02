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

                


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m  + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
                
        
