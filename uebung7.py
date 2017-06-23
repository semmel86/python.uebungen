from __future__ import with_statement
'''
Created on 22.05.2017

@author: semmel
'''
import random
import time
import threading
from threading import Thread
from time import clock
from threading import Lock


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
            
    print(list)       
            
# Test iteratives Quicksort
#list2 = [9,8,7,6,5,4,3,2,1]
#quickSortIterative(list2)
#print(list2)

#INSERTION SORT 1
def insertionSort(alist):
   for index in range(1,len(alist)):
     currentvalue = alist[index]
     position = index
     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1
     alist[position]=currentvalue
# insertionsort 2
def insertionsort(A):
  for pos in range(1, len(A)):
    i = pos
    while i>0 and A[i] < A[i-1]:
      A[i], A[i-1] = A[i-1], A[i]
      i -= 1
  #assert isSorted(A) to slow and not useful
  return A



#BUBBLE SORT     
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
#SELECTION SORT                
def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

#SHELL SORT       
def shellSort(alist):
    
    def gapInsertionSort(alist,start,gap):
        for i in range(start+gap,len(alist),gap):
    
            currentvalue = alist[i]
            position = i
    
            while position>=gap and alist[position-gap]>currentvalue:
                alist[position]=alist[position-gap]
                position = position-gap
    
            alist[position]=currentvalue
    
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)
      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

#MERGESORT
def mergeSort(alist):
   # print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            
from random import randint
def quicksort_rek(A):
  if len(A) > 1:
    pivot = A[randint(0, len(A)-1)]
    lower = [x for x in A if x < pivot]
    equal = [x for x in A if x == pivot]
    higher = [x for x in A if x > pivot]
    return quicksort_rek(lower) + equal + quicksort_rek(higher)
  else:
    return A     

#HEAPSORT
def heapsort(A):
  # Hilfsfunktionen
  def isLeaf(i):
    return i > H[0]//2
  def left(i):
    return 2*i
  def right(i):
    return 2*i+1
  def parent(i):
    return i//2
  def heapify(i):
    while not isLeaf(i):
      maxi = i
      if left(i) <= H[0] and H[left(i)] > H[maxi]:
        maxi = left(i)
      if right(i) <= H[0] and H[right(i)] > H[maxi]:
        maxi = right(i)
      H[i], H[maxi] = H[maxi], H[i] # vertauscht die Knoten
      if i == maxi: # es fand keine Vertauschung statt
        break
      else:
        i = maxi
  def makeMaxHeap():
    # erstellt einen MaxHeap aus der Liste
    for i in range(H[0]//2, 0, -1): # spart die Blaetter aus
      heapify(i)
  # sortiert die Liste
  H = [len(A)] + A
  makeMaxHeap()
  while H[0] > 0:
    H[H[0]], H[1] = H[1], H[H[0]] # vertauscht Knoten
    H[0] -= 1
    heapify(1)
  
  return H[1:]

def countingsort(A):
  if len(A) > 0:
    maxi = max(A)
    C = [0 for x in range(maxi+1)] # Hilfsarray
    # zaehlt die Vorkommen aller Werte in A
    for a in A:
      C[a] += 1
    # addiert alle Vorkommen auf
    for i in range(len(C)-1):
      C[i+1] += C[i]
    # befuellt Ergebnisliste
    B = list(range(len(A)))
    for a in reversed(A):
      C[a] -= 1
      B[C[a]] = a
    return B
  else:
    return []

def gleichverteilung(x,mini,maxi):
  if (mini != maxi):
    return (x-mini) / (maxi-mini)
  else:
    return 1
import math
def bucketsort(A,f=gleichverteilung):
  n = len(A)
  # Vorsortierung aller Elemente in Buckets
  buckets = [[] for i in range(n+1)]
  for e in A:
    buckets[math.floor(f(e,min(A),max(A))*n)].append(e)
  # Endsortierung durch Insertionsort
  res = []
  for b in buckets:
    res = res + insertionsort(b)
  return res

def binary_search(arr, low, high, key):
    if low == high:
        if arr[low] > key:
            return low
        else:
            return low + 1
    if low > high:
        return low
    mid = (low + high) // 2
    if arr[mid] < key:
        return binary_search(arr, mid + 1, high, key)
    elif arr[mid] > key:
        return binary_search(arr, low, mid - 1, key)
    else:
        return mid


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        ind = binary_search(arr, 0, i - 1, key)
        arr = arr[:ind] + [key] + arr[ind:i] + arr[i + 1:]
    return arr

def processSorting(name,sortAlgorithm,list,n):
        
        t0=time.process_time()
        sortAlgorithm(list)
        t1=time.process_time()
        print(name,"for",n,"elements takes",t1-t0/100,"sek")
        return True
   

    
#testSortings(1000,'asc',)
list1=[]
  
def buildList(n,sort='no'):
    for i in range(n):
        if(sort=='asc'):
            element=i
        elif(sort=='desc'):
            element=n-i
        else:
            element=random.randrange(0, 1000000, 1)
        
        list1.append(element)
    # sort lists and measure/print process times
n=10
listlength=[10,100,1000,2500,5000,7500,10000,15000,20000,30000]
listTypes=['no','asc','desc']
#for j in range(3):
#       type=listTypes[j]
#type="not sorted"
type="asc"
#type="desc"
print("Sorting",type,"list")
for i in range (10):
    n=listlength[i]
    buildList(n,type)
    #processSorting("Insertionsort",(lambda n:insertionsort(n)),list1,n)
    #processSorting("Insertionsort2",(lambda n:insertionSort(n)),list1,n)
    #processSorting("Quicksort",(lambda n:quickSortIterative(n)),list1,n)
    #processSorting("Quicksort2",(lambda n:quicksort_rek(n)),list1,n)
    #processSorting("Mergesort",(lambda n:mergeSort(n)),list1,n)
    #processSorting("Shellsort",(lambda n:shellSort(n)),list1,n)
    #processSorting("Selectionsort",(lambda n:selectionSort(n)),list1,n)
    #processSorting("Bubblesort",(lambda n:bubbleSort(n)),list1,n)
    #processSorting("Heapsort",(lambda n:heapsort(n)),list1,n)
    #processSorting("Bucketsort",(lambda n:bucketsort(n)),list1,n)
    #processSorting("Countingsort",(lambda n:countingsort(n)),list1,n)
    processSorting("InsertionSort BinarySearch",(lambda n:insertion_sort(n)),list1,n)
    #print(list1)
    #processSorting("PythonSort",(lambda n:n.sort),list1,n)
    #processSorting("PythonSort",(lambda n:sorted(n)),list1,n)


#testSortings(1000,'asc',)
