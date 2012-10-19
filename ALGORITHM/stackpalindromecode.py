import queue
stack=queue.LifoQueue()
s="school"
isPalindrome=True
for c in s:
        stack.put(c)

i=0
while not stack.empty():
    if(stack.get()!=s[i]):
        isPalindrome=False
    
    i+=1
if (isPalindrome):
    print("%s is a palindrome " % (s))
else:
    print("%s is not a palindrome " % (s))


