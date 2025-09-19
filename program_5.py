# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.
dog_cost = 0
dog_type_input = int(input("Do you want a (1) hot dog or (2) chili dog:"))
if dog_type_input == 1:
    dog_cost = (float(3.50))
elif dog_type_input == 2:
    dog_cost = (float(4.50))
else:
    print("What kind of hot dog is that?! I quit working retail!")
    exit()

#figure out toppings
dog_topping1 = 0
dog_topping2 = 0
dog_topping3 = 0
dog_topping1_input = input("Do you want cheese ( Y or N )?")
if dog_topping1_input == "Y":
    dog_topping1 = float(0.50)

dog_topping2_input = input("Do you want peppers ( Y or N )?")
if dog_topping2_input == "Y":
    dog_topping2 = float(0.75)

dog_topping3_input = (input("Do you want grilled onions ( Y or N )?"))
if dog_topping3_input == "Y":
    dog_topping3 = float(1.00)

subtotal = dog_cost + dog_topping1 + dog_topping2 + dog_topping3
tax = subtotal * float(0.07)
total = subtotal + tax
print("Hot Dog with Toppings: $", round(subtotal,2))
print("Tax: $", round(tax,2))
print("Total: $", round(total,2))