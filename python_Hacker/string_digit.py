#to differ digits and characters in a given string
a=input('enter a string')
b=[]# to store digits
c=[]#to store charecters
l=len(a)
for i in range(l):
    if(a[i].isdigit()):
        b.append(a[i])
    else:
        c.append(a[i])
print(b,'\n',c)

#count the number of digits and charecters in a given string
a=input('enter a string')
c=0 #count the number of digits in a string
d=0 #count the number alphabets in a string
for i in range(len(a)):
    if(a[i].isdigit()):
        c+=1
    elif(a[i].isalpha()):
        d+=1
    else:
        False
print('number of digit:',c,'\n','number of charecter:',d)
