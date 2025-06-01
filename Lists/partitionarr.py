# class Solution:
#     def pivotArray(self, nums, pivot):
#         pt1 = 0  #will point to the greater item
#         size = len(nums)
    
#         for index,data in enumerate(nums):
#             if data < pivot:
#                 nums[index],nums[pt1] = nums[pt1] , nums[index] #swap
#                 pt1 += 1
                
#         # print(pt1)
#         # print(nums)
#         # Second pass: Move elements = pivot after elements < pivot
#         pt2 = pt1
#         for index in range(pt1, size):
#             if nums[index] == pivot:
#                 nums[index], nums[pt2] = nums[pt2], nums[index]
#                 pt2 += 1
        
#         return nums
    
# solution = Solution()
# print(solution.pivotArray([9,12,5,10,14,3,10], 10)) # [9, 3, 5, 10, 10, 12, 14]

class Solution:
    def pivotArray(self, nums, pivot):
        
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pivot_count = 0
        
        # First pass: Place elements < pivot at the beginning
        for num in nums:
            if num < pivot:
                result[left] = num
                left += 1
            elif num == pivot:
                pivot_count += 1
        
        # Second pass: Place pivot elements in the middle
        mid = left
        for _ in range(pivot_count):
            result[mid] = pivot
            mid += 1
        
        # Third pass: Place elements > pivot at the end
        for num in nums:
            if num > pivot:
                result[mid] = num
                mid += 1
        
        return result

    
    
solution = Solution()
print(solution.pivotArray([9, 12, 3, 5, 14, 10, 10], 10)) # [9, 3, 5, 10, 10, 12, 14]
        
        