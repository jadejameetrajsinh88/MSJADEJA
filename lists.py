import random as r
'''
l_odd = []
l_even = []


for i in range (1,6):
    a = r.randint(1,101)
    l_odd.append((2*a-1))
print("the list of odd numbers is ",l_odd)
for i in range (1,5):
    b = r.randint(1,101)
    l_even.append(2*b)
print("the list of even numbers is ",l_even)
c=len(l_even)



def list():
    l_odd.pop(2)
    for i in range (2,c+2):
        l_odd.insert(i,l_even[i-2])
    print(l_odd)
list()



def sort():
    l_odd.sort()
    print(l_odd)
sort()



def find():
    l1 =[]
   
    for i in range (1,21):
        x=r.randint(1,51)
        l1.append(x)
    print(l1)
    m = int(input("ënter the number that you want to find"))
    for i in range(1,20):
        if (m == l1[i]):
            print("the index of your number is ",i)
    
find()

'''
# def duplicate():
#     l1 =[]
   
#     for i in range (0, 50):
#         x=r.randint(1,30)
#         l1.append(x)
#     print(l1)
#     m=50
#     l2 = []
#     for i in range (0, m):
#         x=l1.index(l1[i])
#         l2.append(x)
#         if x in l2:
#             l1.pop(x)
#             m-=1
#         # if x==i:
#         #     continue
#         # elif l1[i] == l1[x]:
#         #     del(l1[x])   

# duplicate()



# def plus_minus():
#     l1 =[]
#     l2 =[]
#     l3 =[]
    
#     for i in range (0, 30):
#         x=r.randint(-20,20)
#         l1.append(x)
#     print(l1)
#     for i in range (0, 30):
#         m = l1[i]
#         if m<0:
#             l2.append(l1[i])
#         elif m>=0:
#             l3.append(l1[i])
    
#     print("list that has eliments greater than 0 : ", l3)
#     print("list that has eliments less than 0 : ",l2)


# plus_minus()

# def upper():
#     list = ['meetraj', 'heet', 'ravi', 'karan', 'jainish']
#     for i in range (0, 5):
#         x = list[i]
#         y=x.upper()
#         list.pop(i)
#         list.insert(i, y)
#     print(list)
# upper()


# def converter():
#     temp_fer = [10, 20, 30, 40, 50]
#     for i in range (0,5):
#         temp_fer[i] = (temp_fer[i]-31)*(5/9)
#     print(temp_fer)
# converter()



def stacks():
    stack = []
    def push(y):
        stack.append(y)
    def s():
        print(stack)
    def pop():
        stack.pop()
    
    def find(w):
        if w in stack:
            a1=stack.index(w)
            print("your eliment is on ",a1,"th index, thank you  ")
        else:
            print("eliment is not present in stack!!!")

    o ="yes"
    while o=="yes":
        o = input('     enter "yes" to do operation, or enter "no" to stop :')
        print('''enter s to view all the eliments : 
        entre "push" for insert eliment :
        enter "pop" to delete last eliment :
        enter "find" to find any perticular eliment in stack :''')
        x= input("")

        if x=="push":
            y = input("enter the value that you want to insert in the stacks : ")
            push(y)
        elif x=="s":
            s()
        elif x == "pop":
            pop()
        elif x == "find":
            w = input("enter teh eliment that you want to find in stack :")
            find(w)
stacks()



# def three_lists():
#     l1 = [1,2,3,4,5,6,7,8,9,10]
#     l2 = [2,4,6,8,10]
#     l3 = []
#     for i in range (0 , len(l1)):
#         if l1[i] in l2:
#             continue
#         else:
#             l3.append(l1[i])
#     print(l1)
#     print(l2)
#     print(l3)
# three_lists()