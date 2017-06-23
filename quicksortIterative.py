
'''
Created on 10.06.2017

@author: Sebastian Selmke
'''


def quickSortIterative(list):
    '''
    iterative Loesung von Quicksort 
    @param list - zu sortierende Liste
    '''
    # partition Funktion entsprechend der Vorlesung
    # da diese bereits iterativ und effektiv innerhalb der Liste arbeitet
    def partition(list,low, high):
            pivot=list[low]
            i=low
            for j in range(low + 1, high +1):
                if(list[j]<pivot):
                    i=i+1
                    list[i],list[j]=list[j],list[i]
            list[i],list[low]=list[low],list[i]
            return i
    
    # Fuer die iterative Lsg wird eine zusaetzliche Liste als Stack benutzt der 
    # die positionen der Partitionen beinhaltet
    # initialisiert mit (low,high)== (0,len(list-1))
    stack=[(0,len(list)-1)]
    # sortiere so lange, wie zu sortierende Partitionen auf dem stack liegen
    while len(stack)!=0:
        # nimm die obersten Elemente vom Stack
        # die die Partition definieren die mittels partition als naechstes partitioniert und um 
        # das Pivot Element sortiert werden soll
        part=stack.pop()
        low = part[0]
        high = part[1]
        
        # fuehre partition aus und ermittle das akuelle pivot element
        pivot = partition( list, low, high )
        #print("pivot:",pivot,"low:",low,"high:",high,"list:",list,"stack:",stack)
            
        # wenn es elemente links des pivot elements gibt, dann packe partition 
        # auf den stack die zwischen pivot und low liegt
        if pivot-1 > low:
            stack.append((low,pivot-1))
        # wenn es elemente rechts des pivot elements gibt, dann packe partition 
        # auf den stack die zwischen pivot und rechts liegt
        if pivot+1 < high:
            stack.append((pivot+1,high))
            
   # print(list)       
            
# Test iteratives Quicksort
list2 = [9,8,7,6,5,4,3,2,1]
print("unsortiert:",list2)
quickSortIterative(list2)
print("sortiert",list2)



timsort(list)
# run ist ein Teil der liste, der mit einem sortierten bereich beginnt
# dabei muss dieser bereich strend absteigend oder aufsteigend sortiert sein
 runs=splitIntoRuns(list)
 
# sortiere zunächst die runs
for i in range(len(runs))
# wenn der run absteigen sortier ist,
# reverse(sortierten bereich)
    if runs[i] == descendingSorted:
        reverse[runs[i]]
    # nun sollte der run entweder sortiert sein,
    # oder der erste teil des runs ist sortiert und die
    # hintersten elemente nicht, damit kann sehr effektiv aus dem 
    # unsortierten bereich über insertionsort in den Sortierten Bereich nachsortiert werden 
    if !(runs[i]isSorted())
    insertionsort(runs[i])

# nun sind alle runs in sich sortiert und müssen noch zusammengefügt werden
# die mergesort implementierung für runs
# merged dabei immer kleine runs zu größen um unnötiges
# nachsortieren von mehrfach vorkommenden elementen zu vermeiden
improvedMergesort(runs)