# WHAT FUNCTIONS CAN DO ########################
# Function that simply executes some code:
def saying_hello():
	print("hello from your Python script")

# Function that executes and returns a value:
def age_calculator(current_year, year_of_birth):
	age = int(current_year) - int(year_of_birth)
	return age

# Function that calls another function:
def only_if_approved(approved=True):
	if approved:
		saying_hello()
	else:
		print ("not today")
		



# WHY USING FUNCTIONS ########################
# Without Functions
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area
area = length * width

# Calculate perimeter
perimeter = 2 * (length + width)

# Display results
print("Area:", area)
print("Perimeter:", perimeter)

# With Functions
def get_rectangle_dimensions():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    return length, width

def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def display_results(area, perimeter):
    print("Area:", area)
    print("Perimeter:", perimeter)

def main():
    length, width = get_rectangle_dimensions()
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    display_results(area, perimeter)

main()




# DEFAULT VALUES ########################
# optional argument 
def power(base, exponent=2):
    return base ** exponent

result1 = power(3)     
result2 = power(3, 3)  


# Handling Default or Optional Inputs:
def process_data(data, normalize=True, validate=True):
    # Implementation details
    pass

process_data(my_data)               # Uses default values for normalize and validate
process_data(my_data, normalize=False)  # Customizes normalize, uses default for validate


# Avoiding None Checks:
def print_message(message="No message provided"):
    print(message)

print_message()             # Output: No message provided
print_message("Hello!")     # Output: Hello!


# using mutable as default values
# default arguments are evaluated only once when the function is created.
# This is notable with mutable arguments

def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list


result1 = append_to_list(1)
print(result1)  

result2 = append_to_list(2)
print(result2)  


# do this instead
def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


result1 = append_to_list(1)
print(result1)

result2 = append_to_list(2)
print(result2) 




# ARGS and KWARGS ########################
# args
def add(*args):
    result = 0
    for num in args:
        result += num
    return result

print(add(1, 2, 3))  
print(add(4, 5, 6, 7))

# kwargs
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="Wonderland")


# difference between kwargs and dictionaries 
# using kwargs
def test(**kwargs):
    return kwargs

test(a=10, b=20)

# using a dictionary
def test(my_dict):
    return my_dict

test(dict(a=10, b=20))




# GLOBAL and LOCAL SCOPE ########################
# global and local
number = 5 # global variable

def foo():
    number = 10 # local variable
    print(f"local variable {number}") 

foo()
print(f"global variable {number}")


# reading  a global variable
number = 5 # global variable

def foo():
    result = number**2
    print(result)
foo()


# interacting with a local variable
def foo():
    x = 15
    return x
foo()

print(x + 5)


# a little confusion
a = 15

def change():
    # increment value of a by 5
    b = a + 5
    a = b
    print(a)

change()


# difference between reading and modify a global variable
# can't change it unless using the global keyword
counter = 0 # global variable

def foo():
    # global counter
    for num in range(10):
        counter += num
    print(counter)

foo()

# here you are only reading the value
number = 5 # global variable

def foo():
    result = number**2
    print(result)
foo()



# RECURSION ########################
# Factorial without recursion
def factorial(n):
    fact = 1
    if n == 1 or n == 0:
        return 1
    else:
        while n > 0:
            fact = fact * n
            n = n - 1
        return fact
    
user_input = n = int(input("Enter the number: "))
if int(user_input) < 0:
    print("Factorial doesn't exist for negative numbers")
else:
    print(f"{user_input}! is: {factorial(user_input)}")

# 4! --> 4 * 3 * 2 * 1
# n = 4     1 = 1 * 4
# n = 3     4 = 4 * 3
# n = 2     12 = 12 * 2
# n = 1     24 = 24 * 1
# fact = 24


# Factorial with recursion
def rec_factorial(n):
    # base case: n is 0 or 1
    if n <= 1:
        return 1
    # recursive case: n is greater than 1
    else:
        return n * rec_factorial(n - 1)
    
user_input = (int(input("Insert a number: ")))
print(rec_factorial(user_input))


