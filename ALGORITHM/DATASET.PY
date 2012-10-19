def isInList (dataset,searchword):
    for data in dataset:
        if(data ==searchword):
            return True
    return False
    
      
dataset=["Joy","Errol","Jane","Marco","BJ","Ondoy"]

print("Is Joy in the list?")
print(isInList(dataset,"Joy"))
print("Is BJ in the list?")
print(isInList(dataset,"BJ"))
print("Is Sony in the list?")
print(isInList(dataset,"Sony"))
print("Is errol in the list?")
print(isInList(dataset,"errol"))



