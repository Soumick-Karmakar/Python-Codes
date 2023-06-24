s=input('Enter the size of the pattern')
s=int(s)
k=s
m=1
for i in range(1,s+1):
    for j in range(1,k+1):
        m=m%(s+1)
        print(m,end='')
        m=m+1
    print()
 
