import turtle
from turtle import *

def Cementary( N, M ):
    kwartal = []
    for i in range (0,N):
        kwatera = []
        for j in range(0,M):
            kwatera.append('None')
        kwartal.append(kwatera)
    print("Cementary is ready :>")
    return kwartal

def dig(kwartal, *param):
    for i in param:
        kwartal[i[0]][i[1]]={}
    return kwartal

def bury(kwartal, row, col, *info):
    if kwartal[row][col] == 'None':
        print(row,", ", col, "nie wykopano dołu")
        return
    else:
        Dict=list(info)
        kwartal[row][col]=Dict.copy()
        return kwartal

def group_bury(kwartal, *param): #param: ( row, kol, *info)
        for i in param:
            bury(kwartal, i[0], i[1], i[2])

def star():
    for z in range(5):                    
            turtle.forward(30)
            turtle.right(144)
    return


def draw(kwartal, N, M):
    #turtle.speed(1)
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
            
        


sementary = Cementary(3,3) 
print(sementary)

dig(sementary, (0,0), (1,0));
print(sementary)

group_bury( sementary, (0,0, "rozgwiazda 1"), (1,0, "rozgwiazda 2") );
print(sementary)


draw(sementary, 3, 3)


