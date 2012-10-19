def LinearSearch(Sentence, keyword):
    for data in Sentence:
        if (data.lower()==keyword.lower()):
            return True
    return False
Sentence="I lost my ball"
words = Sentence.split()
result=LinearSearch(words,"ball")
print (words)
print(result)
