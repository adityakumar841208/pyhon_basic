import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.heap = []  # Min-heap for returned numbers
        self.present = set()  # Set to track numbers in heap
        self.next_num = 1  # The next smallest number in the infinite set

    def popSmallest(self):
        if self.heap:
            # Pop from heap if any numbers were added back
            smallest = heapq.heappop(self.heap)
            self.present.remove(smallest)
            return smallest
        else:
            # Otherwise, return the next natural number
            self.next_num += 1
            return self.next_num - 1

    def addBack(self, num: int):
        # Only add back if it's smaller than next_num and not already in heap
        if num < self.next_num and num not in self.present:
            heapq.heappush(self.heap, num)
            self.present.add(num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
obj.addBack(2)
obj.popSmallest()
obj.popSmallest()
obj.popSmallest()
obj.addBack(1)
obj.addBack(2)
obj.addBack(3)