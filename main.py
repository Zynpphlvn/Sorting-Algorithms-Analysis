# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import createDataSets as cds
import InsertionSort as ins
import MergeSort as ms
import QuickSort as qs
import HeapSort as hs
import CountSort as cs
#import os 

sizes = [200, 400, 600, 800, 1000]
    
for x in sizes:
       cds.best(x)
       cds.average(x)
       cds.average2(x)
       cds.average3(x)
       cds.worst(x)
       cds.worstCaseOfMixed(x)    
       cds.sameValues(x)
       cds.sameValues2(x)
       cds.sameValues3(x)
       
print("For Insertion Sort graph please choose 1:")
print("For Merge Sort graph please choose 2:")
print("For Quick Sort graph please choose 3:")
print("For Heap Sort graph please choose 4:")
print("For Count Sort graph please choose 5:")
print("For a comparative graph of all algorithms, please choose 6:")

choose = input()
if choose == "1":
    ins.Insertion() 
    ins.generateCases()

elif choose == "2":
    ms.Merge()
    ms.generateCases()    
    
elif choose == "3":
    qs.Quick()
    qs.generateCases()  

elif choose == "4":
    hs.Heap()
    hs.generateCases()  
    
elif choose == "5":
    cs.Count()
    cs.generateCases()  
    cs.generateCasesforVariantK()
    
else:
    
    ins.Insertion()       
    ms.Merge()
    qs.Quick()
    hs.Heap()
    cs.Count()

    plt.grid()
    plt.title("") 
    plt.xlabel("Input Sizes")
    plt.ylabel("Times")
    
    plt.plot(sizes, cs.timesAve, '-r')
    plt.plot(sizes, ins.timesAve, '-b')
    plt.plot(sizes, ms.timesAve, '-y')
#    plt.plot(sizes, qs.timesAve, '-g')
    plt.plot(sizes, hs.timesAve)
    plt.legend(["count sort", "insertion sort", "merge sort", "quick sort", "heap sort"])
 
#to clear generated input files 
#for x in cds.fileNames:
#    os.remove(x)