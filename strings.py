def vowels():
    a = input("enter the string :")
    b = "aeiouAEIOU"
    count = 0
    for i in a:
        for j in b:
            if i==j:
                count+=1
    print(count)
vowels()