user_age = input("how old are you?")
price = 0
popcorn_price = 5000

if int(user_age) <= 12:
    price = 7000
elif int(user_age) <= 18:
    price = 9000
elif int(user_age) >= 45 and int(user_age) <= 55:
     price = 0
     print("Everthing is going to be ok. Have a free ride on us")

elif int(user_age) <= 64:
    price = 12000
elif int(user_age) >= 65:
        price = 8000

user_student_question = input("are you student? Y or N")
if user_student_question == "Y":
    price = price - 2000
else:
        int(user_age) >= 20
        print("Your ticket would be " + str(price))


user_popcorn = input("do you want to buy popcorn? Y or N")
if user_popcorn == "Y":
    print("your final price is " + str(price + popcorn_price))
else:
    print("your final price is " + str(price))


