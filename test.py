def displayMatrix(m):
    for i in range (len(m)):
        print("|", end=" ")
        for j in range (len(m[0])):
            if m[i][j]>0 and m[i][j]<10:
                print("0"+str(m[i][j]), end=" ")
            else:
                print(str(m[i][j]), end=" ")
        print("|") 

def moveUp(m):
    found = False
    for i in range (len(m)):
        for j in range (len(m[0])):
            if m[i][j] == 16 and i!=0 and (not found):
                m[i][j], m[i-1][j] = m[i-1][j], m[i][j]
                found = True
    return 2
    
ans = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
x = moveUp(ans)
displayMatrix(ans)
print(x)



