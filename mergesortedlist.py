class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while( m + n > 0):
            if(n == 0):
                m = 0
            elif(m == 0 ):
                nums1[i] = nums2[j]
                i = i + 1
                j = j + 1
                n = n - 1
                print("teste")
            elif(m > 0 and nums1[i] <= nums2[j]):
                m = m - 1
                i = i + 1
            elif(n > 0 and nums2[j] <= nums1[i]):
                nums1[i],nums2[j] = nums2[j],nums1[i]
                m = m - 1
                i = i + 1
                nums2.sort()

        print(nums1)

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3

Solution().merge(nums1,m,nums2,n)

