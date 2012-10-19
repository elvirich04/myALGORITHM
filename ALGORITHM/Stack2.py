import queue
stack=queue.LifoQueue()
stack.put("Vanilla")
stack.put("Chocolate")
stack.put("Strawberry")

while not stack.empty():
    flavor=stack.get()
    print("I ate %s"%(flavor))
