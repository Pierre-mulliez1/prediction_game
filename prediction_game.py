#name: 0 or 1 decision game vs AI
#description: prediction_game in python using memory based decisions
#author: Pierre Mulliez
#Last updated: 03/02/2021

def intparse(value):
#parsing for integer
        try:
            return int(value)
        except ValueError:
            return  "please enter a valid number"
def varparsing(instr):
#prompt for re-entry of data if parsing to integer is not possible 
    number = intparse(input(instr))
    while intparse(number) == "please enter a valid number":
        print("please enter a valid number")
        number = intparse(input(instr))
    return number
#linear congruences function
def congruences(Fsteps,num):
    li = []
    for numb in range(0,Fsteps):
            num = (22695477*num+1)%(2**32)
            li.append(num)
    return li
def randomdecision(li, iteration):
#calculate computer decision given the round 
    if li[iteration] <= 2**32/2:
        comput = 0
    else:
        comput = 1
    return comput 

#initialize value for multiple plays 
play = True 
totalC = 0
totalP = 0

while play == True:
    number = varparsing("seed: ")
    difficult = ""
    difficulty = varparsing("Choose the type of game (1: Easy; 2: Difficult):")
    #check for value != 1 or 2
    while difficulty != 1 and difficulty != 2:
        print("Enter 1 or 2!")
        difficulty = intparse(input("Choose the type of game (1: Easy; 2: Difficult):"))
    steps = varparsing("Enter the number of moves: ")
    init = 0
    throw00 = 0
    throw01 = 0
    throw10 = 0
    throw11 = 0
    comp = 0
    player = "PLAYER: "
    computer = "COMPUTER: "
    scoreM = 0
    scoreP = 0
    win = ""

    #linear congruences list
    lis = congruences(steps,number)
    for numb in range(0,steps):
        print("---")
        #player number 
        val = varparsing("Choose your move number "+ str(numb + 1) +" (0 or 1): ")
        #check for value != 1 or 0
        while val != 1 and val != 0:
            print("Enter 1 or 0!")
            val = intparse(input("Choose your move number "+ str(numb + 1) +" (0 or 1): "))
        if difficulty == 2:
            difficult = "Difficult"
            if init == 0:
                #computer choice
                comp = randomdecision(lis, numb)
                #Add player decision to prediction
                if val == 1:
                    init = 2
                else :
                    init = 1
            elif init == 2:
                #computer choice 
                if throw11 > throw01:
                    comp = 1
                elif throw11 < throw01:
                    comp = 0
                else :
                    comp = randomdecision(lis, numb)
                #Add player decision to prediction
                if val == 1:
                    throw11 += 1
                    init = 2
                else:
                    throw01 += 1
                    init = 1
            else :
                #computer choice 
                if throw10 > throw00:
                    comp = 1
                elif throw10 < throw00:
                    comp = 0
                else :
                    comp = randomdecision(lis, numb)
                #Add player decision to prediction 
                if val == 1:
                    throw10 += 1
                    init = 2
                else:
                    throw00 += 1
                    init = 1
        #easy mode: no prediction
        else:
            difficult = "Easy"
            comp = randomdecision(lis, numb)

        #add round score and display round score
        if val == comp:
            scoreM += 1
            computer = computer + "*"
            win = "-- Computer wins !"
        else:
            scoreP += 1
            player = player + "*"
            win = "-- Player wins !"
        print("player = " + str(scoreP) + " machine = " + str(scoreM) + win)
        print(player + '\n' + computer)
        #final score 
        if numb == steps - 1:
            if scoreP > scoreM:
                totalP += 1
                print("--- \n" + difficult + " game is over, final score: player  "+  str(scoreP) + " - "+ str(scoreM) +" computer - You won!")
            elif scoreP < scoreM:
                totalC += 1
                print("--- \n" + difficult + " game is over, final score: player  "+  str(scoreP) + " - "+ str(scoreM) +" computer - Computer won!")
            else:
                print("--- \n" + difficult + " game is over, final score: player  "+  str(scoreP) + " - "+ str(scoreM) +" computer - It was a tie!")
            #rematch ? set a boolean value for parsing the player input
            bol = False 
            while bol != True:
                va = input("Do you want to start a new game? Yes (Y) No (N): ")
                if (va == 'Y'):
                    play = True
                    bol = True 
                elif (va == 'N'):
                    play = False
                    bol = True 
                else :
                    print("please enter Y or N !")
            #printing total scores over different plays         
            print("Total Player Wins: "+ str(totalP)+ "\nTotal Computer Wins: "+ str(totalC))