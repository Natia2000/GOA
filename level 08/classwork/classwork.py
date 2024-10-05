# exc. 1
print("group48 " * 10)
# გვიჩვენებს 10-ჯერ თანმიმდევრობით მოცემულ რიგს

# age = int(input("შეიყვანეთ ასაკი: "))

# It asks the user for an input
# The input from the user in sonverted into an integer
# The integer is stored in a variable


# Examples of automatic data type conversion

x = 5 # integer
y = 2 # integer
z = x/y # float (implicit conversion)
print(z)

a = 3 # integer
b = 1.5 # float
c = a + b # float
print(c)

print(type(5 < 9))
print(type(50 > 100))
print(type(True))
print(type(False))    # all of them are booleans

# data types int, float, str, boolean
#boolean  - True / False


# math operators
# + _ * / // % **

# comparison operators
# >
# <
# <=
# >=
# ==
# !=
print (10 < 11)
print("--------------------------------------")
print (10 == 10) # == უდრის
print (10 != 10) # != არ უდრის


print("----------------------------")
# True - 1
# False - 0
print(int(True) , int(False))


# logical operators საბოლოოდ გამოაქვს boolean type
# and 
# or
# -------------------------------------------------
print("------------------------------------------")
num1 = 3 > 5
num2 = 3 == 3
print(num1 and num2)
# and არის აუცილებლობა! რომ იყოს True ყოველთვის
print( True and True) # True
print (True and False) # False

# print("-------------------------")
# print("group47" and "group48")


# or არ არის აუცილებლობა!
# თუ რომელიმე პირობა შესრულდება, მასინ ეს ჩვენი კოდი გამოიყვანს True
print(True or False) # True
print(False or True) # True
print(False or False) # False

light_on = True
door_locked = False
print(light_on or door_locked)


# light_on = true
# door_locked = false
# print(light_on OR door_locked)
# print(light_on AND door_locked)

