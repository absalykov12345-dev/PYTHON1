a=[1,2,3,4,5,6]
b=list()
c=list()
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
        
print(b)
print(c)