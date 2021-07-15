from sys import stdin
t=stdin.readline().rstrip()
for i in range(int(t)):
    n=stdin.readline().rstrip()
    n=int(n)
    loc=0
    while True:
        p=n%2
        n=int(n/2)
        if p==1:
            print(loc, end=' ')
        if n==0:
            break
        loc=loc+1
    print()