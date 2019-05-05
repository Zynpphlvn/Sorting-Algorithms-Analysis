# -*- coding: utf-8 -*-
import createDataSets as cds
import matplotlib.pyplot as plt
import time
import numpy as np

values = [] 
times = []
counts = []  
timesAve = np.zeros(5)
count = 0

def Count():
    def countSort(array, maxValue=None):
      global count    
      maxValue= max(array)      
      buckets = [0] * (maxValue + 1)
      sortedIndex = 0

      for i in range(0, len(array)):
        buckets[array[i]] += 1
        count += 1
      
      for i in range(0, len(buckets)):
        if(buckets[i] > 0):  
            while (buckets[i] > 0):
              array[sortedIndex] = i
              sortedIndex += 1
              buckets[i] -= 1
              count += 1
            count+=1
              
        else :
              count += 1
              
      return array


    for f in cds.fileNames:
        values.clear() 
        start = time.time()
        with open(f, "r") as reader:
            for value in reader.readlines():
                values.append(int(value)) 
        
        global count
        count = 0
        countSort(values)
        counts.append(count)
        end = time.time()
        times.append(end - start)
        
    cds.generateAverageValues(times, timesAve)

def generateCases():
    # K is fixed, n is variant
    # K is max num in txt
    
            arrBest = [] 
            arrAve = []
            arrWorst = []
            
            #best case
            for i in range(len(counts)):
                if(i % 9 == 0):
                    arrBest.append(counts[i])
                          
            #worst case
            for i in range(len(counts)):
                if(i % 9 == 1):
                    arrWorst.append(counts[i])
                    
            #average case
            for i in range(len(counts)):
                if( i % 9 == 4 ):
                    arrAve.append(counts[i])
                     
            sizes = [200, 400, 600, 800, 1000]
            
            plt.plot(sizes, arrBest, '-ro')
            plt.plot(sizes, arrAve, '-bo')
            plt.plot(sizes, arrWorst, '-go')
            plt.legend(["Best Case", "Worst Case", "Average Case"])
            plt.grid()
            plt.xlabel("Sizes")
            plt.ylabel("Counts")
            plt.clf()
        
        
def generateCasesforVariantK():
    # n is fixed, k is variant
    # k is max num in txt
           
            performance = []
            
            #best case
            performance.append(counts[6])  
                    
            #average case
            performance.append(counts[7]) 
            
            #worst case
            performance.append(counts[8]) 
            
            k = [10, 500, 1000]
            y_pos = np.arange(len(k))
            
            plt.bar(y_pos, performance, align='center', alpha=0.5)
            plt.xticks(y_pos, k)
            plt.xlabel('Max Values')
            plt.ylabel('Counts')
            
            plt.show()
                       