aLine=["Mr.A","Mr.B"]
aLine.append("Mr.C")
aLine.pop(0)
#aLine.remove("Mr.B")
aLine.remove(aLine[0])

i=1
for person in aLine:
    print ("#%i: %s"%(i,person))
    i=i+1
