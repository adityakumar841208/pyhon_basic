import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, priority, value):
        heapq.heappush(self.heap, (priority, value))  # Min-Heap based on priority

    def pop(self):
        return heapq.heappop(self.heap)[1]  # Return only the value, not priority

    def is_empty(self):
        return len(self.heap) == 0

# Example Usage
pq = PriorityQueue()
pq.push(3, "Low Priority Task")
pq.push(1, "High Priority Task")
pq.push(2, "Medium Priority Task")

print(pq.pop())  # Output: "High Priority Task" (lowest priority number)
print(pq.pop())  # Output: "Medium Priority Task"
print(pq.pop())  # Output: "Low Priority Task"
