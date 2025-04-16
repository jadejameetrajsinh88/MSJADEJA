#problem_01
def find_prime_factors(num, factor=2):
    
    if num == 1:
        return []

    if num % factor == 0:
        return [factor] + find_prime_factors(num // factor, factor)
    else:
        return find_prime_factors(num, factor + 1)

number = int(input("Enter a positive integer: "))

if number > 0:
    print(f"The prime factors of {number} are: {find_prime_factors(number)}")
else:
    print("Please enter a positive integer.")

#problem_02
def find_binary(num):
    if num == 0:
        return ""
    else:
        return find_binary(num // 2) + str(num % 2)

number = int(input("Enter a positive integer: "))

if number > 0:
    print(f"The binary equivalent of {number} is: {find_binary(number)}")
else:
    print("Please enter a positive integer.")

#problem_03
def count_vowels(string):
    if string == "":
        return 0

    if string[0].lower() in "aeiou":
        return 1 + count_vowels(string[1:])
    else:
        return count_vowels(string[1:])

user_input = input("Enter a string: ")
print(f"The number of vowels in the string is: {count_vowels(user_input)}")

#problem_04
def reverse_list(numbers):
    if len(numbers) <= 1:
        return numbers

    return [numbers[-1]] + reverse_list(numbers[:-1])

user_input = input("Enter a list of numbers separated by spaces: ")
number_list = list(map(int, user_input.split()))

print(f"The reversed list is: {reverse_list(number_list)}")


#problem_05
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))

print(f"The result of {a}^{b} is: {power(a, b)}")

#problem_06
def sanitize_list(numbers):
    if not numbers:
        return []
    sanitized_first = [0] if numbers[0] < 0 else [numbers[0]]
    return sanitized_first + sanitize_list(numbers[1:])

user_input = input("Enter a list of numbers separated by spaces: ")
number_list = list(map(int, user_input.split()))

print(f"The sanitized list is: {sanitize_list(number_list)}")


#problem_07
def calculate_average(numbers, total=0, count=0):
    if not numbers:
        return total / count if count > 0 else 0

    return calculate_average(numbers[1:], total + numbers[0], count + 1)

user_input = input("Enter a list of numbers separated by spaces: ")
number_list = list(map(float, user_input.split()))  # Use float for decimal values

average = calculate_average(number_list)
print(f"The average of the numbers is: {average}")

#problem_08
def string_length(s):
    if s == "":
        return 0
    else:
        return 1 + string_length(s[1:])

user_input = input("Enter a string: ")

print(f"The length of the string is: {string_length(user_input)}")

