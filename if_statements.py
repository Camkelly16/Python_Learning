
# print("How is the weather outside. Hot, cold, or warm")
# weather_outside=input()
# if weather_outside.upper() == "HOT":
#     print("It's hot day")
#     print("Drink a mlot of water")
# elif weather_outside.upper() == "COLD":
#     print("Put on a jacket")
#     print("You might get sick")
# else:
#     print("It's a lovely day")

good_Credit = False 
house_Price = 1000000
if good_Credit:
    down_Payment = 0.1 * house_Price
    print(f"Your down payment is:  {down_Payment}")
else:
    good_Credit = False 
    down_Payment = 0.2 * house_Price
    print(f"Your down payment is: {down_Payment}")