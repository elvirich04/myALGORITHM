def LinearSearch(Dataset, keyword):
    for Data in Dataset:
        if (Data==keyword):
            return True
    return False
Dataset=["Arc", "Ball", "Court"]
result=LinearSearch(Dataset,"Court")
print(result)
