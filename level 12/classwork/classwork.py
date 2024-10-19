# for i in range(100)
#   print("*" * i)
  
  
  # ფუნქციებს გადაეცემათ ()-ში არგუმენტები, მაგალითები
  # range ---> 3 არგუმენტი,
  # range (start, end. step)
  
  # range(0, 10, 1)
  # 
  # range(10)
  
for i in range(5, 10, 1):
     print(i)
    


# loop for / while

# while statement :
# while True/False


i = 0
while i < 10:
     print("Umar!", i)
     # i = i + 1
     i += 1
     
print("--------------------------")

i = 10
while i > 0:
    print("umar!", i)
    i -= 1
    
    
    
user_password = input("enter your password: ")
password = "123"
while user_password != password:
    user_password = input("Please try again: ") 
print("login successfully!")