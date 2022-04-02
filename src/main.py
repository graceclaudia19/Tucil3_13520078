import time
import functions

# fungsi untuk input file berupa txt
def inputFile():
    file = input("Enter file to read: ")
    with open ('../test/'+file, 'r') as f:
        m = []
        for line in f.readlines():
            m.append( [ int (x) for x in line.split(' ') ] )
        return m

# fungsi untuk input berupa manual 
def inputKeyboard():
    m = [[0 for _ in range(4)] for _ in range(4)]
    for i in range (4):
        for j in range (4):
            m[i][j] = int(input("Enter value for position ["+str(i)+","+str(j)+"]: "))
            while (m[i][j]> 16 or m[i][j] == 0):
                print("Please only input number 1-15 or 16 for blank space!")
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

while (not(x==1 or x==2)):
    print("Invalid Choice! Please Choose either 1 or 2")
    x = int(input("Main Menu \n1. Input file.txt \n2. Input Keyboard\nYour Choice: "))

if x == 1:
    m = inputFile()
elif x == 2:
    m = inputKeyboard()
    
# mengecek apakah goal reachable dengan metode heuristik
if(not functions.reachableGoal(m)):
        print("INITIAL PUZZLE STATE")
        functions.displayMatrix(m)
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
        # apabila initial state puzzle sudah berupa susunan solusi maka tidak perlu menjalankan pencarian solusi
        if rootCost==0:
            print("INITIAL PUZZLE STATE")

            functions.displayInfon(m)
            print("PUZZLE ALREADY SOLVED!")
        else:
            start_time = time.time()
            # pemanfaatan algoritma branch and bound untuk pencarian solusi
            functions.BnB(m)
            print("Program executed in %s seconds" % round((time.time() - start_time),5))


