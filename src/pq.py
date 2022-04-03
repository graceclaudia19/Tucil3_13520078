from heapq import heappush, heappop


# kelas untuk priority queue
class priorityQueue:
    #konstruktor
    def __init__(self):
        self.heap = []
 
    # push pada priority queue
    def push(self, k):
        heappush(self.heap, k)
 
    # pop pada priority queue
    def pop(self):
        return heappop(self.heap)
 
    # mengecek apakah priority queue empty atau tidak
    def isEmpty(self):
        if not self.heap:
            return True
        else:
            return False
    
class node:
    # konstruktor
    def __init__(self, parent, mat,
                 cost, level, move):
                      
        #m enyimpan parent node
        self.parent = parent
 
        # menyimpan matrix
        self.mat = mat
 
        # minyimpan cost (ubin yang tidak sesuai tempatnya)
        self.cost = cost
 
        # menyimpan depth/level/kedalaman
        self.level =level

        # menyimoan move
        self.move = move
        
    # pemanfaatan loading 
    def __lt__(self, next):
        if (self.cost + self.level == next.cost + next.level):
            return self.cost < next.cost
        else:
            return self.cost + self.level < next.cost + next.level

