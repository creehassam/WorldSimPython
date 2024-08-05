#Libraries
import numpy as np
import random as random
import math as math

#Classes
class Tile:
    def __init__(self, x: int, y: int, type: int):
        tileTypePlants = [0, 100, 35, 0]
        tileTypeAnimals = [0, 15, 10, 0]
        self.x = x
        self.y = y
        self.type = type #{0:"sea", 1:"plains", 2:"hills", 3:"mountains"}
        self.plants = tileTypePlants[type]
        self.animals = tileTypeAnimals[type]
        self.ifCity = False
        self.city = None
        
    def __repr__(self):
        return f"Tile ({self.x},{self.y}): type={self.type}, plants={self.plants}, animals={self.animals}"
    
    def cycle(self):
        plants = self.plants
        animals = self.animals
        typeTile = self.type
        rateGrowPlants = [0, 0.1, 0.1, 0]
        capacityPlants = [0, 5000, 4000, 0]
        plantsConsumed = [0, 0.001, 0.001, 0]
        rateGrowAnimals = [0, 0.04, 0.04, 0]
        capacityAnimals = [0, 22, 20, 0]
        animalsMortality = [0, 0.001, 0.001, 0]
        self.plants = int(max(plants + (rateGrowPlants[typeTile] * plants) * (1 - plants / capacityPlants[typeTile]) - (plantsConsumed[typeTile] * animals) + random.randint(-50, 50), 1))
        self.animals = int(max(animals + (rateGrowAnimals[typeTile] * animals) * (1 - animals / capacityAnimals[typeTile]) * (plants / capacityPlants[typeTile]) - (animalsMortality[typeTile] * animals) - (0.01 * animals / plants + 0.00001) + random.randint(-2, 2), 1))
        
class Kingdom:
    def __init__(self, name: str, capital: object, money: int):
        self.name = name
        self.capital = capital
        self.capitalName = capital
        self.kingdomCitys = []
        self.citysNames = []
        self.money = money
        
    def __repr__(self):
        return f"Kingdom '{self.name}'. citys={self.citysNames}, capital={self.capitalName}, money={self.money}"
        
class City:
    def __init__(self, name: str, kingdom: object, ifCapital: bool, pob: int, money: int, x: int, y: int):
        self.name = name
        self.kingdom = kingdom
        self.pob = pob
        self.money = money
        self.resources = [1, 1, 1] #{0:"food", 1:"weapons", 2:"wood"}
        self.x = x
        self.y = y
        self.ifCapital = ifCapital
        
    def __repr__(self):
        return f"City '{self.name}' from '{self.kingdom.name}' in ({self.x},{self.y}): pob={self.pob}, money={self.money} resources={self.resources}"
        
#Functions

#Basic Functions

def f_generateNameRandom(length: int=6):
    name = ""
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    vowels = ["a", "e", "i", "o", "u"]
    for x in range(length):
        if x % 2 == 0:
            name = name + consonants[random.randint(0, len(consonants)-1)]
        else:
            name = name + vowels[random.randint(0, len(vowels)-1)]
    return name        

#Tile Functions

def f_createMap(sizeX: int, sizeY: int):
    global tiles
    a = []
    if type(sizeX) != int or type(sizeY) != int: #Checking for errors
        return False
    if sizeX <= 0 or sizeY <= 0 or sizeX > 1000 or sizeY > 1000:
        return False
    for x in range(sizeX): #Create the map and the tiles
        b = []
        for y in range(sizeY):
            b.append(Tile(x=x, y=y,type=random.randint(0, 3)))
        a.append(b)
    tiles = a
    return tiles

def f_infoTiles():
    global tiles
    x = len(tiles)
    y = len(tiles[0])
    return f"Tiles: ({x},{y})"

def f_infoTile(x: int, y: int):
    global tiles
    if type(x) != int or type(y) != int:
        return False
    if x >= len(tiles) or y >= len(tiles[0]) or x < 0 or y < 0:
        return False
    return repr(tiles[x][y])
        
#Kingdom Functions

def f_addKingdom(name: str, capital: object, money: int):
    if type(name) != str:
        name = str(name)
    if type(money) != int:
        money = 0
    if type(capital) != object:
        capital = None    
        
    global kingdoms
    kingdomNames = [k.name for k in kingdoms]
    if name in kingdomNames: #Check for a repeated kingdom name
        name = name + "(R)"
    kingdom = Kingdom(name, capital, money)
    kingdoms.append(kingdom)
    return kingdom

def f_deleteKingdom(name: str):
    global kingdoms
    n = 0
    for k in kingdoms:
        if name == k.name:
            kingdoms.pop(n)
            return True
        n += 1
    return False

def f_infoKingdoms():
    global kingdoms
    r = ""
    for k in kingdoms:
        r = r + f"'{k.name}' capital:'{k.capitalName}' money:'{k.money}'\n"
    return r
                
def f_infoKingdom(name: str):
    global kingdoms
    n = 0
    for k in kingdoms:
        if name == k.name:
            return repr(k)
        n += 1
    return False
        
def f_newCapital(kingdom: object, newCapital: object):
    global kingdoms
    if f_infoKingdom(kingdom.name) != False:
        kingdom.capital = newCapital
        kingdom.capitalName = newCapital.name
        return True
    return False
    
#City Functions

def f_randomCity(name: str="no name", kingdom: object=None, pob: int=1, money: int=1):
    global tiles
    while True:
        x = random.randint(0, len(tiles)-1) #Create the coords for the city
        y = random.randint(0, len(tiles[0])-1)
        tile = tiles[x][y]
        
        if tile.type >= 1 and tile.type <= 2: #Verify if the tile is valid and call f_addCity
            return f_addCity(name, kingdom, pob, money, x, y)
        else:
            continue

def f_addCity(name: str, kingdom: object, pob: int, money: int, x: int, y: int):
    if type(name) != str:
        name = str(name)
    if type(pob) != int:
        pob = 0 
    if type(money) != int:
        money = 0
    if type(x) != int:
        x = 0 
    if type(y) != int:
        y = 0     
        
    global citys
    global kingdoms
    global tiles
    
    if tiles[x][y].type < 1 or tiles[x][y].type > 2:
        return False
    
    ifCapital = False
    if type(kingdom) != Kingdom: #Verify if that kingdom exists, if not, create a new one
        kingdom = f_addKingdom(f"Kingdom_of_{name}", name, money)
        ifCapital = True
            
    city = City(name, kingdom, ifCapital, pob, money, x, y) #Create the new city
    citys.append(city)
    
    tiles[x][y].ifCity = True
    tiles[x][y].city = city

    if ifCapital == True: 
        f_newCapital(kingdom, city) #Verify if is a capital
        
    kingdom.kingdomCitys.append(city) #Add the city info
    kingdom.citysNames.append(city.name)
    return city
    
def f_deleteCity(name: str):
    global citys
    global tiles 
    n = 0
    for c in citys:
        if name == c.name: #Search if city exists
            c.kingdom.kingdomCitys.pop(c.kingdom.kingdomCitys.index(c)) #Delete the city from citys and from kingdom
            if len(c.kingdom.kingdomCitys) == 0: #Delete the kingdom if it doesn't have any city
                f_deleteKingdom(c.kingdom.name) 
            elif c.ifCapital == True: #If is a capital, create a new capital
                f_newCapital(c.kingdom, c.kingdom.kingdomCitys[0])
            citys.pop(n)

            tiles[c.x][c.y].ifCity = False
            tiles[c.x][c.y].city = None

            return True
        n += 1
    return False

def f_infoCitys():
    global citys
    r = ""
    for c in citys:
        r = r + f"'{c.name}' from '{c.kingdom.name}'\n"
    return r
                
def f_infoCity(name: str):
    global citys
    n = 0
    for c in citys:
        if name == c.name:
            return repr(c)
        n += 1
    return False

#World Functions

def f_start(sizeX: int, sizeY: int, numKingdoms: int=1):
    global tiles
    global citys
    global kingdoms

    if type(sizeX) != int:
        sizeX = 10
    if type(sizeY) != int:
        sizeY = 10 
    if type(numKingdoms) != int or numKingdoms < 1:
        numKingdoms = 1  

    tiles = f_createMap(sizeX, sizeY)
    citys = []
    kingdoms = []

    for _ in range(numKingdoms): #Add new kingdoms
        k = f_addKingdom(f_generateNameRandom(6), None, 5)
        c = f_randomCity(f_generateNameRandom(4), k, 10, 5)
        f_newCapital(k, c)
    return True


def f_cycle(days: int=1):
    global tiles
    global citys
    global kingdoms

    for _ in range(days):
        for x in range(len(tiles)):
            for y in range(len(tiles[0])):
                tiles[x][y].cycle()
                #Verify if a city exists, if so, simulate it
    #Update kingdoms info
    return True


#Variables
tiles = []
citys = []
kingdoms = []

#Start

tiles = f_createMap(10, 10)