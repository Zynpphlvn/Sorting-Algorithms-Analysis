# -*- coding: utf-8 -*-
import createDataSets as cds
import matplotlib.pyplot as plt
import numpy as np
import time

values = []  
times = [] 
counts = []  
timesAve = np.zeros(5)
count = 0

def Quick():
        
        def quickSort(alist):
           quickSortHelper(alist,0,len(alist)-1)
        
        def quickSortHelper(alist,first,last):
           if first<last:
        
               splitpoint = partition(alist,first,last)
        
               quickSortHelper(alist,first,splitpoint-1)
               quickSortHelper(alist,splitpoint+1,last)
        
        def partition(alist,first,last):
           global count
           pivotvalue = alist[first]
        
           leftmark = first+1
           rightmark = last
        
           done = False
           while not done:
        
               while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                   leftmark = leftmark + 1
                   count += 1
        
               while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                   rightmark = rightmark -1
                   count += 1
        
               if rightmark < leftmark:
                   done = True
               else:
                   temp = alist[leftmark]
                   alist[leftmark] = alist[rightmark]
                   alist[rightmark] = temp
        
           temp = alist[first]
           alist[first] = alist[rightmark]
           alist[rightmark] = temp
        
           return rightmark
        a=0
        for f in cds.fileNames:
           a+=1
           values.clear()     
           start = time.time()
           with open(f, "r") as reader:
               for value in reader.readlines():
                   values.append(int(value)) 
                
           global count
           count=0
           quickSort(values)
           counts.append(count)  
           end = time.time() 
                               
           times.append(end - start)
           
        cds.generateAverageValues(times, timesAve)
        
def generateCases():
        
            arrBest = [] 
            arrAve = []
            arrWorst = []
            
            #best case
            for i in range(len(counts)):
                if(i % 9 == 2):
                    arrBest.append(counts[i])
                          
            #worst case
            for i in range(len(counts)):
                if(i % 9 == 0):
                    arrWorst.append(counts[i])
                    
            #average case
            for i in range(len(counts)):
                if(i % 9 == 1 or i % 9 == 3 or i % 9 == 5):
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
            