import itertools
a,b=map(int, input().split())
array=list(map(int, input().split()))
total=0
answer=0
array_permutations=set(itertools.permutations(array,3))
for i in array_permutations:
    total=sum(i)
    if total<=b and answer<=total:
        answer=total
print(answer)