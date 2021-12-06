a=int(input())
x=[0 for i in range(1,a+1)]
x[0]=1
for i in range(1,len(x)):
    if i%2==0 or i%3==0 or i%5==0:
        x[i]=i
    else:
        continue
print(x)
#print(x[a-1])