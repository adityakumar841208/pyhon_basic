class Stackstr:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def show(self):
        for item in self.stack:
            print(item,end="")
    
stack = Stackstr()
stack.push(4)
stack.push(2)
stack.push(8)
stack.push(6)
stack.push(7)
stack.push(2)
stack.pop()
stack.show()





