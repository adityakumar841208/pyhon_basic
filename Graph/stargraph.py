from collections import defaultdict

class Solution:
    def findCenter(self, edges):
        
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        for node in graph:
            if len(graph[node]) == len(edges):
                return node
        
        return -1
    
# another solution with O(1) space complexity and O(1) time complexity:
# class Solution:
#     def findCenter(self, edges: List[List[int]]) -> int:
#         seen = set()
#         for i in edges:
#             if i[0] in seen: return i[0]
#             seen.add(i[0])
#             if i[1] in seen: return i[1]
#             seen.add(i[1])
