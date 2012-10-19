def isPalindrome(words):
    words_letters = [c for c in words.lower() if c.isalpha()]#list comprehension
    print (words_letters)
    return (words_letters == words_letters[::-1])
    #return (words==words[::-1])

s="raCecar"
if(isPalindrome(s)):
    print ("%s is a palindrome"%(s))
else:
    print ("%s is not a palindrome"%(s))
