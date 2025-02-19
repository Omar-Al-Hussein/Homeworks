#Implemented the Inputs to start
salary = input("Enter your salary for the month: $")
month = input("Enter the name of the month: ")
savings_percent = float(input("Enter the percentage for savings: "))
rent_percent = float(input("Enter the percentage for rent: "))
electricity_percent = float(input("Enter the percentage for electricity: "))

#calculation program for each of savings/rent/electricity

savings = (savings_percent / 100) * salary 
rent = (rent_percent / 100) * salary
electricity = (electricity_percent / 100) * salary

#total expenses Code

total_expenses = savings + rent + electricity

