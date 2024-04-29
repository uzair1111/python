meal_price = input("what is the meal price?")
tip = input("what is the tip %?")

total_tip = int(meal_price) * int(tip)/100

print("you will tip " + str(total_tip) + "$ for your meal." )
