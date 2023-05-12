print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? $'))
percentage_tip = float(
  input('What percentage tip would you like to give? 10, 12 or 15? '))
how_many_people = float(input('How many people to split the bill? '))

tip_amount = (percentage_tip / 100) * total_bill
total_amount = total_bill + tip_amount
amount_per_person = round(total_amount / how_many_people, 2)
print(f"Each person should pay: ${amount_per_person}")

