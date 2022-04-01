def kurang(m,el, iNow, jNow):
    less = 0
    for i in range (iNow,len(m)):
        if i==iNow:
            strj = jNow
        else:
            strj = 0
        for j in range(strj,len(m[0])):
            if m[i][j] =="":
                continue
            else:
                if int(el)>int(m[i][j]):
                    less+=1
    return less

def numberOfTilesNotInPosition(m):
    cost = 0
    ans = [["1","2","3","4"],
           ["5","6","7","8"],
           ["9","10","11","12"],
           ["13","14","15",""]]
    for i in range (m):
        for j in range (m[0]):
            if m[i][j]!=ans[i][j]:
                cost+=1
    return cost
                

                
# def moveUp(m, i, j, el):
#     # i and j in current position
#     # STILL BROKEN
#     for i in range (len(m)):
#         for j in range (len(m[0])):
#             if m[i][j] == "":
#                 m[i][j] = el
#                 m[j][i] = ""
#                 return m






# check whether it can be solvedd or not,input matrix, return bool
def reachableGoal(m):
    totLess = 0
    sixteen = False
    nSixteen = 0
    # checking x
    for i in range(len(m)):
        for j in range(len(m[i])):
            if (m[i][j]==""):
                if ((i+j)%2==0):
                    x = 0
                else:
                    x = 1
                sixteen = True
            else:
                less = kurang(m, m[i][j], i, j)
                print("KURANG("+m[i][j]+") =", less)
                if (sixteen):
                    nSixteen+=1
            totLess += less
    totLess+=nSixteen
    print("KURANG(16) =", nSixteen)
    print("SIGMA KURANG(i) =",totLess)
    print("X = ", x)
    print("SIGMA KURANG(i) + X =", totLess+x)
    if (x+totLess)%2==0:
        return True
    else:
        return False





# file = input("Enter file to read: ")
file = "18.txt"
with open ('../test/'+file, 'r') as f:
    m = []
    for line in f.readlines():
        temp = line.strip().split(",")
        m.append(temp)
    for i in range (len(m)):
        for j in range (len(m[0])):
            print(m[i][j], end = " ")
        print()
    if(not reachableGoal(m)):
        print("Tidak dapat diselesaikan!")
    else:
        print("bisa")


# def kurang(i)

