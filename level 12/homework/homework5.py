# 5) difficult porject ( შექმნით, სარეგისტრაციო ფორმა ჩვენი, სოციალური ქსელისთვის <3 input, while, loop )

user_name_surname = input("enter your name: ")
name_surname = ""
while user_name_surname != name_surname:
    user_name_surname = input("Not a valid name. Please try again: ")
print("registered successully")

user_email = input("enter your email: ")
email = ""
while user_email != email:
    user_email = input("Not a valid email. Please try again: ")
print("registered successully")

user_password = input("enter your password: ")
password = "123"
while user_password != password:
    user_password = input("Not a valid email. Please try again: ") 
print("login successfully!")