def add_numbers(number1, number2):
    return number1 + number2

def is_even(number):
    return number % 2 == 0

def reverse(text):
    return text[::-1]

def calculate_factorial(d):
    if d == 0 or d == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, d + 1):
            factorial *= i
        return factorial
    
 # Decorator function
def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

# Function to apply the decorator
def apply_decorator(func):
    return func_decorator(func)

# Sorting function that sorts a list of tuples based on the second element (age)
def sort_age(watu):
    return sorted(watu, key=lambda x: x[1])


def merge_dicts(dict1, dict2):
    merged = dict1.copy()  
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  
        else:
            merged[key] = value  
    return merged



class Car:
   
    
    def __init__(self, make, model, year):
        """
        Initializes the Car with make, model, and year.
        """
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """
        Returns a formatted string with the car's information.
        """
        return f"Car Information: {self.year} {self.make} {self.model}"
