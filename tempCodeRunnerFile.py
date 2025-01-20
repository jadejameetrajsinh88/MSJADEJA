loat(input("enter the value of x :"))
x*=(3.14/180)
i = int(input("enter the value of n :"))   
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)    
def sin():
   
    for n in range (1,i+1):
        a=0
        a += (x**((2*n)-1))*((-1)**(n+1))/fact((2*n)-1)    
    print(a) 


sin()
