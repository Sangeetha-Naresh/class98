f=open("testfile.txt")
#print(f.read())

flines=f.readlines()
print(type(flines)) # stores lines as  a list type

for lines in flines:
    print(lines)
