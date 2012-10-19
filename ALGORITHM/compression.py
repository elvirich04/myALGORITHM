import zlib
s="Hello Jhane"
s=s.encode("utf-16")
a=zlib.compress(s)
print (a)
b=zlib.decompress(a)
b=b.decode("utf-16")
print (b)

