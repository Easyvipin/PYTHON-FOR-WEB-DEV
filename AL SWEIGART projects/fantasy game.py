#fantasy game
PlayerInventory = { 'rope' : 1 , 'torch' : 2 , 'goldcoin': 4 ,'Shields' : 6 }
def DisplayInventory(inventory) :
    print("Inventory : ")
    sum=0
    for i in inventory :
        print(f"{inventory.get(i)}   {i}")
        sum += inventory.get(i)


    print(f"Total number of items : {sum}")
DisplayInventory(PlayerInventory)

#output
Inventory : 
1   rope
2   torch
4   goldcoin
6   Shields
Total number of items : 13


#dragon loot
dragonLoot = ['goldcoin' , 'torch' , 'torch','Shields','goldcoin','torch']
#after dragonloot
def addToInventory(PlayerInventory,dragonLoot) :
    for i in dragonLoot :
        print(i)
        if  i in PlayerInventory :
            print("hello")
            PlayerInventory[i] += 1
        

addToInventory(PlayerInventory,dragonLoot)
DisplayInventory(PlayerInventory)


#output
Inventory : 
1   rope
5   torch
6   goldcoin
7   Shields
Total number of items : 19
