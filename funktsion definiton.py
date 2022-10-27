# define function
import math


def print_hello():
    print("Hello")

def get_hello():
 return "Hello"

def ask_name_and_greet_user():
    name = input("Insert your name:")
    capitalized_name = name.capitalize()
    if capitalized_name == "Thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi, {capitalized_name}. Would you like to have a Hamburger?")


def calculate_hypotenuse_lenght(a, b):

    c = math.sqrt(a**2 + b**2)

    return c

func_result = calculate_hypotenuse_lenght(5, 4)
print(func_result)

func_result = calculate_hypotenuse_lenght(10, 8)
print(func_result)
func_result = calculate_hypotenuse_lenght(5, 3)
print(func_result)


# use function
# print_hello()
#func_result = get_hello()
#print (func_result)