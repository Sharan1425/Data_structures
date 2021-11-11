stack = []
stack.append("https://www.sap.com/")
stack.append("https://www.sap.com/home")
stack.append("https://www.sap.com/contact")
stack.append("https://www.sap.com/help")

print(stack)
print(stack.pop())  # return the last added items in the stack
# we can use stack[-1] only for getting last items in the stack
print(stack)
print("--------------------------------------------------")

from collections import deque
stack = deque()
stack.append("https://www.sap.com/")
stack.append("https://www.sap.com/home")
stack.append("https://www.sap.com/contact")
stack.append("https://www.sap.com/help")
print(stack)
print(stack.pop())
print(stack)

#print(dir(stack))
#append is add items to the right side of the deque
#appendleft is add items to the left side of the deque