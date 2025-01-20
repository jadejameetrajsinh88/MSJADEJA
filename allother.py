
# def prime():
#     a = int(input("enter the number : "))
#     if a==0 or a==1:
#         print("not valid ")
#     else:
#         print("processing")
        
#     for i in range (2,a):
#         if (a%i == 0):
#             print("the number is not prime")
#             break
#     else:
#         print(" prime")
        
# prime()

# def perfect():
#     a = int(input("enter the number : "))
#     c=0
    
#     if a==0 :
#         print("not valid ")
#     else:
#         print("processing")
#     for i in range (1,a):
#         if a%i == 0:
#             c+=i
#     if a==c:
#         print("the number is perfect")
#     else:
#         print("number is not perfect")
            
# perfect()


# def arm():
#      a = input("enter the number : ")
#      b=len(a)
#      m= int(a)
#      a=int(a)
#      x=0
#      for i in range(0,b+1):
#         d=a%10
#         x=x+d**3
#         a//=10
#      if x==m:
#         print("the number is armstrong")
#      else:
#         print("no sorry !!!!!")
# arm()
     

# def pali():
#     a = int(input("enter the number : "))
#     c=a
#     b=0
#     while a!=0:
        
#         b= b*10 + a%10
#         a//=10
#     if b==c:
#         print("palindrome")
#     else:
#         print('fuck')
# pali()

# def auto():
#     a = input("enter the number : ")
#     b=len(a)
#     m= int(a)
#     c=m**2
#     c=c%(10**(b))
#     if c==m:
#         print("auto morphine")
#     else:
#         print("sorry !!!!!!")
# auto()

# # my code  
# def triplets():
#     for i in range (1,31):
#         for j in range (1, 31):
#             x= (i**2)+(j**2)
#             m=x**(0.5)
#             if type(m) is int:
#                 print(i,j,m)
            
# triplets()


# def triplets():
#     for i in range(1, 31):
#         for j in range(1, 31):
#             x = (i**2) + (j**2)
#             m = x**0.5
#             if m.is_integer():
#                 print(i, j, int(m))

# triplets()

# for i in range(0,24):
#     if i == 0:
#         print(i,":", "00","midnight")
#     elif i >= 1 and i <= 11:
#         print(i,":", "00","am")
#     if i == 12:
#         print(i,":", "00","noon")
#     elif i >= 13 and i <= 23:
#         print(i,":", "00","pm")


# def fact(a):
#     if a==0 or a==1:
#         return 1
#     else:
#         return a*fact(a-1)

# n = int(input("enter the value of n :"))
# r = int(input("enter the value of r :"))

# per = fact(n)/fact(n-r)
# com = per/fact(r)
# print("permutation",per,"combination", com)



# def fact(a):
#     if a==0 or a==1:
#         return 1
#     else:
#         return a*fact(a-1)
# a = int(input("enter the value of n :"))
# fact(a)



# a = int(input("enter the value of n :"))
# def fact():
#     for i in range (a, 0,-1):
#         print(i)
# fact(a)




# def fibo(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=' ')
#         a, b = b, a + b

# n_terms = int(input("enter the number :"))

# fibo(n_terms)

import math

d = float(input("enter the value of x :"))
x=d*(math.pi/180)
i = int(input("enter the value of n :"))   
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)    
def sin():
   
    for n in range (i):
        a=0
        a += (x**((2*n)+1))*((-1)**(n+1))/fact((2*n)+1)    
    print(a) 


sin()



