# -*- coding: utf-8 -*-
import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time

values = []  
times = [] 
counts = []  
timesAve = np.zeros(5)
  
def Insertion():
    
    
    def insertionSort(alist):
       count = 1
       for index in range(1,len(alist)):
         currentvalue = alist[index]
         position = index
         x = 0
         while position>0 and alist[position-1]>currentvalue:
             alist[position]=alist[position-1]
             position = position-1
             count += 1
             x = 1
          
         if(x == 0):    #if count incremented in while loop then will not incremented count again
             count += 1
         
         alist[position]=currentvalue
         
       counts.append(count)  
           
    for f in cds.fileNames:
        values.clear() 
        start = time.time()
        with open(f, "r") as reader:
            for value in reader.readlines():
                values.append(int(value))         
        
        insertionSort(values)
        end = time.time()
        times.append(end - start)
        
    cds.generateAverageValues(times, timesAve)

def generateCases():
            global counts
            arrBest = [] 
            arrAve = []
            arrWorst = []
            
            #best case
            for i in range(len(counts)):
                if(i % 9 == 0):
                    arrBest.append(counts[i])
                          
            #worst case
            for i in range(len(counts)):
                if(i % 9 == 4):
                    arrWorst.append(counts[i])
                    
            #average case
            for i in range(len(counts)):
                if(i % 9 == 1 or i % 9 == 2 or i % 9 == 3):
                    arrAve.append(counts[i])
                
            arrAve2 = []    
            for i in range(len(arrAve)):
                x= (arrAve[i] + arrAve[i+1] + arrAve[i+2])/3
                i+=2
                if(len(arrAve2) >= len(arrAve)/3 ):
                    break
                arrAve2.append(x)
                x=0

            sizes = [200, 400, 600, 800, 1000]

            plt.plot(sizes, arrBest, '-ro')
            plt.plot(sizes, arrAve2, '-bo')
            plt.plot(sizes, arrWorst, '-go')
            plt.legend(["Best Case", "Average Case", "Worst Case"])
            plt.grid()
            plt.xlabel("Sizes")
            plt.ylabel("Counts")
    
    