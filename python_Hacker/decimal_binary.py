#decimal to binary conversion
a=int(input('enter a decimal number'))
b=[]
c=''
n=2
while(a>0):
    b.append(a%n)
    a=a//n
i=len(b)-1
while(i>=0):
    c=c+str(b[i])
    i=i-1
print('binary output:',c)
    
