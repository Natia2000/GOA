# name = "davit"
# name = "George"
# name = name + "davit"
# ✌
# name += "davit"
# print(name)


"""-- შექმნილი გვაქვს res. უნდა დავუმატოთ და თან გავუტოლოთ თითოეული ცვლადის მნიშვნელობა, ოღონდ ისე, რომ ჩვენს ცვლადებს ემატებოდეს + " " სიმბოლო და საბოლოოოდ დავპრინტოთ res 
R e n g k o g u ✔
"""

name = "Rengoku"
res = ""
for i in name:
    # pass code
    res += i + " "
print(res)

print("--------------------------------------")

for i in "giorgi":
    print(i)
    
    
    
# if statements / მოქმედება ------------ true, false

if 3 < 4: #True
    print("this is true")
elif 3 > 4:
    print("this is still true!!")
elif 3 < 4: #else if
    print("this is still true!!")
elif 3 > 4:
    print("this is true")
else: # False თუ ყველაფერი მცდარი აღმოჩნდა
    print("this is not true")
print("end")

# ანუ მოქმედება შეწყდება მაშინ, როცა პირველივე სწორი პასუხი დაფიქსირდება;
# შეგვიძლია კიდე if-ში დავწეროთ კიდევ if


age = 41
if age >= 18:
    print("Regular price")
else:
    print("Discount")
    
# another example
for i in range (100):
    if i % 3 == 0 and i % 5 == 0:
        print("ვაშლი")
    else:
        print("Opa")