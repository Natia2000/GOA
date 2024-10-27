# 3) 
# შევქმნათ ცვლადი, რომელიც დაიანგარიშებს საბოლოო შედეგს result
# 5-ჯერ შევეკითხოთ  for ლუპის გამოყენებით, მომხარებელს სხვადასხვა ციფრებბი
# შევკრიბავთ += გმაოყენებთ და print  -ში 
# გამოვითვლით საშუალო არითმეტიკულს ამ ციფებისას <3 

# numbers = input("enter 5 numbers: ")


sum_of_numbers = 0
for i in range(5):
    num = int(input("enter number: "))
    sum_of_numbers += num
print(sum_of_numbers)
    