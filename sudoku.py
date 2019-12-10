#10.12.2019
#-------------sudoku


#metoda set - ustawianie pol
#metoda - wyznaczanie wlasciwosci kolumn, wierszy

#class block:
   # tab = [3*[None]]*3
from math import *

class sudoku:    
    def create(self, bottom=True):                  #bottom->false obiekty typu sudoku
        if bottom==True:                            #bottom true -> None
            self.blok = [[None for x in range(3)] for i in range(3) ]
        if bottom==False:
            self.plansza = [[ sudoku() for x in range (3) ] for i in range (3)]
            for zm in self.plansza:
                for z in zm: 
                    z.create(True)
    
    def show(self):
        for i in self.plansza:
            for j in i:
                print(j.blok)
                

    def set(self, w, k,x):
        if ( self.check(w, k, x) ):
            i = floor(w/3)
            j = floor(k/3)
            self.plansza[i][j].blok[w-i*3][k-j*3] = x;
        else:
            print( " Wbrew zasadom sudoku debilu!" )

    def check(self, w, k, x):
        i = floor(w/3)
        j = floor(k/3)
        #sprawdzenie bloku: 
        for z in self.plansza[i][j].blok:
            for y in z:
                if y == x:
                    return False # => nie mozna wsadzic, wbrew sudoku xD
                #print (x, y, check)
        return True
            


A = sudoku()
A.create(False)
A.show()




            #self.plansza = [[ self.create() for x in range (3) ] for i in range (3)]   
  

    #def getelem( self, w, k):


    #metody ktore maja weryfikowac czy w tym polu moze byc wartosc
    
