def BnBrecursion(m, depth, numNodes, matrixesBefore, step):
    tempM = copyMatrix(m)
    PuzzleToSolve, PuzzleCosts, Move = solve(tempM, matrixesBefore)
    if step ==116:
        for i in range(len(PuzzleToSolve)):
            print("Puzzle", i+1, ":")
            displayMatrix(PuzzleToSolve[i])
            print("Cost:", PuzzleCosts[i])
            print("Move:", Move[i])
            print("")
    position = ["up", "right","down","left"]
    numNodes+=len(Move)
    print("STEP", step)
    print("Move: "+str(Move[0])+"\nCost: "+str(PuzzleCosts[0])+"\nTotal nodes: "+str(numNodes))
    print("Depth: "+str(depth))
    displayMatrix(PuzzleToSolve[0])
    print()
    step+=1

    if PuzzleCosts[0] == 0:
        print("-- PUZZLE SOLVED! --")
    else:
        matrixesBefore.append(m)
        BnB(PuzzleToSolve[0], depth+1, numNodes, matrixesBefore,step)

def solveBiasa(m, matrixesBefore):
    dirs = ["up", "right","down","left"]
    iM = blankPositionI(m)
    jM = blankPositionJ(m)
    mUp = copyMatrix(m)
    mRight = copyMatrix(m)
    mDown = copyMatrix(m)
    mLeft = copyMatrix(m)
    PuzzleToSolve = []
    PuzzleCosts = []
    Move = []
    canMoveUp = False
    canMoveRight = False
    canMoveDown = False
    canMoveLeft = False
    for i in range(len(dirs)):
        if dirs[i] == "up" and iM-1>=0:
            costUp = moveUp(mUp)
            if IsNotInMatrixBefore(mUp, matrixesBefore):
                PuzzleCosts.append(costUp)
                canMoveUp = True
        if dirs[i] == "right" and jM+1<len(m[0]):
            costRight = moveRight(mRight)
            if IsNotInMatrixBefore(mRight, matrixesBefore):
                PuzzleCosts.append(costRight)
                canMoveRight = True
        if dirs[i] == "down" and iM+1<len(m):
            costDown = moveDown(mDown)
            if IsNotInMatrixBefore(mDown, matrixesBefore):
                PuzzleCosts.append(costDown)
                canMoveDown = True
        if dirs[i] == "left" and jM-1>=0:
            costLeft = moveLeft(mLeft)
            if IsNotInMatrixBefore(mLeft, matrixesBefore):
                PuzzleCosts.append(costLeft)
                canMoveLeft = True

    PuzzleCosts.sort()

    up = False
    right = False
    down = False
    left = False
    for cost in PuzzleCosts:
        if canMoveLeft and cost == costLeft and not left:
            PuzzleToSolve.append(mLeft)
            left = True
            Move.append("left")
        elif canMoveDown and cost == costDown and not down:
            PuzzleToSolve.append(mDown)
            down = True
            Move.append("down")
        elif canMoveRight and cost == costRight and not right:
            PuzzleToSolve.append(mRight)
            right = True
            Move.append("right")
        elif canMoveUp and cost == costUp and not up:
            PuzzleToSolve.append(mUp)
            up = True
            Move.append("up")
    return PuzzleToSolve[0], PuzzleCosts[0], Move[0]

def BnB(m, depth, numNodes, matrixesBefore, step):
    temp = copyMatrix(m)
    found = False
    pq = pq.priorityQueue

    PuzzleToSolve, PuzzleCosts, Move = solve(temp, matrixesBefore)
    print("STEP", str(step))
    displayMatrix(PuzzleToSolve)
    print("Cost:", PuzzleCosts)
    print("Move:", Move)
    print("")
    if (PuzzleCosts==0):
        print("-- PUZZLE SOLVED! --")
        found = True
    else:
        matrixesBefore.append(m)
        while not found:
            PuzzleToSolve, PuzzleCosts, Move = solve(PuzzleToSolve, matrixesBefore)
            step+=1
            print("STEP", str(step))
            displayMatrix(PuzzleToSolve)
            print("Cost:", PuzzleCosts)
            print("Move:", Move)
            print("")
            if (PuzzleCosts==0):
                print("-- PUZZLE SOLVED! --")
                found = True

def solve(m, matrixesBefore):
    dirs = ["up", "down","left","right"]
    iM = blankPositionI(m)
    jM = blankPositionJ(m)
    mUp = copyMatrix(m)
    mRight = copyMatrix(m)
    mDown = copyMatrix(m)
    mLeft = copyMatrix(m)
    PuzzleToSolve = []
    PuzzleCosts = []
    Move = []
    canMoveUp = False
    canMoveRight = False
    canMoveDown = False
    canMoveLeft = False
    for i in range(len(dirs)):
        if dirs[i] == "up" and iM-1>=0:
            costUp = moveUp(mUp)
            if IsNotInMatrixBefore(mUp, matrixesBefore):
                PuzzleCosts.append(costUp)
                canMoveUp = True
        if dirs[i] == "right" and jM+1<len(m[0]):
            costRight = moveRight(mRight)
            if IsNotInMatrixBefore(mRight, matrixesBefore):
                PuzzleCosts.append(costRight)
                canMoveRight = True
        if dirs[i] == "down" and iM+1<len(m):
            costDown = moveDown(mDown)
            if IsNotInMatrixBefore(mDown, matrixesBefore):
                PuzzleCosts.append(costDown)
                canMoveDown = True
        if dirs[i] == "left" and jM-1>=0:
            costLeft = moveLeft(mLeft)
            if IsNotInMatrixBefore(mLeft, matrixesBefore):
                PuzzleCosts.append(costLeft)
                canMoveLeft = True

    PuzzleCosts.sort()

    up = False
    right = False
    down = False
    left = False
    for cost in PuzzleCosts:
        if canMoveLeft and cost == costLeft and not left:
            PuzzleToSolve.append(mLeft)
            left = True
            Move.append("left")
        elif canMoveDown and cost == costDown and not down:
            PuzzleToSolve.append(mDown)
            down = True
            Move.append("down")
        elif canMoveRight and cost == costRight and not right:
            PuzzleToSolve.append(mRight)
            right = True
            Move.append("right")
        elif canMoveUp and cost == costUp and not up:
            PuzzleToSolve.append(mUp)
            up = True
            Move.append("up")
    return PuzzleToSolve, PuzzleCosts, Move

def generateChildNode(m, pq):
    dirs = ["up", "down","left","right"]
    iM = blankPositionI(m)
    jM = blankPositionJ(m)
    mUp = copyMatrix(m)
    mRight = copyMatrix(m)
    mDown = copyMatrix(m)
    mLeft = copyMatrix(m)
    PuzzleToSolve = []
    PuzzleCosts = []
    Move = []
    canMoveUp = False
    canMoveRight = False
    canMoveDown = False
    canMoveLeft = False
    for i in range(len(dirs)):
        if dirs[i] == "up" and iM-1>=0:
            costUp = moveUp(mUp)
            if IsNotinVisitedNodes(mUp, matrixesBefore):
                PuzzleCosts.append(costUp)
                canMoveUp = True
        if dirs[i] == "right" and jM+1<len(m[0]):
            costRight = moveRight(mRight)
            if IsNotInMatrixBefore(mRight, matrixesBefore):
                PuzzleCosts.append(costRight)
                canMoveRight = True
        if dirs[i] == "down" and iM+1<len(m):
            costDown = moveDown(mDown)
            if IsNotInMatrixBefore(mDown, matrixesBefore):
                PuzzleCosts.append(costDown)
                canMoveDown = True
        if dirs[i] == "left" and jM-1>=0:
            costLeft = moveLeft(mLeft)
            if IsNotInMatrixBefore(mLeft, matrixesBefore):
                PuzzleCosts.append(costLeft)
                canMoveLeft = True

    PuzzleCosts.sort()

    up = False
    right = False
    down = False
    left = False
    for cost in PuzzleCosts:
        if canMoveLeft and cost == costLeft and not left:
            PuzzleToSolve.append(mLeft)
            left = True
            Move.append("left")
        elif canMoveDown and cost == costDown and not down:
            PuzzleToSolve.append(mDown)
            down = True
            Move.append("down")
        elif canMoveRight and cost == costRight and not right:
            PuzzleToSolve.append(mRight)
            right = True
            Move.append("right")
        elif canMoveUp and cost == costUp and not up:
            PuzzleToSolve.append(mUp)
            up = True
            Move.append("up")
    return PuzzleToSolve, PuzzleCosts, Move
