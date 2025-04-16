
#problem_01
def fun():
    print("this is function :")
def msg():
    print("this is msg :")
def disp():
    print("this is disp :")
list1 = [disp,fun,msg]

for i in list1:
    i()

#problem_02
list1 = [1,2,3,4,5,6]
list2 = [6,5,4,3,2,1]
m1 = map(lambda x,y: x+y , list1,list2)
print(list(m1))

#problem_03
import random as r
list1 = []
for i in range (10):
    list1.append(r.randint(-15,15))
m1 = map(lambda x: x**2, list1)
print(list(m1))


#problem_04
lst = ['madam','Python',"malayalam",12321]
def pelindrom(x):
    y = str(x)
    return True if y == y[::-1] else False

print(list(filter(pelindrom,lst)))

#problem_05
faculty = ["punitjain","nirav","darshit","manivel","prakashchandra","parthprajapati","nanji"]
print(list(filter( lambda x :len(x)>=8,faculty)))