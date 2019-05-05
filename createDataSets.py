import random

fileNames= []

def best(size):
       #values are increasing 
       #best of insertion and merge
       #worst of quicksort
       name = "best" + str(size) + ".txt"
       fileNames.append(name)
       file = open(name, "a")
       for i in range(size):
           file.write(str(i))
           file.write("\n")
            
def average(size):
        #txt contains random numbers
        name = "average1" + str(size) + ".txt"
        fileNames.append(name)
        file = open(name, "a")
        for x in range(size):
            file.write(str(random.randint(1,size)) + "\n")
            
def average2(size):
        #txt contains random numbers
        name = "average2" + str(size) + ".txt"
        fileNames.append(name)
        file = open(name, "a")
        for x in range(size):
            file.write(str(random.randint(1,size)) + "\n")

def average3(size):
        #txt contains random numbers
        name = "average3" + str(size) + ".txt"
        fileNames.append(name)
        file = open(name, "a")
        for x in range(size):
            file.write(str(random.randint(1,size)) + "\n")
            
def worst(size):
        #values are decreasing
        #worst of insertion
        #best of merge
        name = "worst" + str(size) + ".txt"
        fileNames.append(name)
        file = open(name, "a")
        for i in range(size):
            file.write(str(size - i) + "\n")
            
def worstCaseOfMixed(size):
        # txt contains: 100,0, 99,1,98,2,97,3,96,4 … for merge sort worst case    
        name = "worstMixed" + str(size) + ".txt"
        fileNames.append(name)
        file = open(name, "a")
        y = size
        for x in range(int(size/2)):
            file.write(str(x) + "\n")
            file.write(str(y) + "\n")
            y = y - 1
            
def sameValues(size):
        #txt contains one unique value
        #best case of heapsort
        name = "sameValues1" + str(size) + ".txt"
        fileNames.append(name)
        file = open(name, "a")
        for x in range(size):
            file.write("10\n")
            
def sameValues2(size):
        #txt contains one unique value
        #best case of heapsort
        name = "sameValues2" + str(size) + ".txt"
        fileNames.append(name)
        file = open(name, "a")
        for x in range(size):
            file.write("500\n")
            
def sameValues3(size):
        #txt contains one unique value
        #best case of heapsort
        name = "sameValues3" + str(size) + ".txt"
        fileNames.append(name)
        file = open(name, "a")
        for x in range(size):
            file.write("1000\n")
            
def generateAverageValues(arr, arr2):
        
    for i in range(len(arr)):
        x = int(i/9)
        y=arr[i]
        arr2[x] += y
        
    for i in range(5):        
        arr2[i] /= 9

    return arr2
        
        
            
            
            
            
        
        

