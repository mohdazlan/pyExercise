print('''
             _                                ___                               ___  ___                                ___  ___   ___                    __  
  .'|=| `.   .'|\/|`.     .'|      .'|=|_.'   .'|=|`.     .'|        .'|=|_.' |   | |`.     .'|        .'|=|`.   `._|=|   |=|_.'   .'|=|`.     .'|=|  | 
.'  | | .' .'  |  |  `. .'  |    .'  |      .'  | |  `. .'  |      .'  |      |   | |  `. .'  |      .'  | |  `.      |   |      .'  | |  `. .'  | |  | 
|   |=|'.  |   |  |   | |   |    |   |      |   |=|   | |   |      |   |      |   | |   | |   |      |   |=|   |      |   |      |   | |   | |   |=|.'  
|   | |  | |   |  |   | |   |    `.  |  ___ |   | |   | |   |  ___ `.  |  ___ `.  | |   | |   |  ___ |   | |   |      `.  |      `.  | |  .' |   |  |`. 
|___|=|_.' |___|  |___| |___|      `.|=|_.' |___| |___| |___|=|_.'   `.|=|_.'   `.|=|___| |___|=|_.' |___| |___|        `.|        `.|=|.'   |___|  |_| 
      ''')
# list of health quotes {3}    health = [" xxxx ","ÿyyyy"","zzzzzz"]
# random.integer(1,3)
# def print health(random)

def calculateBMI(x,y):
    #BMI = berat / (tinggi * tinggi)
    BMI = x / (y * y)
    return BMI

berat = float(input("berat dlm kg :"))
tinggi = float(input("tinggi dalam m :"))

nilaiBMI = calculateBMI(berat,tinggi)
print(nilaiBMI)