import random


class job:
    def __init__(self,name):
        
        luck=random.randint(1,3)
        
        self.magic=random.randint(3,15)
        self.health=random.randint(3,15)
        self.strength=random.randint(3,15)
        self.initiative=random.randint(3,15)
        self.name=name

        if(luck==1):
            self.klasse="Barbarian"
            self.strength*=3
            self.health*=3
        elif(luck==2):
            self.klasse="Cleric"
            self.magic*=3
            self.initiative*=3
        else:
            self.klasse="Druid"
            self.health*=2
            self.magic*=2
            self.initiative*=2
        
        self.statsum=self.health+self.magic+self.initiative+self.strength

playercount=int(input("How Many Players?: "))

list=[]
for x in range(0,playercount):
    name=input("What's the name of player "+str(x+1)+": ")
    player=job(name)
    list.append(player)
    

print("\n\n!!! Your Characters are complete !!!\n")
for x in range(0,playercount):
    print("%s is a %s!\nStrength: %d\nMagic: %d\nHealth: %d\nInitiative: %d\nTOTAL STATS: %d\n"%(list[x].name,list[x].klasse,list[x].strength,list[x].magic,list[x].health,list[x].initiative,list[x].statsum))
