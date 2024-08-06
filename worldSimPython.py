#Libraries
import random as random
import math as math

#Classes
class Tile:
    def __init__(self, x: int, y: int, type: int):
        tileTypePlants = [0, 3000, 2000, 0]
        tileTypeAnimals = [0, 15, 10, 0]
        self.x = x
        self.y = y
        self.type = type #{0:"sea", 1:"plains", 2:"hills", 3:"mountains"}
        self.plants = tileTypePlants[type]
        self.animals = tileTypeAnimals[type]
        self.ifCity = False
        self.city = None
        self.Hplants = [self.plants]
        self.Hanimals = [self.animals]
        
    def __repr__(self):
        return f"Tile ({self.x},{self.y}): type={self.type}, plants={self.plants}, animals={self.animals}"
    
    def cycle(self):
        if self.type >= 1 and self.type <= 2:
            plants = self.plants
            animals = self.animals
            typeTile = self.type
            rateGrowPlants = [0, 0.1, 0.1, 0]
            capacityPlants = [0, 5000, 4000, 0]
            plantsConsumed = [0, 0.001, 0.001, 0]
            rateGrowAnimals = [0, 0.04, 0.04, 0]
            capacityAnimals = [0, 22, 20, 0]
            animalsMortality = [0, 0.001, 0.001, 0]
            self.plants = int(max(plants + (rateGrowPlants[typeTile] * plants) * (1 - plants / capacityPlants[typeTile]) - (plantsConsumed[typeTile] * animals) + random.randint(-10, 10), 1))
            self.animals = int(max(animals + (rateGrowAnimals[typeTile] * animals) * (1 - animals / capacityAnimals[typeTile]) * (plants / capacityPlants[typeTile]) - (animalsMortality[typeTile] * animals) - (0.01 * animals / plants + 0.001) + random.randint(-2, 2), 1))
        self.Hplants.append(self.plants)
        self.Hanimals.append(self.animals)
            
class Kingdom:
    def __init__(self, name: str, capital: object, pob: int, money: int):
        self.name = name
        self.capital = capital
        self.capitalName = capital
        self.kingdomCitys = []
        self.citysNames = []
        self.pob = pob
        self.money = money
        self.Hpob = [pob]
        self.Hmoney = [money]
        
    def __repr__(self):
        return f"Kingdom '{self.name}'. citys={self.citysNames}, capital={self.capitalName}, pob={self.pob}, money={self.money}"
        
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
        self.Hpob = [pob]
        self.Hmoney = [money]
        
    def __repr__(self):
        return f"City '{self.name}' from '{self.kingdom.name}' in ({self.x},{self.y}): pob={self.pob}, money={self.money} resources={self.resources}"
    
    def cycle(self):
        tile = tiles[self.x][self.y]
        #Resource: Food
        foodConsumed = 0.001 #food consumed everyday by one person in tons
        foodWorkers = 0.7 #Percent of people working on production of food
        efficiencyFood = 0.005 #tons produced by one person in one day
        foodProduced = max(0, int(self.pob * foodWorkers * efficiencyFood * min(1, (tile.plants * 1000) / (self.pob * foodWorkers * efficiencyFood))- self.pob * foodConsumed))
        self.resources[0] += int(foodProduced * 0.5)

        #Resource: Weapon
        armyWorkers = 0.05 #Percent of people working on the army
        weaponsProduced = self.pob * armyWorkers
        self.money -= int(weaponsProduced * 0.05)
        self.resources[1] = max(0, int(weaponsProduced))

        #Resource: Wood
        lumberjackWorkers = 0.1 #Percent of people working on wood
        efficiencyWood = 1 #tons produced by one person in one day
        self.resources[2] += max(0, int(self.pob * lumberjackWorkers * efficiencyWood))

        #Update tile
        tile.plants -= int((self.pob * foodWorkers * efficiencyFood + self.pob * lumberjackWorkers * efficiencyWood)*0.001)

        #pob
        birthRate = 0.0001 #birth rate per person
        deathRate = 0.00006 #death rate per person
        self.pob += math.ceil((self.pob * birthRate * min(1, self.resources[0] / (self.pob * foodConsumed)) - self.pob * deathRate))

        if self.pob <= 0:
            f_deleteCity(self.name)
            return False
        
        #money
        valueFood = 100
        self.money += int(foodProduced * 0.5 * valueFood) 

        #Create a new city
        if (self.money / self.pob) > 10 and self.resources[0] > 10 and self.resources[1] > 100 and self.resources[2] > 5000 and self.money > 50000 and self.pob > 1000:
            n = True
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if self.x + x < 0 or self.y + y < 0:
                        continue
                    if tiles[self.x + x][self.y + y].type >= 1 and tiles[self.x + x][self.y + y].type <= 2 and tiles[self.x + x][self.y + y].ifCity == False and n == True and (x == 0 or y == 0):
                        f_addCity(f_generateNameRandom(6), self.kingdom, 1000, 500, self.x + x, self.y + y) #Add new city and stuff
                        self.resources[0] -= 10
                        self.resources[2] -= 5000
                        self.money -= 50000
                        self.pob -= 1000
                        n = False
        
        self.Hpob.append(self.pob)
        self.Hmoney.append(self.money)
        
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

def f_day():
    global day
    return day

def f_updateLists():
    global tiles, kingdoms, citys
    return tiles, kingdoms, citys

#Tile Functions

def f_createMap(sizeX: int, sizeY: int):
    global tiles
    a = []
    if type(sizeX) != int or type(sizeY) != int: #Checking for errors
        return False
    if sizeX <= 0 or sizeY <= 0 or sizeX > 100 or sizeY > 100:
        return False
    
    for x in range(sizeX): #Create the map and the tiles
        b = []
        for y in range(sizeY):
            if x == 0 or x == sizeX-1 or y == 0 or y == sizeX-1:
                b.append(Tile(x=x, y=y,type=0))
                continue
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

def f_addKingdom(name: str, capital: object,pob: int, money: int):
    if type(name) != str:
        name = str(name)
    if type(pob) != int:
        pob = 0
    if type(money) != int:
        money = 0
    if type(capital) != object:
        capital = None    
        
    global kingdoms
    kingdomNames = [k.name for k in kingdoms]
    if name in kingdomNames: #Check for a repeated kingdom name
        name = name + "(R)"
    kingdom = Kingdom(name, capital, pob, money)
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
        r = r + f"'{k.name}' capital:'{k.capitalName}' pob:'{k.pob}' money:'{k.money}'\n"
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
        
        if tile.type >= 1 and tile.type <= 2 and tile.ifCity == False: #Verify if the tile is valid and call f_addCity
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
        
    global tiles, kingdoms, citys
    
    if tiles[x][y].type < 1 or tiles[x][y].type > 2:
        return False
    
    ifCapital = False
    if type(kingdom) != Kingdom: #Verify if that kingdom exists, if not, create a new one
        kingdom = f_addKingdom(f"Kingdom_of_{name}", name, pob, money)
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
    global tiles, citys 
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

def f_infoCitys(details: int=0):
    global citys
    global kingdoms
    r = ""
    if details == 1:
        for k in kingdoms: 
            for c in k.kingdomCitys:
                r = r + repr(c) + "\n"
        return r
    
    for c in citys: #No details
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
        k = f_addKingdom(f_generateNameRandom(8), None, 10000, 500)
        c = f_randomCity(f_generateNameRandom(6), k, 10000, 500)
        f_newCapital(k, c)
    return True


def f_cycle(days: int=1):
    global tiles
    global citys
    global kingdoms
    global day

    for d in range(days):
        for x in range(len(tiles)):
            for y in range(len(tiles[0])):
                tiles[x][y].cycle() #Tiles simulation
                if tiles[x][y].ifCity == True: #Verify if a city exists, if so, simulate it
                    tiles[x][y].city.cycle()
        day += 1
        
        if days > 500:
            if d == int(days / 10): #Just printing the percents with a horrible 'if statements' code
                print("10%")
            elif d == int(days*2 / 10):
                print("20%")
            elif d == int(days*3 / 10):
                print("30%")
            elif d == int(days*4 / 10):
                print("40%")
            elif d == int(days*5 / 10):
                print("50%")
            elif d == int(days*6 / 10):
                print("60%")
            elif d == int(days*7 / 10):
                print("70%")
            elif d == int(days*8 / 10):
                print("80%")
            elif d == int(days*9 / 10):
                print("90%")
                
        #Update kingdoms info
        for k in kingdoms:
            pob = 0
            money = 0
            for c in k.kingdomCitys:
                pob += c.pob
                money += c.money
            k.pob = pob
            k.money = money
            k.Hpob.append(pob)
            k.Hmoney.append(money)
    return True


#Variables
tiles = []
kingdoms = []
citys = []
day = 0

#Start

tiles = f_createMap(10, 10)