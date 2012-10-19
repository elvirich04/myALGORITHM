import queue

aList=queue.Queue()
aList.put("Mr.A")
aList.put("Mr.B")
aList.put("Mr.C")
print (aList.get())
print (aList.get())

#while not aList.empty():
#   print(aList.get())
