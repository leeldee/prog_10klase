

names= ["anna", "oskars", "jenifer", "anna", 'miks'] 

ages = [17, 18, 18, 15, 20] 


print(f'{names[0]} is {ages[0]} years old.')
print(f'{names[1]} is {ages[1]} years old.')
print(f'{names[2]} is {ages[2]} years old.')
print(f'{names[3]} is {ages[3]} years old.')


names= ["anna", "oskars", "jenifer", "anna",'miks'] 
ages = [17, 18, 18, 15, 20] 
numbers = range(len(names))

for number in numbers:
    print(f'{names[number]} is {ages[number]} years old.')