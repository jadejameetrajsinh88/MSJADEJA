import datetime 




def tuple1():
    l1=['arya','ashra','ragi',('darshit','samir','meetraj'),('rudra','yash')]
    c=0
    for i in range (0,len(l1)):
        if isinstance(l1[i],tuple):
            x=l1[i]
            c+=len(x)
        
    print(c)
tuple1()



def tuple2():
    l1=[(1,'name1',10),(2,'name2',20),(3,'name3',30),(4,'name4',40),(5,'name5',50)]
    roll = []
    name = []
    age = []
    for i in range (0,len(l1)):
        if isinstance(l1[i],tuple):
            x=l1[i]
            roll.append(x[0])
            name.append(x[1])
            age.append(x[2])
    print("roll no :",roll)
    print("names :",name)
    print("age :",age)
tuple2()


def tuple3():
    

    date1 = datetime.datetime(2022, 12, 25)
    date2 = datetime.datetime(2022, 12, 20)


    difference = date1 - date2
    print(difference)
        
       
        
tuple3()



def tuple4():
    l1=[('name1',10),('name2',20),('name3',30),('name4',40),('name5',50)]
    l2 = sorted(l1,key=lambda item: item[1], reverse=True)

    for i in range(len(l1)):
        for j in range(i + 1, len(l1)):
            if l1[i][1] < l1[j][1]:
            # Swap the tuples
                l1[i], l1[j] = l1[j], l1[i]

# Display the sorted list
    print(l1)
tuple4()




def tuple5():
    l1=[(),('name2',20),('name3',30),('name4',40),('name5',50)]
    l0=[]
    for i in range (0,len(l1)):
        r=l1[i]
        if len(r)==0:
            continue
        else:
            l0.append(r)
    print(l0)
tuple5()



def tuple6():
    t1 =(1, 2, 3, 4, 5, 6, 7,8, 9, 0)
    m = input("enter the number that you want to delete :")
    if m in t1:
        n=t1.index(m)
        t2=t1[0:n]+t1[n+1:len(t1)+1]
        print(t2)
    else:
        print("no such eliment available")
    
tuple6()

'''

def tuple7():
    t1 =(1, 2, 3, 4, 5, 6, 7,8, 9, 0)
    print(t1)
    print("enter 'd' to delete eliment :")
    print("enter 'i' to insert eliment :")
    

    x = input("")
    if x=="d":
        tuple6()
    elif x=="a":
        m = input("enter the number that you want to insert :")
        n = int(input("enter the index where you want to insert : "))
        t3 = (m)
        t4=t1[:n]+t3+t1[n+1:]
        print(t4)
tuple7()
'''