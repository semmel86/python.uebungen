
'''
ALP2 - Uebung1
Created on 16.05.2017
@author: Sebastian Selmke
'''
def mod(a,b):
    '''
    Aufgabe 1 - Modulo
    Berechnet den Rest von div aequivalent zu %, man beachte das mod(n,0) als undefiniert definiert wird
    @param a: Dividend
    @param b: Divisor
    @return: Rest r der ganzzahligen Division a/b
    '''
    
    if(b==0):
        raise ZeroDivisionError('Division by Zero not defined!')
    suM=a+b
    # Fall 1: Wenn a und b groesser/gleich der Summe(a,b) 
    # dann gilt a und b sind Elemente der natuerlichen Zahlen einschliesslich 0
    if((suM>=a) & (suM>=b)):
        # Fuer Fall 1 kann die Division als Reduktion von a durch die Subtraktion abgebildet werden, solange (a >=b)
        while(a>=b):
            a-=b
    # Fall 2: Wenn a und b kleiner der Summe(a,b) 
    # dann gilt a und b sind Elemente der negtiven ganzen Zahlen
    elif((suM<a) & (suM<b)): 
     # Fuer Fall 2 kann die Division als Reduktion von a durch die Subtraktion abgebildet werden, solange (a <= b)
        while((a<=b)):
            a-=b
    # Fall 3 : Wenn Fall 1 und 2 nicht zutreffen 
    # dann ist entweder a positiv und b negativ oder umgekehrt
    # hier kann die Subtraktion durch Addition abgebildet werden
    else:
        # Fall 3 a:a ist negativ
        # solange addieren wie a<0 gilt
        if(a<b):
            while(a<0):
               a+=b
        # Fall 3 b:a ist positiv
         # solange addieren wie a>0 gilt
        else:
            while(a>0):
                a+=b
    return a





def collatz(n):
    '''
    Aufgabe 2 Collatz-Folge
    @param n : Ganzzahliger Wert N mit dem die Collatzfolge beginnen soll
    @return: Liste der Elemente der Collatzfolge von n
    '''    
    # Hilfsfunktion die den naechsten Collatz(n) zurueckgibt
    def simpleCollatz(n):
        # wenn n eine gerade Zahl ist, so ist Collatz(n) = n//2 
        if(n%2==0):
            return (n//2)
        # sonst 3*n+1
        else:
            return(3*n+1)
        
    # die Ergebnisliste
    result=[n]
    # eine lustige While Schleife die solange den Collatz berechnet bis n==1 gilt
    # sie ist deshalb so lustige, weil wuerde sie nicht terminieren, ein Beweisfall gefunden waere fuer den die Folge nicht endet 
    # oder nicht auf 1 endet
    while(n!=1):
        n=simpleCollatz(n)
        result.append(n)
    return result




'''
@note: Aufgabe 4
'''  
#
def printMatrix(matrix):
    '''
    @note: Gibt die gegebene Matrix auf der Standardausgabe aus, (kein Return Wert!)
    @param matrix: eine Matrix in Form einer geschachtelten Liste[[]] 
    ''' 
    # Ermittlung der Dimension der Matrix MxN
    n=len(matrix)
    m=len(matrix[0])
    line=""
    # durchlaufen der Matrix MxN und zufuegen der einzelnen Eintraege in die Ausgabezeile, Tabstop getrennt
    for i in range(n):
        for k in range(m):
           line= line + str(matrix[i][k])+"\t "
        # Zeilenweise Ausgabe
        print(line)
        # carriage Return -> zuruecksetzen der Zeile
        line=""
       
        
def readInMatrix(n,m):
    '''
    @note: Funktion zum Einlesen einer Matrix, da explizit gefordert in der AUfgabenstellung 
    wurde  input() innerhalb der Funktion definiert
    @return: Eingegebene Matrix
    ''' 
    if(n>0 & m>0):
        matrix=[]
        # iteriere ueber die Zeilen
        for i in range(n):
            line=[]
            # iteriere durch die Spalten
            for k in range(m):
                # einlesen des wertes und schreiben in die Matrix an Stelle [i],[k]
                print("Bitte Wert fuer ",i,k,"Eingeben:")
                line.append(input("value:"))
            matrix.append(line)
        return matrix

    else:
        raise ValueError('Dimensionen n und m muessen <=0 sein')
    
def transpondMatrix(matrix):
    '''
    @note: Funktion zum transponieren einer Matrix MxN zu NxM
     1  2  3       1  4  7
     4  5  6  =>   2  5  8
     7  8  9       3  6  9
    @param matrix: Ausgangsmatrix MxN
    @return: transponierte Matrix NxM
    ''' 
    # ermitteln der Dimension MxN
    n=len(matrix)
    m=len(matrix[0])
    newMatrix=[]
    # Einlesen der n-Zeilen der Ausgangsmatrix
    # die als n Spalten der Ergebnismatrix uebernommen werden
    for i in range(m):
        row=[]
        for k in range(n):
            row.append(matrix[k][i])
        newMatrix.append(row)
    # rueckgabe
    return newMatrix



#########################
# weekday aus Uebung 1
#########################
# control if a given Date (int,int,int) is a real Date,
# if so, returns true else false
def isDate(day,month,year):
    # first check Month between 0 and 12
    if(month<=12 or month>=0): 
        
        # define possible values for day depending on the specific month
        lengthOfMonthInDays=[31,28,31,30,31,31,30,31,30,31,30,31]
        # calculate if it is a leap year-> February days +1 
        # for performance, first check if month = February, if not the condition is not useful
        if(month==2 and year % 4 == 0 and not(year % 100 ==0 and year % 400!=0)):
            lengthOfMonthInDays[1]=29 #lang February
        # check if day into possible day range
        if(day>=1 and day <=lengthOfMonthInDays[month-1]):
            return True
    else:
        # date not valid
        return False

# returns the weekday as String if the given date is valid
def weekday(day,month,year):
    
    # check date
    if(isDate(day,month,year)):
        
        # calculate number of weekday
        
        y=year-(14-month)//12
        x=y+ (y//4) -(y//100) + (y//400)
        m= month + 12 *((14-month)//12) -2
        result2=(day+x+(31*m)//12)%7
        #print ("result2 :", result2)
        # convert weekday number to readable String 
        return getDayAsString(int(result2))
    else:
        return "The given Date is not valid"
    
# convert a given number(0-6) into a String representing a Weekday
# or Error Message if the number is out of range
def getDayAsString(day):
    if(day>=0 and day<=6):
        days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        return days[day-1]
    else:
        return "An Error occured while formatting Integer to the Day, Number "+str(day)+" out of range"

def calcWeekDays(startDay,startMonth,startYear,endDay,endMonth,endYear):
    '''
    @note: Aufgabe 3 Wochentage - Berechnet die Anzahl der einzelnen Tage zwischen dem gegebenen start und end Datum
    auf die ein 13ter Tag des Monats gefallen ist
    @param startDay 
    @param startMonth
    @param startYear
    @param endDay
    @param endMonth
    @param endYear
    @return: List Wochentage
    @requires: weekday
    
    ''' 
    #dictionary, dass die Wochentage und die einzelnen Zaehler beinhaltet
    count={"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}
    # Bedingung fuer die While-Schleife ist, dass das aktuelle Datum kleiner als das Enddatum sein soll, 
    # als aktuell wird das startdatum hochgezaehlt. Durch die Multiplikation Jahr *100000 und Monat *100 entsteht ein 
    # durch die Groesse vergleichbarer Zahlenwert der das genaue Datum wiederspiegelt
    while((startYear*10000+startMonth*100+startDay) < (endYear*10000+endMonth*100+endDay)):
        # zaelt den tag wenn nicht der aktuelle tag nicht kleiner als 13 ist
        if(startDay<=13):
            count[weekday(13,startMonth,startYear)]+=1
        # wenn er groesser ist wird er auf 13 gesetzt und fuer diesen Monat kein Tag gezahlt
        else:
            startDay=13
        # zahlt die Monate hoch bis 12
        if(startMonth<12):
            startMonth+=1
        # wenn 12 erreicht ist, wird das Jahr erhoeht
        else:
            startMonth=1
            startYear+=1
    # rueckgabe des Ergebnisses
    return count

# Test Aufgabe 3
# stelle heute fest als enddatum
import time
day=int(time.strftime("%d"))
month=int(time.strftime("%m"))
year=int(time.strftime("%Y"))
# gibt die Zahlung aller 13ten ab dem 1.1.1700 aus:
print(calcWeekDays(1,1,1700,day,month,year))



#Test Collatz:
n=int(input("Collatz(n) berechnen, bitte n eingeben:"))
result=collatz(n)
length=len(result)
# Ausgabe der Collatzfolge und ihrer Elemente
print(result,length)

#Test Mod
print("Test:",mod(12.2,5),12.2%5)
print("Test:",mod(-12.2,5),-12.2%5) 
print("Test:",mod(12.2,-5),12.2%-5) 
print("Test:",mod(-12.2,-5),-12.2%-5)  

print("Test:",mod(12,6),12%6)
print("Test:",mod(-12,6),-12%6) 
print("Test:",mod(12,-6),12%-6) 
print("Test:",mod(-12,-6),-12%-6)  
#print("Test:",mod(4,0),4%0)       
   # if(negative):result*=-1
   
   
 # m=Spalten, n=Zeilen
 #testMatrix
testMatrix=readInMatrix(3,1)
#print("test Printing")
#printMatrix(testMatrix)
#print("test transponding")
#printMatrix(transpondMatrix(testMatrix))