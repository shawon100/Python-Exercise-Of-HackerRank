n=int(input())
row=[]
res=[]
#lc=[[input(),float(input())] for _ in range(n)]

for i in range(n):
    name=input()
    score=float(input())
    row.append([name,score])

#print(row)
row.sort(key=lambda  x:x[1])
fc=row[0][1]
sc=row[1][1]

if sc<0:
    for i in range(len(row)):
        if row[i][1]>=0:
            sc=row[i][1]
            break
elif fc==sc:
    for i in range(len(row)):
        if row[i][1]!=fc:
            sc=row[i][1]
            break



for i in range(len(row)):
       if sc==row[i][1]:
          res.append(row[i][0])

res.sort()

for p in res:
    print(p)