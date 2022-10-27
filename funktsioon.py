def func():
    print ("I´m inside the function")
func()
def my_name_is(name):
    print(f"my name is {name}")

my_name_is("Sten")

num = "1"
def sum_six(num):
    return 6 + num
print(sum_six(1))
print(sum_six(6))

def sum_numbers (a, b):
    return a + b

print(sum_numbers(5, 5))
print(sum_numbers(0, 25))

def usd_to_eur(dollar):
   return round(dollar * 0.8)
print(usd_to_eur(100))
