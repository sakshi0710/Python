a=0
b=1

print(a, end=" ")
print(b, end=" ")
for i in range(1,50):
    c=a+b
    print(c,end=" ")
    a,b=b,c

