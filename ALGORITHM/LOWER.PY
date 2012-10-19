Python 3.2.2 (default, Sep  4 2011, 09:51:08) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Please enter a word:civic
['c', 'i', 'v', 'i', 'c']
civic is a palindrome
>>> ================================ RESTART ================================
>>> 
<function isPalindrome at 0x021B4C48>
>>> ================================ RESTART ================================
>>> 
<function isPalindrome at 0x02404C48>
>>> ================================ RESTART ================================
>>> 
['r', 'a', 'c', 'e', 'c', 'a', 'r']
True
>>> word="HI"
>>> word.lower()
'hi'
>>> word,isalpha()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    word,isalpha()
NameError: name 'isalpha' is not defined
>>> word.isalpha()
True
>>> word="Hi!"
>>> word.isalpha()
False
>>> for c in word:
	print(c)

	
H
i
!
>>> for c in word.lower(0
		    print(c)
		    
SyntaxError: invalid syntax
>>>  for c in word.lower(0
	print(c)
		     
SyntaxError: unexpected indent
>>> for c in word.lower():
	print(c)
