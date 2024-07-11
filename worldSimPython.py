#Libraries
import numpy as np
import random as random

#Classes
class Tile:
    def __init__(self, x, y, type):
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
    def __init__(self, name, capital, money):
        self.name = name
        self.capital = capital
        self.capitalName = capital
        self.citys = []
        self.citysNames = []
        self.money = money
        
    def __repr__(self):
        return f"Kingdom '{self.name}'. citys={self.citysNames}, capital={self.capitalName}, money={self.money}"
        
class City:
    def __init__(self, name, kingdom, pob, money, x, y):
        self.name = name
        self.kingdom = kingdom
        self.pob = pob
        self.money = money
        self.resources = [1, 1, 1] #{0:"food", 1:"weapons", 2:"wood"}
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"City '{self.name}' from '{self.kingdom.name}' in ({self.x},{self.y}): pob={self.pob}, money={self.money} resources={self.resources}"
        
#Functions

#Tile Functions

def f_createMap(sizeX, sizeY):
    a = []
    for x in range(sizeX):
        b = []
        for y in range(sizeY):
            b.append(Tile(x=x, y=y,type=random.randint(0, 3)))
        a.append(b)
    return a

#Kingdom Functions

def f_createKingdom(name, capital, money):
    kingdom = Kingdom(name, capital, money)
    return kingdom

#City Functions

def f_randomCity(name="no name", kingdom=None, pob=1, money=1):
    while True:
        x = random.randint(0, sizeMapX-1)
        y = random.randint(0, sizeMapY-1)
        tile = tiles[x][y]
        print("LOG:", tile.type)
        if tile.type >= 1 and tile.type <= 2:
            return f_createCity(name, kingdom, pob, money, x, y)
        else:
            continue

def f_createCity(name, kingdom, pob, money, x, y):
    if kingdom == None:
        kingdom = f_createKingdom(f"Kingdom of {name}", name, money)    
    city = City(name, kingdom, pob, money, x, y)
    kingdom.capital = city
    kingdom.capitalName = city.name
    kingdom.citys.append(city)
    kingdom.citysNames.append(city.name)
    return city

#Variables

sizeMapX = 10
sizeMapY = 10
tiles = []

#Start

tiles = f_createMap(sizeMapX, sizeMapY)
city1 = f_randomCity("puebla")
print(city1)
tile1 = tiles[city1.x][city1.y]
print(tile1)
print(city1.kingdom)