n= int(input('Enter a number'))
f=1
r=n
while f<=r:
    for i in range(1,round(n/2)+2):
        for j in range(1,n+1):
            if j==f or j==r:
                print('*',end='')
            else:
                print(' ',end='')
        print()
        f=f+1
        r=r-1
