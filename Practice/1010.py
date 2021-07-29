import math
n=int(input())
for i in range(0,n):
    a,b=map(int, input().split())
    result=math.factorial(b)/(math.factorial(a)*math.factorial(b-a))
    print(int(result))
