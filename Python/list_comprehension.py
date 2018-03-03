#ListOfNumbers = [ x for x in range(10) ]
#print(ListOfNumbers)
#ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0]
#print(ListOfThreeMultiples)

x = int(input())
y = int(input())
z = int(input())
n = int(input())

lc=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n]
print(lc)
