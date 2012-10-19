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
dataset=[10,20,30,50,80]
keyword=20
result=binary_search(dataset,keyword)
print(result)
