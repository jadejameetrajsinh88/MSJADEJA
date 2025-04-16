#problem_01
def count_lower_upper():
    str = input("enter the string :")
    lower = 0
    upper = 0
    for i in str:
        if ord(i)>=97 and ord(i)<=122:
            lower+=1
        elif ord(i)<=90 and ord(i)>=65:
            upper+=1
        else:
            continue
    op = {"lower":lower, "upper":upper}
    print(op)
count_lower_upper()

#problem_02
def compute():
    n = int(input("enter the number:"))
    l = []
    count=0
    for i in range (1,n+1):
        string = str(n)*i
        l.append(int(string))
    for i in l:
        count+=i
    print(count)
compute()

#problem_03
def creat_array():
    a=int(input("enter the first dimention of arry:"))
    b=int(input("enter the second dimention of arry:"))
    c=int(input("enter the third dimention of arry:"))
    x=int(input("enter the value of each eliment of arry:"))
    l1 = []
    l2 = []
    l3 = []
    for i in range (a):
        l1.append(x)
        l2=[l1]*b
        l3=[l2]*c
    print(l3)
creat_array()

#problem_04
def sum_avg(marks):
    total = sum(marks)  
    average = total / len(marks)  
    return total, average 
marks = []
for i in range(1, 6):  
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
total, average = sum_avg(marks)
print(f"Total Marks: {total}")
print(f"Average Marks: {average}")


#problem_05
def ispangram():
    sample = input("enter the sentence :")
    set1 = set(sample.lower())-{" "}
    
    alpha_set = set("abcdefghijklmnopqrstuvwxyz")
    if alpha_set.issubset(set1):
        print("sentence is pangram")
    else:
        print("the sentence is not pangram")
ispangram()


#problem_06
def squareqube():
    x = int(input("enter the number :"))
    l1 = []
    for i in range (1,x+1):
        tuple = (i,i**2,i**3)
        l1.append(tuple)
    return l1
print(squareqube())



#problem_07
def pelindrome():
    x = (input("enter the string :"))
    list1 = list(x)
    while " " in list1:
        list1.remove(" ")
    y = str(list1.reverse())
    if y == x:
        print("pelindrome")
    else:
        print("not palindrome")

#problem_08
def convert():
    string = input("enter the string :")
    list1= list(string)
    while " " in list1:
        list1.remove(" ")
    set1= set(list1)
    
    print("your final string is like :")
    x ="".join(sorted(set1))
    print(x)
    
convert()

#problem_09
def count_alpha_digits():
    num_alpha = 0
    num_digit = 0
    string = input("enter the string :")
    list1 = list(string)
    while " " in list1:
        list1.remove(" ")
    x = str(list1).lower()
    for i in x:
        if ord(i)>=97 and ord(i)<=122:
            num_alpha+=1
        elif ord(i)>=48 and ord(i)<=57:
            num_digit+=1
        else:
            continue
    result = dict()
    result["num_alpha"]=num_alpha
    result["num_digit"]=num_digit
    print(result)
count_alpha_digits()
    
#problem_10
def frequency():
    result = {}
    string = input("Enter the string: ")
    
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    
    
    for char, count in result.items():
        print(f"'{char}': {count}")

frequency()


#problem_11
def create_list():
    string1 = input("Enter the string1: ")
    string2 = input("Enter the string2: ")
    list1 = list(string1)
    list2 = list(string2)
    list3 = []

    for i in list1:
        if i in list2:
            list3.append(i)
        else:
            continue
    print("the intersection of lists : ",list3)
create_list()
