import time
import functions

file = input("Enter file to read: ")
with open ('../test/'+file, 'r') as f:
    m = []
    for line in f.readlines():
        m.append( [ int (x) for x in line.split(' ') ] )
    if(not functions.reachableGoal(m)):
        print("Tidak dapat diselesaikan!")
    else:
        print("Dapat diselesaikan!")
        rootCost = functions.cost(m)
        if rootCost==0:
            print("PUZZLE ALREADY SOLVED!")
        else:
            start_time = time.time()
            functions.BnB(m)
            print("Program executed in %s seconds" % round((time.time() - start_time),5))

