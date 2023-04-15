import numpy as np

class Matrix():
    def __init__(self, m, n):
        self.m = m
        self.n = n
        # Create a matrix 100x10
        randomArray = np.random.rand(self.m, self.n)
        #Transpose matrix to make column vectors
        self.exampleMatrix = randomArray.transpose()

    #return index of largest magnitude number in column
    def searchHighest(self, pivotCol):
        index = pivotCol
        highest = self.exampleMatrix[pivotCol, pivotCol]
        #For pivotCol, search for the highest value in the array
        for i in range(pivotCol, self.m):
            if self.exampleMatrix[pivotCol, i] > highest:
                highest = self.exampleMatrix[pivotCol, i]
                index = i
        return index
    
    #Swap the places of 2 rows
    def swapColumn(self, x, pivotCol):
        #Takes 2 column vectors at postion x and pivtoCol and sets them to the same in reverse order
        self.exampleMatrix[:,[x,pivotCol]] = self.exampleMatrix[:,[pivotCol,x]]
        
    #reduce all column values to 0 other than the pivot
    def rowReduce (self, pivotCol):
         highestMagnitude = self.exampleMatrix[pivotCol, pivotCol]
         #Loops for each entry in exampleMatrix[pivotCol]
         for j in range(pivotCol+1,self.m):
             nextNumber = self.exampleMatrix[pivotCol, j]
             scalar =-(nextNumber)/highestMagnitude
             #Apply the scalar and addition for each column
             for i in range (0,self.n):
                  self.exampleMatrix[i, j] = self.exampleMatrix[i, pivotCol] * scalar + self.exampleMatrix[i, j]
    
    #Transpose of the current matrix state

         
     
         
    #Return specific element in exampleMatrix
    def getElement(self, x, y):
        return self.exampleMatrix[x,y]
    #Return exampleMatrix in its original form 
    def toString(self):
        return np.matrix(self.exampleMatrix.transpose())







