from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, value):
        self.container.append(value)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
def reverse_string(value): 
    stack = Stack()
    for i in value:
        stack.push(i)
    rev_str = ""
    while stack.size()!=0:
        rev_str += stack.pop()
    return rev_str


if __name__ == "__main__":
    obj = Stack()
    print(obj.is_empty())
    print(obj.size())
    obj.push(99)
    obj.push(7)
    obj.push(11)
    obj.push(22)
    print(obj.peek())
    print(obj.pop())

    # 1.exercise
    print(reverse_string("we will conquere COVI-19"))