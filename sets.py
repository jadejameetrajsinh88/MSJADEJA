#problem_01
"""
main_string = "MeetRAjSInh"
set1 = set(main_string.upper())
print(set1)

#problem_02

import random as a

set2 = set()
count = 0

for _ in range(10):  
    x = a.randint(15, 45)
    set2.add(x)

print("Your set is like:", set2)

to_discard = set()
for value in set2:
    if value < 30:
        count += 1
    elif value > 35:
        to_discard.add(value)  

for value in to_discard:
    set2.discard(value)

print("Updated set:", set2)
print("Count of values less than 30:", count)



#pproblem_03

set1 = set()
set_add = {"meetarj", "meet", "abhishek", "jani", "jainish" }
set_remove = {"meet", "jainish"}
set_add_next  = {"priyanshi"}
set1.update(set_add)
print(set1)
for i in set_remove:
    set1.remove(i)
print(set1)
set1.update(set_add_next)
print(set1)


#problem_04


all_names = {"Alice", "Bob", "Bharlie", "Anna", "Bella", "Avid", "Andrew", "Betty", "Bve","Ashol"}

set_a = set()
set_b = set()

for i in all_names:
    x=i[0]
    if x[0].lower() == "a":
        set_a.add(i)
    else:
        set_b.add(i)
print("Names starts with A :",set_a)
print("names starts with B :",set_b)

"""

