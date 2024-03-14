def greeting(name, day):
    print("Hello " + name  +" This day is " + day)

name = input("Your name")
today = input("Wheter today is good or bad?")
greeting(name,today)

def complexCal(x,y,z):
    print(x * y * z)

x = 3
y = 2
z = 6
complexCal(x,y,z)

def calculateBMI(x,y):
    #BMI = berat / (tinggi * tinggi)
    BMI = x / (y * y)
    return BMI

berat = input("berat dlm kg")
tinggi = input("tinggi dalam m")

nilaiBMI = calculateBMI(berat,tinggi)
print(nilaiBMI)
