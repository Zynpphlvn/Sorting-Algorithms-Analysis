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

def Heap():
    # To heapify subtree rooted at index i. 
    # n is size of heap 
    def heapify(arr, n, i): 
        global count
        largest = i  # Initialize largest as root 
        l = 2 * i + 1     # left = 2*i + 1 
        r = 2 * i + 2     # right = 2*i + 2 
        count += 1       
        # See if left child of root exists and is 
        # greater than root 
        if l < n and arr[i] < arr[l]: 
            largest = l 
  
      
        # See if right child of root exists and is 
        # greater than root 
        if r < n and arr[largest] < arr[r]: 
            largest = r 
        
        # Change root, if needed 
        if largest != i: 
            arr[i],arr[largest] = arr[largest],arr[i]  # swap 
            # Heapify the root. 
            heapify(arr, n, largest) 
      
    # The main function to sort an array of given size 
    def heapSort(arr): 
        global count
        n = len(arr) 
        
        # Build a maxheap. 
        for i in range(n, -1, -1): 
            heapify(arr, n, i) 
      
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i]   # swap 
            heapify(arr, i, 0) 
    
    for f in cds.fileNames:
        values.clear() 
        start = time.time()
        with open(f, "r") as reader:
            for value in reader.readlines():
                values.append(int(value)) 
  
        global count
        count=0
        heapSort(values)
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
                if(i % 9 == 4):
                    arrBest.append(counts[i])
                          
            #worst case
            for i in range(len(counts)):
                if(i % 9 == 0):
                    arrWorst.append(counts[i])
                    
            #average case
            for i in range(len(counts)):
                if(i % 9 == 1 or i % 9 == 2 ):
                    arrAve.append(counts[i])
                
            arrAve2 = []    
            for i in range(len(arrAve)):
                x= (arrAve[i] + arrAve[i+1]) / 2
                i+=1
                if(len(arrAve2) >= len(arrAve)/2 ):
                    break
                arrAve2.append(x)
                x=0
                
            sizes = [200, 400, 600, 800, 1000]
            
            plt.plot(sizes, arrAve2, '-bo')
            plt.plot(sizes, arrBest, '-ro')
            plt.plot(sizes, arrWorst, '-go')
            plt.legend(["Best Case", "Average Case", "Worst Case"])
            plt.grid()
            plt.xlabel("Sizes")
            plt.ylabel("Counts")
    
