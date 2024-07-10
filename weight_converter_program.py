# #Ask the user for his weight, allow them to enter it
# #Ask if the weight is in lbs or Kg, allow them to pick the metric
# #print the conversion of the opposite weight metric they chose. 

weight = input("Weight: ")

weight_metric=input("(L)bs or (K)g: ")

if weight_metric.upper() == "L":
    weight_conver = int(weight) * 0.453592
    print(f"You are {weight_conver} kilos")
else:
    weight_conver = int(weight) * 2.20462
    print(f"You are {weight_conver} in pounds")

