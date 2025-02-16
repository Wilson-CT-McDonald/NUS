# Q1
# a) Declaring variables for name, age, and height
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in centimeters: "))

# b) Printing a greeting message using the name
print(f"Hello, {name}!")

# c) Calculating the user’s age 10 years from now
age_in_10_years = age + 10
print(f"You will be {age_in_10_years} years old in 10 years.")

# d) Displaying height in meters by converting height from centimeters
height_meters = height / 100
print(f"Your height in meters is {height_meters:.2f} meters.")

# Q2
# a) Prompting the user to enter a number
userInput = float(input("Enter a number: "))

# b) Checking if the number is positive, negative, or zero
if userInput > 0:
    print("The number is positive.")
elif userInput < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Q3
# a) Prompting the user to input an integer n
n = int(input("Enter an integer n: "))

# b) Using a for loop to print all even numbers from 1 up to n
print("Even numbers from 1 to", n, ":")
for i in range(2, n+1, 2):  # start at 2, increment by 2 to get even numbers, To note that range doesnt include end, hence n+1 is needed when n is an even number
    print(i)

# Q4
# a) Defining a function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# b) Prompting the user to input values for length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# c) Calling the function and displaying the area
area = calculate_area(length, width)
print("The area of the rectangle is: ", area)

