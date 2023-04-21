import random

def soldier():
    return random.randint(1,6),"s"

def rider():
    return random.randint(1,10),"r"

king1=True
king2=True
number_soldier1=2
number_rider1=1

number_soldier2=2
number_rider2=1
player1=[]
player2=[]
x=0
wrong=True

while(king1==True and king2==True): 
    
    print(f"!LETS PLAY ROUND {x+1}: ")
    print("Which Unit do you want to choose?")
    
    #GENERATE NUMBER FOR PLAYER 1
    if(number_soldier1==0 and number_rider1>0):  #If out of soldiers but still riders
     print("Out of Soldier Units. You will choose a Rider this Round")
     player1=rider()
    elif(number_rider1==0 and number_soldier1>0): #if Out of riders but still Soldiers
       print("Out of Rider Units. You will choose a Soldier this Round")
       player1=soldier()
    else:
       
       while(wrong==True):    ##TYPE AGAIN IF WRONG INPUT
         unit=input("Choose Your Unit!\nEnter 'soldier' or 'rider': ") #If you have at least 1 soldier and 1  rider
         if(unit=="soldier"): 
            player1=soldier()
            wrong=False
            
         elif(unit=="rider"):
            player1=rider()
            wrong=False
         else:
            wrong=input("!!!WRONG INPUT!!! Type Again: ")
            wrong=True
         
    print("\nYou rolled ",player1[0])
    wrong=True


     #GENERATE NUMBER FOR PLAYER 2
    if(number_soldier2==0 and number_rider2>0):  #If out of soldiers but still riders
     print("Out of Soldiers. Player2 Chooses a Rider!",end=" ")
     player2=rider()
     print("He rolled a ",player2[0])
    elif(number_rider2==0 and number_soldier2>0): #if Out of riders but still Soldiers
       print("Out of Rider Units. Player2 Chooses a Soldier this Round",end=" ")
       player2=soldier()
       print("He rolled a ",player2[0])
    else:
       luck=random.randint(1,2)  #50% Chance to Use either Soldier or Rider
       if(luck==1): 
          player2=soldier()
          print("Player 2 Chooses a Soldier. He rolled: ",player2[0])
       else:
          player2=rider()
          print("Player 2 Chooses a Rider. He rolled: ",player2[0])
    
    print("\nFIGHT!")
    if(player1[0]>player2[0]): #If your score is higher
       print("You won this round")
       if(player2[1]=="s"):   #If you won and enemy had soldier
          number_soldier1+=1
          number_soldier2-=1
       else:
          number_rider1+=1   #if you won and enemy used rider
          number_rider2-=1
          
    if(player1[0]<player2[0]): #If your score is lower
       print("You lost this round")
       if(player1[1]=="s"):   #If you lost with soldier
          number_soldier1-=1
          number_soldier2+=1
       else:
          number_rider1-=1   #if you lost with rider
          number_rider2+=1
    
    print("Remaining Units:\nPlayer1:",number_soldier1,"Soldiers and",number_rider1 ,"Riders")
    print("Player2:",number_soldier2,"Soldiers and",number_rider2 ,"Riders\n------------------------")
    x+=1
    
    if(number_rider1+number_soldier1==0):
       king1=False
    elif(number_rider2+number_soldier2==0):
       king2=False


print("Game Ended")
if(king1==True):
   print("WINNER!")
else:
   print("LOOSER!")
