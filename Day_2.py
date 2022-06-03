print("Welcome to the bill calculator!")
total=int(input('What was the bill?'))
tip=int(input('10, 12 or 15 % tip?'))
people=int(input('How many people?'))
tip_conversed=tip/100*total+total
result=tip_conversed/people
print(f'You should pay: {result}')
