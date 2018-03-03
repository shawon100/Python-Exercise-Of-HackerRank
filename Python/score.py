n=int(input())
l=(input()).split()
p=[]
for i in range(0,len(l)):
    m=int(l[i])
    if m not in p:
      p.insert(i,m)

p.sort(reverse=1)
#print(p)
print(p[1])