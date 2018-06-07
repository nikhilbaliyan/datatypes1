stack = ["romen", "dean"]
stack.append("rock")
stack.append("john")
print(list)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

from collections import deque
queue = deque(["Romen", "seth", "dean"])
print(queue)
queue.append("rock")
print(queue)
queue.append("john")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)