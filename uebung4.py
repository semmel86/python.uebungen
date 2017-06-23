'''
Created on 21.05.2017

@author: semmel
'''


import sys

def hanoi(n):
    '''
    @note: Rekursive loesung fuer die Tuerme von Hanoi
    @param n: Anzahl Scheiben auf dem Stapel
    '''
    
    # definiere die Tuerme/Stapel (Name, Liste als Stapel)
    stabA=("Anfangsstapel",[])
    stabH=("Hilfsstapel",[])
    stabZ=("Zielstapel",[])
    
     # befuelle Anfangsstapel
    for i in range(n,0,-1):
        stabA[1].append(i)
    
    print("Start 'Tuerme von Hanoi': ",stabA, stabH, stabZ)
   # rekursive Hilfsfunktion die je aufruf eine Scheibe von parameter 'stabA' auf 'stabZ' legt
    def hanoiRec(n, stabA, stabH, stabZ, rekursionszaehler):
        # Abbruchbedingung(n=0): alle Scheiben wurden von A->Z bewegt
        if n > 0:
            # Bewege zunaechst den Turm(n-1) von A->H (um die unterste Scheibe von A nach Z bewegen zu koennen)
            hanoiRec(n - 1, stabA, stabZ, stabH, rekursionszaehler+1)
            # Lege die grosse Scheibe von 'A' auf 'Z'
            if stabA[1]!=[]:
               # aktuelleScheibe = stabA[1].pop()
                print ("Lege",'['+str(stabA[1].pop() )+']',"von",stabA,"auf",stabZ)
                stabZ[1].append(n)
            # Bewege nun den kleinen Turm(n-1) von H nach Z
            hanoiRec(n - 1, stabH, stabA, stabZ, rekursionszaehler+1)
       # print("Rekursionstiefe",rekursionszaehler)
    
    # Aufruf der inneren rekursiven Hilfsfunktion  
    hanoiRec(n,stabA,stabH,stabZ,1)       
    print("Ende 'Tuerme von Hanoi': ",stabA, stabH, stabZ)
    
def recursiondepth(n):
    '''
    @note AUfgabe 1 ermittlet die Rekursionstiefe
    '''
    try:
        # rekursiver Aufruf mit zaehler
        # print(n)
        recursiondepth(n+1)
    except:
        # Ausnahme bedeutete keine rursion mehr moeglich
        # Desshalb ists der letzte erfolgreiche Aufruf=n-1
        print("Maximale Rekursionstiefe: ",n-1)
        #print(sys.getrecursionlimit())
       
        
recursiondepth(1)
hanoi(999) 
#sys.setrecursionlimit(100)
#recursiondepth(1)
# maximale Rekurionstiefe 995
# d.h. hanoi kann maximal bis hanoi(994) errechnet werden ueber die rekursive Methode, da fuer
# hanoi(n) insgesamt n+1 rekursionen noetig sind
# Beispiel um hanoi(3) zu loesen folgende Teilprobleme geloest werden:
# 1*hanoi(3)->2*Hanoi(2)->4*hanoi(1)->16*hanoi(0)
        