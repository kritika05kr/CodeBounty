class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_list = nums1 + nums2
        
        merged_list.sort()  
         
        total_elements = len(merged_list)

        if total_elements % 2 != 0:
            return float(merged_list[total_elements // 2])
        else:
            middle1 = merged_list[total_elements // 2 - 1]
            middle2 = merged_list[(total_elements // 2 - 1)+1]
            return (middle1 + middle2)/2 

solution = Solution()
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
result = solution.findMedianSortedArrays(nums1, nums2)

print("Median:", result)
