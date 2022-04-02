import pq

def kurang(m, el, iNow, jNow):
    # Penjelasan:
    # fungsi ini berguna untuk menghitung banyak tile j
    # dimana j < i dan POSISI(j) > POSISI(i)
    # fungsi ini akan membantu perhitungan apakah puzzle dapat diselesaikan atau tidak
    # fungsi ini akan mengembalikan nilai kurang(i)
    less = 0
    for i in range (iNow,4):
        if i==iNow:
            strj = jNow
        else:
            strj = 0
        for j in range(strj,4):
            if m[i][j] == 16:
                continue
            else:
                if el> m[i][j]:
                    less+=1
    return less

def reachableGoal(m):
    # Penjelasan:
    # fungsi ini akan menentukan apakah persoalan dapat diselesaikan atau tidak
    # x merupakan nilai 1/0, sel yang diarsir akan bernilai 1, tidak diarsir bernilai 0
    # reachableGoal dilakukan dengan menghitung sigma Kurang(i) + X
    # jika sigma Kurang(i) + x ganjil maka tidak dapat dicapai, akan mereturn FALSE
    # sebaliknya, apabila hasil genap maka akan mereturn TRUE
    totLess = 0
    # checking x
    kurangTable = [0 for i in range (17)]
    for i in range(4):
        for j in range(4):
            if (m[i][j]>16):
                return False
            if (m[i][j]==16):
                if ((i+j)%2==0):
                    x = 0
                else:
                    x = 1
            less = kurang(m, m[i][j], i, j)
            totLess += less
            kurangTable[m[i][j]] = less
    displayKurangTable(kurangTable, x, totLess)
    if (x+totLess)%2==0:
        return True
    else:
        return False

def cost(m):
    # Penjelasan:
    # fungsi ini berguna untuk menghitung cost dengan cara banyaknya ubin tidak kosong yang 
    # tidak terdapat pada susunan akhir
    # fungsi ini mengembalikan cost suatu node
    costs = 0
    ans = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]
    for i in range (4):
        for j in range (4):
            if m[i][j] != 16:
                if m[i][j]!=ans[i][j]:
                    costs+=1
    return costs

def copyMatrix(m):
    # Penjelasan:
    # fungsi ini digunakan untuk mengcopy suatu matrix ke matrix lain
    # guna dari pengc-copy-an matrix ini adalah agar tidak merusak sebuah matrix saat dilakukan deep copy
    # fungsi ini mengembalikan matrix yang telah tercopy
    newM = []
    for i in range(4):
        newM.append([])
        for j in range(4):
            newM[i].append(m[i][j])
    return newM
                
def moveUp(m):
    # Penjelasan:
    # fungsi ini ditujukan untuk mengubah posisi ubin kosong ke atas
    # fungsi ini akan mendeep copy matrix sesuai dengan pergeseran yang dilakukan
    # pergeseran terlebih dahulu di cek apakah memungkinkan (masih dalam ukuran 4x4)
    # jika tidak memenuhi maka tidak akan melakukan perubahan pada matrix
    found = False
    for i in range (4):
        for j in range (4):
            if m[i][j] == 16 and i-1>=0 and (not found):
                m[i][j], m[i-1][j] = m[i-1][j], m[i][j]
                found = True

def moveDown(m):
    # Penjelasan:
    # fungsi ini ditujukan untuk mengubah posisi ubin kosong ke bawah
    # fungsi ini akan mendeep copy matrix sesuai dengan pergeseran yang dilakukan
    # pergeseran terlebih dahulu di cek apakah memungkinkan (masih dalam ukuran 4x4)
    # jika tidak memenuhi maka tidak akan melakukan perubahan pada matrix
    found = False
    for i in range (4):
        for j in range (4):
            if m[i][j] == 16 and i+1<=3 and (not found):
                m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
                found = True
    

def moveRight(m):
    # Penjelasan:
    # fungsi ini ditujukan untuk mengubah posisi ubin kosong ke kanan
    # fungsi ini akan mendeep copy matrix sesuai dengan pergeseran yang dilakukan
    # pergeseran terlebih dahulu di cek apakah memungkinkan (masih dalam ukuran 4x4)
    # jika tidak memenuhi maka tidak akan melakukan perubahan pada matrix
    found = False
    for i in range (4):
        for j in range (4):
            if m[i][j] == 16 and j+1<=3 and (not found):
                m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
                found = True

def moveLeft(m):
    # Penjelasan:
    # fungsi ini ditujukan untuk mengubah posisi ubin kosong ke kiei
    # fungsi ini akan mendeep copy matrix sesuai dengan pergeseran yang dilakukan
    # pergeseran terlebih dahulu di cek apakah memungkinkan (masih dalam ukuran 4x4)
    # jika tidak memenuhi maka tidak akan melakukan perubahan pada matrix
    found = False
    for i in range (4):
        for j in range (4):
            if m[i][j] == 16 and j-1>=0 and (not found):
                m[i][j], m[i][j-1] = m[i][j-1], m[i][j]
                found = True

def displayMatrix(m):
    # Penjelasan:
    # fungsi ini melakukan pencetakan matrix ke layar
    print("╔════╤════╤════╤════╗")
    for i in range(4):
        print("║", end=" ")
        for j in range(4):
            el = m[i][j] 
            line = "0"+ str(el) if el < 10 else str(el)
            if el == 16: 
                line = "  "
            line = line + " │" if j != 3 else line + " ║"
            print(line, end=" ")
        if i != 3:
            print("\n╟────┼────┼────┼────╢")
    print("\n╚════╧════╧════╧════╝")    

def isSame(m1, m2):
    # Penjelasan:
    # fungsi ini membandingkan dua buah matrix yang ada di parameter
    # jika sama mereturn TRUE, jika berbeda mereturn FALSE
    for i in range(4):
        for j in range(4):
            if m1[i][j] != m2[i][j]:
                return False
    return True

def isNotInListOfNodes(nodeToCheck, listOfNodes):
    # Penjelasan:
    # fungsi ini mengeccek apakah sebuah node tidak berada di sebuah list of nodes
    # jika ada akan mereturn FALSE, jika tidak ada akan TRUE 
    for node in listOfNodes:
        if isSame(node.mat, nodeToCheck.mat):
            return False
    return True

def displayInfo(step, node):
    # Penjelasan:
    # fungsi ini digunakan untuk mencetak info dari setiap pengiterasian yang digunakan ke layar
    if step != 0:
        print("-- S T E P ",step,"--")
        print("Cost  :", node.cost)
        print("Level :", node.level)
        print("Move  :", node.move)
    else:
        print("INITIAL PUZZLE STATE")
    displayMatrix(node.mat)
    print("\n")

def displayKurangTable(kurangTable,x, totless):
    # Penjelasan:
    # fungsi ini digunakan untuk mencetak i dan nilai masing-masing yaitu kurang(i) secara berurutan ke layar
    # fungsi ini juga mencetak sigma dari kurang(i) dan x serta pertambahan keduanya
    print(" -------------------")
    print("|  i   |  Kurang(i) |")
    print(" -------------------")
    for i in range(len(kurangTable)):
        if i == 0:
            continue
        else:
            if i<10:
                if kurangTable[i] < 10:
                    print("|  0"+str(i)+"  |    ", kurangTable[i], "     |")
                else:
                    print("|  0"+str(i)+"  |    ", kurangTable[i], "    |")
            else:
                if kurangTable[i] < 10:
                    print("| ",i," |    ",kurangTable[i],"     |")
                else:
                    print("| ",i," |    ",kurangTable[i],"    |")
    print(" -------------------")
    print("\nΣ Kurang(i)     =",str(totless))
    print("Nilai x         =",str(x))
    print("Σ Kurang(i) + x =", str(totless + x))
    print("\n")

def generateChildNode(parent, visitedNodes):
    # Penjelasan:
    # fungsi untuk mengenerate ruang pohon status sesuai parent node(cost terkecil) 
    # fungsi ini akan mngembalikan ARRAY OF GENERATED NODES 

    # menginisialisasi tempat penyimpanan node yaitu pada sebuah array
    generatedNodes = []

    # mengcopy matrix agar menjaga tidak terubah saat deep copy
    parMatrix = copyMatrix(parent.mat)    

    # DOWN
    # mengcopy matrix parent yang nantinya akan dilakukan pergeseran ke bawah
    mDown = copyMatrix(parMatrix)
    # melakukan pergeseran ke bawah
    moveDown(mDown)
    # membuat node baru sesuai atribut pada kelas node
    nodeDown = pq.node(parMatrix,mDown, cost(mDown), parent.level+1, "down")
    # jika node yang baru dibuat tidak ada di list of visitedNodes, maka node akan ditambahkan ke list of nodes
    if isNotInListOfNodes(nodeDown, visitedNodes):
        generatedNodes.append(nodeDown)
    
    # UP
    # mengcopy matrix parent yang nantinya akan dilakukan pergeseran ke atas
    mUp = copyMatrix(parMatrix)
    # melakukan pergeseran ke atas
    moveUp(mUp)
    # membuat node baru sesuai atribut pada kelas node
    nodeUp = pq.node(parMatrix,mUp, cost(mUp), parent.level +1, "up")
    # jika node yang baru dibuat tidak ada di list of visitedNodes, maka node akan ditambahkan ke list of nodes
    if isNotInListOfNodes(nodeUp, visitedNodes):
        generatedNodes.append(nodeUp)
    
    # RIGHT
    # mengcopy matrix parent yang nantinya akan dilakukan pergeseran ke kanan
    mRight = copyMatrix(parMatrix)
    # melakukan pergeseran ke kanan
    moveRight(mRight)
    # membuat node baru sesuai atribut pada kelas node
    nodeRight = pq.node(parMatrix,mRight, cost(mRight), parent.level+1, "right")
    # jika node yang baru dibuat tidak ada di list of visitedNodes, maka node akan ditambahkan ke list of nodes
    if isNotInListOfNodes(nodeRight, visitedNodes):
        generatedNodes.append(nodeRight)
    
    # LEFT
    # mengcopy matrix parent yang nantinya akan dilakukan pergeseran ke kiri
    mLeft = copyMatrix(parMatrix)
    # melakukan pergeseran ke kiri
    moveLeft(mLeft)
    # membuat node baru sesuai atribut pada kelas node
    nodeLeft = pq.node(parMatrix,mLeft, cost(mLeft), parent.level+1, "left")
    # jika node yang baru dibuat tidak ada di list of visitedNodes, maka node akan ditambahkan ke list of nodes
    if isNotInListOfNodes(nodeLeft, visitedNodes):
        generatedNodes.append(nodeLeft)

    # mereturn nodes yang telah dibangkitkan 
    return generatedNodes

def BnB(m):
    # Penjelasan:
    # Fungsi ini dilakukan untuk menyelesaikan persoalan 15 puzzle dengan algoritma branch and bound
    # Fungsi akan berhenti saat dalam keadaan goal state

    # menginisialisasikan priority queue
    PQ = pq.priorityQueue()

    # membuat node awal yaitu node dengan matrix yang sama dengan matrix awal
    parent = pq.node(None,m,cost(m), 0, "initial position")

    # menginisialisasi array of visited nodes
    visitedNodes = []

    # menginisialisasi array of generated nodes
    generatedNodes = [parent]

    # menambahkan node awal ke priority queue
    PQ.push(parent)

    step = 0
    while not(PQ.isEmpty()):
        # pop elemen paling depan prioqueue
        parent = PQ.pop()     

        # menambahkan node yang sekarang akan dibangkitkan sebagai visited node
        visitedNodes.append(parent)

        # mendisplay info untuk iterasi sekarang
        displayInfo(step, parent)

        # jika cost = 0 maka sudah mencapai goal state
        if parent.cost == 0:
            print("\n\( ﾟヮﾟ)/ -- YOUR PUZZLE IS SOLVED! -- ٩(◍╹∀╹◍)۶")
            print("\nTotal Nodes Generated:", len(generatedNodes),"nodes")
            return parent
        else:
            # membangkitkan node child sesuai dengan parent
            childNodes = generateChildNode(parent, visitedNodes)
            # menambahkan node child ke prioqueue dengan priority berupa cost(depth+tile tidak kosong yang berbeda dengan solusi)
            for child in childNodes:
                PQ.push(child)
                generatedNodes.append(child)

        # step akan bertambah satu tiap penelusuran pohon statusn
        step += 1
