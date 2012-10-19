aList=["VANILLA", "CHOCOLATE"]
aList.append("UBE")
aList.pop()
aList.append("STRAWBERRY")
size=len(aList)
for i in range(size, 0, -1):
    flavor=aList[i-1]
    print("I ate %s."%(flavor))

