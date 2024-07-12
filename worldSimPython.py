#Libraries
import numpy as np
import random as random

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
        
    def __repr__(self):
        return f"Tile ({self.x},{self.y}): type={self.type}, plants={self.plants}, animals={self.animals}"
        
class Kingdom:
    def __init__(self, name: str, capital: object, money: int):
        self.name = name
        self.capital = capital
        self.capitalName = capital
        self.citys = []
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

#Tile Functions

def f_createMap(sizeX: int, sizeY: int):
    a = []
    for x in range(sizeX):
        b = []
        for y in range(sizeY):
            b.append(Tile(x=x, y=y,type=random.randint(0, 3)))
        a.append(b)
    return a

def f_infoTiles():
    x = len(tiles)
    y = len(tiles[0])
    return f"Tiles: ({x},{y})"

def f_infoTile(x: int, y: int):
    return repr(tiles[x][y])
        
#Kingdom Functions

def f_addKingdom(name: str, capital: object, money: int):
    kingdomNames = [k.name for k in kingdoms]
    if name in kingdomNames:
        name = name + "(R)"
    kingdom = Kingdom(name, capital, money)
    kingdoms.append(kingdom)
    return kingdom

def f_deleteKingdom(name: str):
    n = 0
    for k in kingdoms:
        if name == k.name:
            kingdoms.pop(n)
            return True
        n += 1
    return False

def f_infoKingdoms():
    r = ""
    for k in kingdoms:
        r = r + f"'{k.name}' capital:'{k.capitalName}' money:'{k.money}'\n"
    return r
                
def f_infoKingdom(name: str):
    n = 0
    for k in kingdoms:
        if name == k.name:
            return repr(k)
        n += 1
    return False
        
def f_newCapital(kingdom: object, newCapital: object):
    if f_infoKingdom(kingdom.name) != False:
        kingdom.capital = newCapital
        kingdom.capitalName = newCapital.name
        return True
    return False
    
#City Functions

def f_randomCity(name: str="no name", kingdom: object=None, pob: int=1, money: int=1):
    while True:
        x = random.randint(0, sizeMapX-1) #Create the coords for the city
        y = random.randint(0, sizeMapY-1)
        tile = tiles[x][y]
        
        if tile.type >= 1 and tile.type <= 2: #Verify if the tile is valid and call f_addCity
            return f_addCity(name, kingdom, pob, money, x, y)
        else:
            continue

def f_addCity(name: str, kingdom: object, pob: int, money: int, x: int, y: int):
    ifCapital = False
    if kingdom == None: #Verify if that kingdom exists, if not, create a new one
        kingdom = f_addKingdom(f"Kingdom_of_{name}", name, money)
        ifCapital = True
            
    city = City(name, kingdom, ifCapital, pob, money, x, y) #Create the new city
    citys.append(city)
    
    if ifCapital == True: 
        f_newCapital(kingdom, city) #Verify if is a capital
        
    kingdom.citys.append(city) #Add the city info
    kingdom.citysNames.append(city.name)
    return city
    
def f_deleteCity(name: str): 
    n = 0
    for c in citys:
        if name == c.name: #Search if city exists
            citys.pop(n) #Delete the city from citys and from kingdom
            c.kingdom.citys.pop(c.kingdom.citys.index(c.name)) 
            if c.ifCapital == True: #If is a capital, create a new capital
                f_newCapital(c.kingdom, c.kingdom.citys[0])
            return True
        n += 1
    return False

def f_infoCitys():
    r = ""
    for c in citys:
        c = c + f"'{c.name}' from '{c.kingdom}'\n"
    return r
                
def f_infoCity(name: str):
    n = 0
    for c in citys:
        if name == c.name:
            return repr(c)
        n += 1
    return False
    
#Variables

sizeMapX = 10
sizeMapY = 10
tiles = []
citys = []
kingdoms = []

#Start

tiles = f_createMap(sizeMapX, sizeMapY)
city1 = f_randomCity("puebla")
print(city1)
tile1 = tiles[city1.x][city1.y]
print(tile1)
print(city1.kingdom)