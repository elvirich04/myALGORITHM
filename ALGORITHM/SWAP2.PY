Dataset=["ABS-CBN","GMA","RPN"]
IndexToSwap1=0
IndexToSwap2=1
temp=Dataset[IndexToSwap1]
Dataset[IndexToSwap1]=Dataset[IndexToSwap2]
Dataset[IndexToSwap2]=temp
print(Dataset)
