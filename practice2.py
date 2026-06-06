print("Welcom to Python Pizza Deliveries!!")
size_price = 0
size = input("what size pizza do you want? S, M, L : ")
if size == "S":
    size = size_price + 15
elif size == "M":
    size = size_price + 20
elif size == "L":
    size = size_price + 25
else:
    print("You typed wrong inputs.")

pepperoni_price = 0
pepperoni_value = input("Do you want Pepperoni on your pizza? Y or N ")
if pepperoni_value == "Y":
    pepperoni_value = pepperoni_price + 2
if pepperoni_value == "N":
    pepperoni_value = pepperoni_price + 0



extra_cheese_price = 0
extra_cheese = input("Do you want extra cheese? Y or N ")
if extra_cheese == "Y":
    extra_cheese = extra_cheese_price + 1
if extra_cheese == "N":
    extra_cheese = extra_cheese_price + 0


print("your final price is " + str(size + pepperoni_value + extra_cheese))