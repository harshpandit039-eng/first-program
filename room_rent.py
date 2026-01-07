#monthly expenses for room renter

rent=int(input("Enter rent here: "))
food_cost=int(input("Enter food_cost here: "))
Electricity_expense=int(input("Enter electricity_expense here: "))
charges_per_unit=int(input("Enter charges_per_unit here: "))
person=int(input("Enter person living flat/room: "))
total_bill=Electricity_expense*charges_per_unit
output=(rent+food_cost+total_bill)//person
print(output)

