import queue
stack=queue.LifoQueue()
s="racecar"

for c in s:
        stack.put(c)

while not stack.empty():
        print(stack.get())
