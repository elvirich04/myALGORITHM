def binary_search(dataset,keyword):
    min=0
    max=len(dataset)-1 
    while True:
        if(max<min):
            return False
        mid=(min + max)/2
        mid=int(mid)
        if(dataset[mid]<keyword):
            min=mid + 1
        elif(dataset[mid]>keyword):
            max=mid -1
        else:
            return mid
dataset=["Errol", "Jhane", "Kobe", "Marco", "Sony"]
keyword="Sony"
result=binary_search(dataset,keyword)
print(result)
