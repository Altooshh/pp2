def grams_to_ounces(grams):
    return 28.3495231 * grams

print(grams_to_ounces(100))




def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

print(fahrenheit_to_celsius(100))  





def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return "No solution"

print(solve(35, 94))  





def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

print(filter_prime([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))





from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print(''.join(perm))

print_permutations("abc")  





def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse_sentence("We are ready")) 




def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False




def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False




import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

print(sphere_volume(3)) 




def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

print(unique_elements([1, 2, 2, 3, 4, 4, 5])) 




def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False




def histogram(lst):
    for num in lst:
        print('*' * num)

histogram([4, 9, 7]) 




import random

def guess_number():
    number = random.randint(1, 20)
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    attempts = 0
    while True:
        guess = int(input("Take a guess. "))
        attempts += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

guess_number()




import math

def sphere_volume(radius):
    """Вычисляет объём сферы по заданному радиусу"""
    return (4/3) * math.pi * radius**3

def is_palindrome(s):
    """Проверяет, является ли строка палиндромом"""
    s = s.replace(" ", "").lower()
    return s == s[::-1]
