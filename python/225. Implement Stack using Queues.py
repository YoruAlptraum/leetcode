# allowed operations append(), pop(0), peek(0)
from collections import deque

class MyStackWithList:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack2 = []
        self.stack2.append(x)
        for i in range(len(self.stack)):
            self.stack2.append(self.stack[i])
        self.stack = self.stack2
        print(self.stack)

    def pop(self) -> int:
        return self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
    
# myStack = MyStackWithList()
# myStack.push(1)
# myStack.push(2)
# print(myStack.top()) # return 2
# print(myStack.pop()) # return 2
# print(myStack.empty()) # return False
# print('====================================')
# myStack = MyStackWithList()
# myStack.push(1)
# myStack.push(2)
# myStack.push(3)
# print(myStack.pop())   # 3
# print(myStack.pop())   # 2
# print(myStack.pop())   # 1
# print(myStack.empty()) # True

class MyStackWithDeque:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)
        for _ in range(len(self.stack)-1):
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0

myStack = MyStackWithDeque()
myStack.push(1)
myStack.push(2)
print(myStack.top()) # return 2
print(myStack.pop()) # return 2
print(myStack.empty()) # return False
print('====================================')
myStack = MyStackWithDeque()
myStack.push(1)
myStack.push(2)
myStack.push(3)
print(myStack.pop())   # 3
print(myStack.pop())   # 2
print(myStack.pop())   # 1
print(myStack.empty()) # True