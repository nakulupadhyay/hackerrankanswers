a,b=input().split()
a=int(a)
b=int(b)
k=int(input())
rec=a&b
rec1=a|b
rec2=a^b
if rec>=k:
    rec=0
if rec1>=k:
    rec1=0
if rec2>=k:
    rec2=0
m=max(rec,rec1,rec2)
print(m)
