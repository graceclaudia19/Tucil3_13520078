from heapq import heappush, heappop

from numpy import mat
# A class for Priority Queue
class priorityQueue:
     
    # Constructor to initialize a
    # Priority Queue
    def __init__(self):
        self.heap = []
 
    # Inserts a new key 'k'
    def push(self, k):
        heappush(self.heap, k)
 
    # Method to remove minimum element
    # from Priority Queue
    def pop(self):
        return heappop(self.heap)
 
    # Method to know if the Queue is empty
    def isEmpty(self):
        if not self.heap:
            return True
        else:
            return False
    
class node:
     
    def __init__(self, parent, mat,
                 cost, level, move):
                      
        # Stores the parent node of the
        # current node helps in tracing
        # path when the answer is found
        self.parent = parent
 
        # Stores the matrix
        self.mat = mat
 
        # Storesthe number of misplaced tiles
        self.cost = cost
 
        # Stores the number of moves so far
        self.level =level

        self.move = move
        
    def __lt__(self, next):
        if (self.cost + self.level == next.cost + next.level):
            return self.cost < next.cost
        else:
            return self.cost + self.level < next.cost + next.level

