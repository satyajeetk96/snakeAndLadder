# Required Libraries
import random
import time

# This function generates a number between 1 to 6 (inclusive)
def rollTheDice():
    value = random.randint(1,6)
    print("Dice value: " + str(value))
    return value

# The game function
def startTheGame():
    # Initially both the players are at 1
    playerA = 1
    playerB = 1
    
    snake_dic = {99:45, 23:9, 65:34, 78:56, 41:22, 27:6, 55:30} # Snake dictionary
    ladder_dic = {8:24, 17:40, 49:86, 37:85, 13:44, 57:95} # Ladder dictionary
    
    # Terminate the loop if any player crosses the 100 mark
    while(playerA < 100 and playerB < 100):
        print("\nA's Turn:")
        playerA = playerA + rollTheDice()
        if(playerA in snake_dic.keys()): # If snake is present at any number
            playerA = snake_dic[playerA] # Player value will go to the tail of the snake
        elif(playerA in ladder_dic.keys(-+)): # If a ladder is present at any number
            playerA = ladder_dic[playerA] # Player will climb up the ladder
        print("Score of player A: " + str(playerA))
        time.sleep(2)
        
        print("\nNow B's Turn:")
        playerB = playerB + rollTheDice()
        if(playerB in snake_dic.keys()): # If snake is present at any number
            playerB= snake_dic[playerB]  # Player  value will go to the tail of the snake
        elif(playerB in ladder_dic.keys()): # If a ladder is present at any number
            playerB = ladder_dic[playerB] # Player will climb up the ladder
        print("Score of player B: " + str(playerB))
        time.sleep(2)

    if(playerA >= 100):
        print("\n\nPlayer A wins!!!")
    else:
        print("\n\nPlayer B wins!!!")
        

if __name__ == "__main__":
    startTheGame()

