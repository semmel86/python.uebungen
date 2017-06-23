'''
Created on 22.05.2017

@author: semmel
'''

def hanoiIt(n):
    stabA=[]
    stabH=[]
    stabZ=[]

  # befuelle Anfangsstapel
    for i in range(n,0,-1):
        stabA.append(i)
        
    def printStapel():
        print("A:",stabA,"H:",stabH,"Z",stabZ)
    
       
   
  #  print("Anfang: ",stabA)
    
   # print(stabA,stabH,stabA!=[0],stabH!=[n+1])
    while((stabA!=[] or stabH!=[])):
        #print("true")
        if(stabA!=[] and(stabH==[] or stabA[(len(stabA)-1)]<stabH[(len(stabH)-1)])):
            #A->H
            stabH.append(stabA.pop())
            printStapel()
            
        if(stabH!=[] and(stabZ==[] or stabZ[(len(stabZ)-1)]>stabH[(len(stabH)-1)])):
            #H->Z
            stabZ.append(stabH.pop())
            printStapel()
            
        if(stabZ!=[] and(stabA==[] or stabA[(len(stabA)-1)]>stabZ[(len(stabZ)-1)])):
            #Z->A
            stabA.append(stabZ.pop())
            printStapel()
            
hanoiIt(8)