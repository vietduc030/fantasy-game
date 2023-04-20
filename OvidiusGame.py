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

while(king1==True and king2==True): 
    
    print(f"\n\nLets play round {x+1}: ")
    print("Which Unit do you want to choose?")
    
    #GENERATE NUMBER FOR PLAYER 1
    if(number_soldier1==0 and number_rider1>0):  #If out of soldiers but still riders
     print("Out of Soldier Units. You will choose a Rider this Round")
     player1=rider()
    elif(number_rider1==0 and number_soldier1>0): #if Out of riders but still Soldiers
       print("Out of Rider Units. You will choose a Solduer this Round")
       player1=soldier()
    else:
       unit=input("Choose Your Unit!\nEnter 'soldier' or 'rider': ")
       if(unit=="soldier"): 
          player1=soldier()
       if(unit=="rider"):
          player1=rider()
    print("\nYou rolled ",player1[0])

     #GENERATE NUMBER FOR PLAYER 2
    if(number_soldier2==0 and number_rider2>0):  #If out of soldiers but still riders
     print("Out of Soldiers. Player2 Chooses a Rider!")
     player2=rider()
    elif(number_rider2==0 and number_soldier2>0): #if Out of riders but still Soldiers
       print("Out of Rider Units. Player2 Chooses a Soldier this Round")
       player2=soldier()
    else:
       luck=random.randint(1,2)
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
    print("Player2:",number_soldier2,"Soldiers and",number_rider2 ,"Riders")
    x+=1
    
    if(number_rider1+number_soldier1==0):
       king1=False
    elif(number_rider2+number_soldier2==0):
       king2=False


    
print("Game Ended")
