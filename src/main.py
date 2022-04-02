import time
import functions

def inputFile():
    file = input("Enter file to read: ")
    with open ('../test/'+file, 'r') as f:
        m = []
        for line in f.readlines():
            m.append( [ int (x) for x in line.split(' ') ] )
        return m

def inputKeyboard():
    m = [[0 for _ in range(4)] for _ in range(4)]
    for i in range (4):
        for j in range (4):
            m[i][j] = int(input("Enter value for position ["+str(i)+","+str(j)+"]: "))
    return m

print("""
                                                __                             __      
                                 _      _____  / /________  ____ ___  ___     / /_____ 
                                | | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \\
                                | |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /
                                |__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   \__/\____/ 

 ██╗ ██████╗     ██████╗ ██╗   ██╗███████╗███████╗██╗     ███████╗    ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ 
███║██╔════╝     ██╔══██╗██║   ██║╚══███╔╝╚══███╔╝██║     ██╔════╝    ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗
╚██║███████╗     ██████╔╝██║   ██║  ███╔╝   ███╔╝ ██║     █████╗      ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝
 ██║██╔═══██╗    ██╔═══╝ ██║   ██║ ███╔╝   ███╔╝  ██║     ██╔══╝      ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗
 ██║╚██████╔╝    ██║     ╚██████╔╝███████╗███████╗███████╗███████╗    ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║
 ╚═╝ ╚═════╝     ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝    ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝                                                                                                                       
""")

x = int(input("Main Menu \n1. Input file.txt \n2. Input Keyboard\nYour Choice: "))
if x==1 or x==2:
    if x == 1:
        m = inputFile()
    elif x == 2:
        m = inputKeyboard()
    if(not functions.reachableGoal(m)):
            print("\nYour Puzzle can't be Solved")
            print("""
──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀──
            """)
    else:
            print("\nYour Puzzle can be Solved! :) \n")
            print("""
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
            """)
            
            rootCost = functions.cost(m)
            if rootCost==0:
                print("PUZZLE ALREADY SOLVED!")
            else:
                start_time = time.time()
                functions.BnB(m)
                print("Program executed in %s seconds" % round((time.time() - start_time),5))
else:
    print("Invalid Choice!")
    exit()

