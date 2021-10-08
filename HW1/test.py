'''
A simple test program for muplitication turing machine.
The natural numbers are encoded as followings:
for x \neq 0, n(x)=1^x (x * 1s, for example: 3 -> 111)
for x = 0, n(x)=0
Alphabet :{0,1,2,3}, I use 2 to denote the \rightarrow and 3 to denote the \Box.
'''
def mul(a,b,c, i, j,k,q):
    if q[0]=='s':
        if a[i]==2 and b[j]==3 and c[k]==3:
            b[j]=2
            c[k]=2
            i+=1
            j+=1
            k+=1
            q[0]='t'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        else:
            print('error')
            return
    if q[0]=='t':
        if a[i]==2 and b[j]==1 and c[k]==3:
            b[j]=1
            c[k]=1
            i+=1
            j+=1
            q[0]='c'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        elif a[i]==0 and b[j]==3 and c[k]==3:
            b[j]=3
            c[k]=0
            q[0]='h'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        elif a[i]==1 and b[j]==3 and c[k]==3:
            b[j]=1
            c[k]=3
            i+=1
            j+=1
            q[0]='c'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        elif a[i]==0 and b[j]==0 and c[k]==3:
            b[j]=0
            c[k]=0
            q[0]='h'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        elif a[i]==1 and b[j]==0 and c[k]==3:
            b[j]=3
            c[k]=3
            j-=1
            q[0]='r'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        else:
            print('error')
            return
    if q[0]=='c':
        if a[i]==1 and b[j]==3 and c[k]==3:
            b[j]=1
            c[k]=3
            i+=1
            j+=1
            q[0]='c'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        elif a[i]==0 and b[j]==3 and c[k]==3:
            b[j]=0
            c[k]=3
            i+=1
            q[0]='t'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        else:
            print('error')
            return
    if q[0]=='r':
        if a[i]==1 and b[j]==1 and c[k]==3:
            b[j]=1
            c[k]=1
            i+=1
            k+=1
            q[0]='r'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        elif a[i]==3 and b[j]==1 and c[k]==3:
            b[j]=3
            c[k]=3
            i-=1
            j-=1
            q[0]='l'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        elif a[i]==1 and b[j]==2 and c[k]==3:
            b[j]=2
            c[k]=3
            q[0]='h'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        else:
            print('error')
            return
    if q[0]=='l':
        if a[i]==1 and b[j]==1 and c[k]==3:
            b[j]=1
            c[k]=1
            i-=1
            k+=1
            q[0]='l'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        elif a[i]==0 and b[j]==1 and c[k]==3:
            b[j]=3
            c[k]=3
            i+=1
            j-=1
            q[0]='r'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        elif a[i]==1 and b[j]==2 and c[k]==3:
            b[j]=2
            c[k]=3
            q[0]='h'
            mul(a,b,c,i,j,k,q)
            if q[0]=='h':
                return
        else:
            print('error')
            return
    if q[0]=='h':
        print(a)
        print(b)
        print(c)
        return
print("A simple test program for muplitication turing machine. \n The natural numbers are encoded as followings: \n for x not equal to 0, n(x)=1^x (x * 1s, for example: 3 -> 111)\n for x = 0, n(x)=0\n Alphabet :{0,1,2,3}, I use 2 to denote the Rightarrow and 3 to denote the Box.")
print('first case: 3*2, the output when halt:')     
a=[2,1,1,1,0,1,1,3,3,3,3,3,3,3]
b=[3,3,3,3,3,3,3,3,3,3,3,3,3,3]
c=[3,3,3,3,3,3,3,3,3,3,3,3,3,3]
i=0
j=0
k=0
q=['s']
mul(a,b,c,i,j,k,q)

print('second case: 0*2, the output when halt:')  
a=[2,0,0,1,1,3,3,3,3,3,3,3,3,3]
b=[3,3,3,3,3,3,3,3,3,3,3,3,3,3]
c=[3,3,3,3,3,3,3,3,3,3,3,3,3,3]
i=0
j=0
k=0
q=['s']
mul(a,b,c,i,j,k,q)

print('third case: 3*0, the output when halt:')  
a=[2,1,1,1,0,0,3,3,3,3,3,3,3,3]
b=[3,3,3,3,3,3,3,3,3,3,3,3,3,3]
c=[3,3,3,3,3,3,3,3,3,3,3,3,3,3]
i=0
j=0
k=0
q=['s']
mul(a,b,c,i,j,k,q)