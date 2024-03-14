import random
#random is a library

#my_name = input("My name is?")
#my_temp = input("What is the temperature?")
#kelvin =  float(my_temp) + 273.15
#print("hi there " + my_name + "the temp is" + str(my_temp) + "which is in kelvin " + str(kelvin) )

acronyms = ['LOL', 'IDK', 'SMH', 'TBH']
for x in acronyms:
    print(x)

r1 = random.random()  
print(r1)

r2 = random.choice([1,2,3,4,5])  
print(r2)

r3 = random.randint(1,1000)  
print(r3)

total = 0
expense = []

for i in range(5):
    expense.append(float((input("enter a number"))))

total = sum(expense)
print("total ", total)

loot = ""
roll = random.randint(1,3)
print(roll)
if roll == 1:
    loot="emas"