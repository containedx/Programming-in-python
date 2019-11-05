#programik tworzacy cmentarz XD

import turtle
from turtle import *

def Cementary( N, M ): #funkcja wypelniajaca cmentarz pustymi kwaterami
    kwartal = []
    for i in range (0,N):
        kwatera = []
        for j in range(0,M):
            kwatera.append('None')
        kwartal.append(kwatera)
    print("Cementary is ready :>")
    return kwartal

def dig(kwartal, *param): #kopanie dolu == wpisanie do kwatery slownika na dane
    for i in param:
        kwartal[i[0]][i[1]]={}
    return kwartal

def bury(kwartal, row, col, *info): #pochowek indywidualny, lokalizacja, informacje o szczatkach
    if kwartal[row][col] != {}:  #jesli nie wykopano dolu to ninu
        print(row,", ", col, "nie wykopano dołu lub ktos pogrzebany!")
        return
    else:                   #jak wszystko okejo to wsadzamy :)
        Dict=list(info)
        kwartal[row][col]=Dict.copy()
        return kwartal

def group_bury(kwartal, *param): #param: ( row, kol, *info)  #pochowek zbiorowy xdd
        for i in param:
            bury(kwartal, i[0], i[1], i[2])

def star():                 #rysowanie gwiazdki 
    for z in range(5):                    
            turtle.forward(30)
            turtle.right(144)
    return


def draw(kwartal, N, M):   #wizualizacja cmentarza, rysujemy kwatery puste i pelne
    turtle.speed(6)
    for i in range(0,N):
        for j in range(0,M):
            
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            if kwartal[i][j] != 'None':
                turtle.left(135)
                turtle.penup()
                turtle.forward(20)
                turtle.pendown()
                star()
                turtle.right(180)
                turtle.penup()
                turtle.forward(20)
                turtle.pendown()
                turtle.left(45)
                
                            
              
          

        turtle.left(180)
        turtle.forward(M*50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
            
        

#MAIN czy cos tam
sementary = Cementary(5,5)    
print(sementary)

dig(sementary, (0,0), (1,0), (2,1))
print(sementary)

group_bury( sementary, (0,0, "rozgwiazda 1"), (1,0, "rozgwiazda 2"), (2, 1, "ametyst" ))
print(sementary)







##### update 5.11
# nowa funkcja grzebiaca umarlych <3

def procedure( cementary, x, y, *, arms, **args ): #cmentarz, ,pozycja, liczba ramion, **pozostałe argumenty- słownik
    print("******\nramiona: ", arms, "arg: ", args, "\n********")
    if cementary[x][y] != {} :
        return
    else:        
        cementary[x][y]['arms'] = arms
        cementary[x][y].update(args)   #dopisanie wartosci do slownika




dig(sementary, (3,3))
procedure(sementary, 3, 3, arms=5, arg="arg1", arg2="arg2")  # '*' w def parametrow wymusza uzycie arms='...' :)

print(sementary)

draw(sementary, 3, 3)







