
import cmath
"""
#this is a comment

print('hello world!')

number = 1
number2 = 2

#code below will just add to numbers

print(number + number2)

#let the user write something to the console
num1 = input("Enter")

num2 = input("Enter next number")

sum = num1 + num2
print(sum)



#function that will print the area of a triangle

base = float(input("Please enter base: "))

height = float(input("Please enter te height: "))

print(base * height)

#need to add math

number3 = input("Write a number ")

num3 = cmath.sqr(number3)
print(num3)

number4 = input("Write a second number")
"""

#function


def multiplication(num1, num2):
    product = num1 * num2;
    if(product<1000):
        return product
    else:
        return num1 + num2

    number1 = int(input("Enter a valid numer"))
    number2 = int(input("Entera a second number"))
    result = multiplication(number1, number2)
    print("The result is", result)




