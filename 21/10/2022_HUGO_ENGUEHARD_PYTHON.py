montuple = ("Tomate", "Oignon", "Semoule", "Miel", "Sucre")

def exo1():
    (a, b ,*c) = montuple
    # a, b ,*c = montuple # On peut aussi l'écrire comme ça

    # print(c)

    for i in range(len(montuple)):
        print(montuple[i])
        print(i)

# exo1()

def exo2():
    index = 0
    while(index < len(montuple)):
        print(index)
        print(montuple[index])
        index += 1
        
# exo2()

def exo3():
    for i in range(101):
        if(i%2 == 0 and i!=0):
            print(i)

    # x=2
    # while x<101:
    #     print(x)
    #     x += 2

# exo3()

import random

def exo4():
    listePossibilite = [1,2,3,4,5,6]
    for i in range(6):
        print("Lancé n°", i+1, ":", random.choice(listePossibilite))
        
# exo4()



def exo5():
    listeLances = []
    nombreTotalLance = input("Combien de dés voulez-vous lancer : ")
    index=0
    
    while(index<(int)(nombreTotalLance)):
        listeLances.append(random.choice([1,2,3,4,5,6]))
        index += 1
        
    totalDesLances = 0
    for i in range(len(listeLances)):
        totalDesLances += listeLances[i]
    
    print("Moyenne des lancés =", totalDesLances/len(listeLances))
    
    
# exo5()

import re

def exo6():
    myString = "How You Doing ?"
    print(len(re.findall("O", myString.upper())))

exo6()