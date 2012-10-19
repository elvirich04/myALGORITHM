def isPalindrome(phrase):
    phrase_letters = [c for c in phrase.lower() if c.isalpha()]
    print (phrase_letters)
    return (phrase_letters == phrase_letters[::-1])

phrase1 =input("Please enter a word: ")
if isPalindrome(phrase1):
    print ("%s is a palindrome" % (phrase1))
else:
    print ("%s is not a palindrome" % (phrase1))

