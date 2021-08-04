#순열 이용하는 문제 permutation
#시간초과
import itertools
operator=['+','-','*','/']
n=int(input())
number=list(map(int, input().split()))
operator_cnt=list(map(int, input().split()))
max=-1000000001
min=1000000001
result=0
array=[]
for index,i in enumerate(operator_cnt):
    for i in range(0,i):
        array.append(operator[index])

operator_permutation=set(itertools.permutations(array,len(array))) #중복을 제거해줘야함
for i in operator_permutation:
    result=number[0]
    for index,j in enumerate(i):
        if j=='+':
            result=result+number[index+1]
        elif j=='-':
            result=result-number[index+1]
        elif j=='*':
            result=result*number[index+1]
        elif j=='/':
            if result<0:
                result=result*(-1)
                result=result//number[index+1]
                result=result*(-1)
            else:
                result=result//number[index+1]
    if max<result:
        max=result
    if min>result:
        min=result

print(max)
print(min)