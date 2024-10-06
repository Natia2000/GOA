# 1. შეეკითხეთ მომხმარებელს მისი წლოვანება და შეინახეთ ის age ცვლადში შემდეგ შეამოწმეთ არის თუ არა მისი წლოვანება 13 ზე დიდი [და] 19 ზე ნაკლები.
# age = input("enter your age: ") 
# print(int(age) > 13)
# print(int(age) < 19)


# 2. ნუგზარის გუშინ მათემატიკის საკონტროლო ქონდა. შეეკითხეთ მას საკონტროლოზე მიღებული ნიშანი(1-10) შემდეგ შექმენით ცვლადები:

# is_A: ამ ცვლადში შეინახეთ True თუ მისი ნიშანი მეტია ან ტოლი 9ზე.
# is_B: ამ ცვლადში შეინახეთ True თუ მისი ნიშანი მეტია ან ტოლი 8ზე [და] ნაკლებია 9ზე.
# is_C: ამ ცვლადში შეინახეთ True თუ მისი ნიშანი მეტია ან ტოლი 7ზე [და] ნაკლებია 8ზე.
# is_D: ამ ცვლადში შეინახეთ True თუ მისი ნიშანი მეტია ან ტოლი 6ზე [და] ნაკლებია 7ზე.
# is_F: ამ ცვლადში შეინახეთ True თუ მისი ნიშანი ნაკლებია 6ზე.
# საბოლოოდ კი დაპრინტეთ ყველა ცვლადი 

# score = input("enter your score from 1 to 10: ")
# A = (int(score) >= 9)
# B = (int(score) >= 8) and (int(score) < 9)
# C = (int(score) >= 7) and (int(score) < 8)
# D = (int(score) >= 6) and (int(score) < 7)
# F = (int(score) < 6)
# print(A)
# print(B)
# print(C)
# print(D)
# print(F)


3. # შექმენით 2 ცვლადი, სადაც ერთში შეინახავთ True-ს და მეორეში False-ს. შემდეგ კი დაპრინტეთ ლოგიკური ოპერატორების და ამ ცვლადების გამოყენებით ყველა შესაძლო განსხვავებული ვარიანტი.


# მაგალითად ჰაერღუმელში შუქის გამორთვა და ხმის ჩართვა ნიშნავს, რომ გათბობის სისტემაც გამორთულია. 
# light_off = False
# light_on = True
# sound_off = True
# sound_on = False
 
# print (light_off or sound_on)
# print (light_off and sound_on)
# print (light_on or sound_off)
# print (light_on and sound_off)


# 4. მომხმარებელს შემოატანინეთ 2 ინტეჯერ ტიპის მონაცემი, შეინახეთ ისინი ცვლადებში და საბოლოოდ შეადარეთ ეს 2 რიცხვი ყველა შედარების ოპერატორით (==, <, >, <=, >=, !=).

# num1 = input("enter the number of books purchased this month: ")
# num2 = input("enter the number of notebooks purchased this month:")
# print(num1 > num2)
# print(num1 < num2)
# print(num1 == num1)
# print(num1 != num2)
# print(num1 <= num2)
# print(num1 >= num2)


# 5. შექმენით a, b და c ცვლადები და მიანიჭეთ მათ ნებისმიერი მთელი რიცხვი. შექმენით ახალი 3 ცვლადი:
# is_a_greatest: ამ ცვლადში შეინახეთ True, თუ a არის უდიდესი ამ სამიდან.
# is_b_middle: ამ ცვლადში შეინახეთ True თუ b არის საშუალო მნიშვნელობა (არა უდიდესი ან უმცირესი).
# is_c_least: ამ ცვლადში შეინახეთ True, თუ c არის სამიდან უმცირესი.

# a = 10
# b = 15
# c = 20
# a_greatest = (a > b) and (a > c)
# b_middle = (a < b < c) or (c < b < a)
# c_least = (c < a) and (c < b)

# print(a_greatest)
# print(b_middle)
# print(c_least)


# #6. შექმენით ცვლადი სახელად score, რომელშიც შეინახავთ ნებისმიერ მთელ რიცხვს(0-100), შექმენით 4 ცვლადი:
# is_pass: ამ ცვლადში შეინახეთ True, თუ ქულა არის 50 ან მეტი.
# is_high_pass: ამ ცვლადში შეინახეთ True, თუ ქულა არის 75-დან 90-მდე (ექსკლუზიური).
# is_perfect: ამ ცვლადში შეინახეთ True, თუ ქულა უდრის 100-ს.
# is_failing: ამ ცვლადში შეინახეთ True, თუ ქულა 50-ზე ნაკლებია

# score = 50
# is_pass = (score >= 50)
# is_high_pass = (75 <= score < 90)
# is_perfect = (score == 100)
# is_failing = (score < 50)

# print(is_pass)
# print(is_high_pass)
# print(is_perfect)
# print(is_failing)

# 7. შექმენით ცვლადები P და Q, თითოეულს მიენიჭე True ან False. შემდეგ შექმენით ახალი ცვლადები:
# P_and_not_Q: ამ ცვლადში შეინახეთ True, თუ P არის True და Q არის False.
# not_P_and_Q: ამ ცვლადში შეინახეთ True, თუ P არის False და Q არის True.
# P_xor_Q: ამ ცვლადში შეინახეთ True, თუ ზუსტად ერთი P ან Q არის True თუ ორივე True-ა მაშინ ამ ცვლადში შეინახეთ False

P = True 
Q = False
P_and_not_Q = (P ==True) and (Q == False)
not_P_and_Q = (P == False) and (Q == True)
P_xor_Q = (P_and_not_Q or not_P_and_Q) or (P == False and Q == False)
print(P_and_not_Q)
print(not_P_and_Q)
print(P_xor_Q)
print(P_xor_Q)

