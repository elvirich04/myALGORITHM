def pyramid(size):
    for i in range(size):
        print ('%s%s'%(' '*(size-(i-1)),'*'*((i*2)+1)))
print(pyramid(3))
