from Partial_Pivoting import Matrix
import time
    
#test case 1 100x10
m = 100
n = 10
start = time.time()
testMatrix1 = Matrix(m, n)
for i in range (0, n):
    testMatrix1.swapColumn(testMatrix1.searchHighest(i),i)
    testMatrix1.rowReduce(i)
end = time.time()
print('Time for ' + str(m) + "x" + str(n) + " is " + str(end-start))

#test case 2 5x5
m = 5
n = 5
start = time.time()
testMatrix2 = Matrix(m, n)
for i in range (0, n):
    testMatrix2.swapColumn(testMatrix2.searchHighest(i),i)
    testMatrix2.rowReduce(i)
end = time.time()
print('Time for ' + str(m) + "x" + str(n) + " is " + str(end-start))

#test case 3 50x50
m = 50
n = 50
start = time.time()
testMatrix3 = Matrix(m, n)
for i in range (0, n):
    testMatrix3.swapColumn(testMatrix3.searchHighest(i),i)
    testMatrix3.rowReduce(i)
end = time.time()
print('Time for ' + str(m) + "x" + str(n) + " is " + str(end-start))

#test case 4 500x500
m = 500
n = 500
start = time.time()
testMatrix4 = Matrix(m, n)
for i in range (0, n):
    testMatrix4.swapColumn(testMatrix4.searchHighest(i),i)
    testMatrix4.rowReduce(i)
end = time.time()
print('Time for ' + str(m) + "x" + str(n) + " is " + str(end-start))
