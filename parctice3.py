print("welcom to treasure island.")
print("your mission is to find the treasure")

while True:
    user_way = input("there is a forked road where do you go? Left? or Right? 1. Left 2.Right").strip()
    if user_way == "1":
        print("I fell into a trap. -GAME OVER-")
        exit()
    elif user_way == "2":
        print("we passed forked road")
        break
    else:
        print("you typed wrong inputs")



while True:
    user_way2 = input("There's a river in front. How do you want to cross? 1. swin 2. wait for boat").strip()

    if user_way2 == "1":
        print("I was eaten by a crocodile -GAME OVER- ")
        exit()
    elif user_way2 =="2":
        print("I took a boat!")
        break
    else:
        print("you typed wrong inputs")


while True:
    final_way = input("There's a 3gates. which gate do you into 1. red 2. green 3. blue").strip()
    
    if final_way == "1":
        print("there was trap only -GAME OVER-")
        exit()
    elif final_way == "2":
        print("there was only monster -GAME OVER-")
        exit()

    elif final_way == "3":
        print("I got the treasure!")
        break
        exit()
    else:
         print("you typed wrong inputs")
print("-happy End-")