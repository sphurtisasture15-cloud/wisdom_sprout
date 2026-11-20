# Q1) Check if a number is positive, negative, or zero.
num = int(input("Enter the number: "))

if num > 0:
    print("It's a positive number.")

elif num < 0:
    print("It's a negative number.")

else:
    print("It's zero.")

# Q2) check whether a number is even or old
num = int(input("enter the number:"))
if num %2 == 0:
    print("It's even")
else:
    print("It's odd") 

#Q3) find greate of two numbers
num1= int(input("enter num1:"))
num2 = int(input("enter num2:"))
if num1 > num2:
    print(num1,"is greater")
elif num2 > num1:
 print(num2,"is greater")
else:
    print("Both numbers are equal.")

# Q4 find the greatest of three numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(num1, "is greatest.")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is greatest.")
else:
    print(num3, "is greatest.")

# Q5) Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter you age:- "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Q6) Check whether a year is a leap year.
year = int(input("enter year:- "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
     print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Q7) Check if a character is a vowel or consonant.
character = input("Enter an alphabet: ").lower()
if len(character) == 1 and character.isalpha():
    if character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u':
        print("It's a vowel.")
    else:
        print("It's a consonant.")
else:
    print("Invalid alphabet.")

# Q8) Check whether a number is divisible by 5 and 11.
num = int(input("Enter the number: "))
if num % 5 == 0 and num % 11 == 0:
    print("It's divisible by both 5 and 11.")
else:
    print("It's not divisible by both 5 and 11.")

# Q9) check if a number is a multiple of both 3 and 7
num = int(input("Enter the number:- "))
if num % 3 == 0 and num % 7 == 0:
    print("it's multiple by 3 and 7.")
else:
    print("It's not a multiple of both 3 and 7.")

# Q10) Assign grades based on marks:
# 90–100: A
#  80–89: B
#  70–79: C
#  60–69: D
#  Below 60: F

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks.")
elif marks >= 90:
    print("You got A Grade.")
elif marks >= 80:
    print("You got B Grade.")
elif marks >= 70:
    print("You got C Grade.")
elif marks >= 60:
    print("You got D Grade.")
else:
    print("You got F Grade.")

# Q11) Check if a character is uppercase or lowercase.
char = input("Enter a character: ")

if len(char) == 1 and char.isupper():
    print("It's an uppercase character.")
elif len(char) == 1 and char.islower():
    print("It's a lowercase character.")
else:
    print("Invalid character.")
    
# Q12) Find whether the entered alphabet is a vowel using if-elif
char = input("Enter an alphabet: ").lower()

if len(char) == 1 and char.isalpha():
    if char == 'a':
        print("It's a vowel.")
    elif char == 'e':
        print("It's a vowel.")
    elif char == 'i':
        print("It's a vowel.")
    elif char == 'o':
        print("It's a vowel.")
    elif char == 'u':
        print("It's a vowel.")
    else:
        print("It's a consonant.")
else:
    print("Invalid alphabet")

# Q13)Check if three sides can form a triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("It can form a triangle.")
else:
    print("It cannot form a triangle.")

# Q14) Determine the type of triangle (Equilateral, Isosceles, Scalene).
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle.")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle.")
    else:
        print("Scalene Triangle.")
else:
    print("Cannot form a triangle.")

# Q15)Find the largest among four numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Largest number is:", a)
elif b >= a and b >= c and b >= d:
    print("Largest number is:", b)
elif c >= a and c >= b and c >= d:
    print("Largest number is:", c)
else:
    print("Largest number is:", d)

#Q16) Check whether a number is a three-digit number.

num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("It is a three-digit number.")
else:
    print("It is not a three-digit number.")

# Q17) Calculate electricity bill using slab rates.
units = int(input("Enter electricity units: "))
if units < 0:
    print("Invalid units.")
elif units <= 100:
    bill = units * 2
elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3
else:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

if units >= 0:
    print("Total electricity bill: Rs.", bill)


# Q18) Calculate income tax based on income slabs.

income = int(input("Enter your income: "))

if income < 0:
    print("Invalid income.")

elif income <= 10000:
    tax = 0

elif income <= 20000:
    tax = (income - 10000) * 0.05

elif income <= 30000:
    tax = (10000 * 0.05) + (income - 20000) * 0.10

else:
    tax = (10000 * 0.05) + (10000 * 0.10) + (income - 30000) * 0.15

if income >= 0:
    print("Income tax:", tax)

# Q19) Check if a student passes (minimum 35 marks in each subject).

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("You are Pass.")
else:
    print("You are Fail.")

# Q20)Find whether a number is within a given range.

num = int(input("Enter a number: "))

if num >= 10 and num <= 50:
    print("Number is within the range.")
else:
    print("Number is outside the range.")

# Q21)Build a simple calculator using if-elif-else (+, -, *, /).
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator.")

# Q22) Check if a year is a century leap year.
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Century Leap Year.")
elif year % 100 == 0:
    print("Century year but not a leap year.")
else:
    print("Not a century year.")

# Q23)Determine the season based on the month number.
month = int(input("Enter month number (1-12): "))

match month:
    case 3 | 4 | 5:
        print("Summer")

    case 6 | 7 | 8 | 9:
        print("Monsoon")

    case 10 | 11 | 12 | 1 | 2:
        print("Winter")

    case _:
        print("Invalid month number.")

# Q24) Find the number of days in a month.
month = input("Enter month name: ").lower()
year = int(input("Enter year: "))

match month:
    case "january" | "march" | "may" | "july" | "august" | "october" | "december":
        print("31 days")

    case "april" | "june" | "september" | "november":
        print("30 days")

    case "february":
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print("29 days")
        else:
            print("28 days")

    case _:
        print("Invalid month name.")
# Q25) Check whether a password meets minimum conditions (length, digits, etc.).

password = input("Enter password: ")

if len(password) >= 8 and any(char.isdigit() for char in password):
    print("Valid Password")
else:
    print("Invalid Password")
# Q26) Determine ticket price based on age category.

age = int(input("Enter your age: "))
if age < 0:
    print("Invalid age.")
elif age < 5:
    print("Ticket is Free.")
elif age <= 17:
    print("Ticket price: Rs. 50")
elif age <= 59:
    print("Ticket price: Rs. 100")
else:
    print("Ticket price: Rs. 70")

#Q27) Calculate discount based on purchase amount.

amount = float(input("Enter purchase amount: "))
if amount < 0:
    print("Invalid purchase amount.")
else:
    if amount < 1000:
        discount = 0
    elif amount < 5000:
        discount = amount * 0.05
    else:
        discount = amount * 0.10

    final_amount = amount - discount
    print("Discount:", discount)
    print("Final amount:", final_amount)

#Q28) Check if a person is eligible for a driving license (age and eyesight condition).

age = int(input("Enter your age: "))
eyesight = input("Is your eyesight normal? (yes/no): ").lower()
if age < 0:
    print("Invalid age.")
elif age >= 18 and eyesight == "yes":
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")

#29) Create a login system with username and password validation.

username = "admin"
password = "12345"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login Successful")
else:
    print("Invalid Username or Password")

#Q30) Create a menu-driven calculator using if-elif-else.


print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 5:
    print("Thank you!")

elif choice >= 1 and choice <= 4:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)
    elif choice == 2:
        print("Result:", a - b)
    elif choice == 3:
        print("Result:", a * b)
    elif choice == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero.")

else:
    print("Invalid choice.")


