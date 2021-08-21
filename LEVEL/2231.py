a=int(input())
sum=0
for i in range(1,a+1):
    number=i
    sum=0
    while number!=0:
        sum=sum+number%10
        number=number//10
    if sum+i == a:
        print(i)
        break
    if i==a:
        print(0)
        break
