class Solution:
    def mergeArrays(self, nums1, nums2):
        
        map = {}
        
        for id,value in nums1:
            map[id] = value
        for id, value in nums2:
            if id in map:
                map[id] += value
            else:
                map[id] = value

        result = [[id, value] for id, value in sorted(map.items())]
        return result
    
    
solution = Solution()
print(solution.mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]]))


# op should be - [[1,6],[2,3],[3,2],[4,6]]
# Explanation: The resulting array contains the following:
# - id = 1, the value of this id is 2 + 4 = 6.
# - id = 2, the value of this id is 3.
# - id = 3, the value of this id is 2.
# - id = 4, the value of this id is 5 + 1 = 6.

# optimized one from chatgpt 
from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1, nums2):
        merged_map = defaultdict(int)

        # Merge both lists in a single loop
        for lst in (nums1, nums2):
            for id, value in lst:
                merged_map[id] += value

        # Return the sorted result
        return sorted(merged_map.items())

solution = Solution()
print(solution.mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
