n=int(input())
name=[]
score=[]

for i in range(n):
    line=input().split()
    nn=line[0]
    name.append(line[0])
    score.append([float(line[1]),float(line[2]),float(line[3])])


result_dict={name[i]:score[i] for i in range(n)}
fr=input()
num=result_dict[fr]
average=sum(num)/3
print('%0.2f' %average)


