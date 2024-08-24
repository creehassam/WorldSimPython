#Libraries
import random as random
import math as math
import gc

#Classes
class Tile:
    def __init__(self, x: int, y: int, type: int):
        tileTypePlants = [0, 3000, 2000, 0]
        tileTypeAnimals = [0, 15, 10, 0]
        self.x = x
        self.y = y
        self.type = type #{0:"sea", 1:"plains", 2:"hills", 3:"mountains"}
        self.plants = tileTypePlants[type]
        self.capacityPlants = [0, 5000, 4000, 0]
        self.animals = tileTypeAnimals[type]
        self.ifCity = False
        self.city = None
        history["tiles"][x][y][0] = [self.plants]
        history["tiles"][x][y][1] = [self.animals]
        
    def __repr__(self):
        return f"Tile ({self.x},{self.y}): type={self.type}, plants={self.plants}, animals={self.animals}"
    
    def cycle(self):
        if self.type >= 1 and self.type <= 2:
            plants = self.plants
            animals = self.animals
            typeTile = self.type
            rateGrowPlants = [0, 0.1, 0.1, 0]
            plantsConsumed = [0, 0.001, 0.001, 0]
            rateGrowAnimals = [0, 0.04, 0.04, 0]
            capacityAnimals = [0, 22, 20, 0]
            animalsMortality = [0, 0.001, 0.001, 0]
            self.plants = math.ceil(max(1, plants + (rateGrowPlants[typeTile] * plants) * (1 - plants / self.capacityPlants[typeTile]) - (plantsConsumed[typeTile] * animals) + random.randint(-10, 10)))
            self.animals = math.ceil(max(1, animals + (rateGrowAnimals[typeTile] * animals) * (1 - animals / capacityAnimals[typeTile]) * (plants / self.capacityPlants[typeTile]) - (animalsMortality[typeTile] * animals) - (0.01 * animals / max(0.1, plants)) + random.randint(-2, 2)))
            history["tiles"][self.x][self.y][0].append(self.plants)
            history["tiles"][self.x][self.y][1].append(self.animals)
            
class Kingdom:
    def __init__(self, name: str, capital: object, pob: int, money: int):
        self.name = name
        self.capital = capital
        self.capitalName = capital
        self.kingdomCitys = []
        self.citysNames = []
        self.pob = pob
        self.money = money
        self.army = 1
        self.isDeleting = False
        self.inWar = False
        self.kingdomsInWar = []
        history["kingdoms"][self.name][0] = [pob]
        history["kingdoms"][self.name][1] = [money]
        
    def __repr__(self):
        return f"Kingdom '{self.name}'. citys={self.citysNames}, capital={self.capitalName}, pob={self.pob}, money={self.money}, PIBpercapita={int(self.money / self.pob)}, Army={self.army}, in war with={self.kingdomsInWar}"
        
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
        history["citys"][self.name][0] = [pob]
        history["citys"][self.name][1] = [money]

        #Cycle Values
        self.foodConsumed = 0.002 #food consumed everyday by one person in tons
        self.foodWorkers = 0.7 #Percent of people working on production of food
        self.efficiencyFood = 0.5 #tons produced by one person in one day
        self.armyWorkers = 0.05 #Percent of people working on the army
        self.woodConsumed = 0.05 #wood consumed everyday by one person in tons
        self.lumberjackWorkers = 0.1 #Percent of people working on wood
        self.efficiencyWood = 1 #tons produced by one person in one day
        self.birthRate = 0.0001 #birth rate per person
        self.deathRate = 0.00006 #death rate per person
        self.valueFood = 100
        self.pobSpents = 10 #Spent for each person in one day
        
    def __repr__(self):
        return f"City '{self.name}' from '{self.kingdom.name}' in ({self.x},{self.y}): pob={self.pob}, money={self.money}, PIBpercapita={int(self.money / self.pob)}, resources={self.resources}"
    
    def cycle(self):
        tile = tiles[self.x][self.y]
        #Resource: Food
        foodConsumed = self.foodConsumed
        foodWorkers = self.foodWorkers
        efficiencyFood = self.efficiencyFood
        maxFoodProduced = tile.plants * 1000 #Maximum of plants producible
        foodProduced = min(maxFoodProduced, math.ceil(self.pob * foodWorkers * efficiencyFood * min(1, tile.plants / (tile.capacityPlants[tile.type] * 1.5)) - self.pob * foodConsumed))
        self.resources[0] += max(0, int(foodProduced * 0.5 - self.resources[0] * 0.05))

        #Resource: Weapon
        armyWorkers = self.armyWorkers
        weaponsProduced = int(self.pob * armyWorkers)
        self.resources[1] = max(0, int(weaponsProduced))

        #Resource: Wood
        woodConsumed = self.woodConsumed
        lumberjackWorkers = self.lumberjackWorkers
        efficiencyWood = self.efficiencyWood
        maxWoodProduced = tile.plants * 100 #Maximum of wood producible
        woodProduced = min(maxWoodProduced, math.ceil(self.pob * lumberjackWorkers * efficiencyWood * min(1, tile.plants / (tile.capacityPlants[tile.type] * 1.5)) - self.pob * woodConsumed) // 10)
        self.resources[2] += max(0, int(woodProduced))

        #Update tile
        tile.plants -= int((foodProduced + self.pob * foodConsumed + self.pob * lumberjackWorkers * efficiencyWood)*0.001)
        if tile.plants < 0:
            tile.plants = 0

        #pob
        birthRate = self.birthRate
        deathRate = self.deathRate
        self.pob += math.ceil((self.pob * birthRate * min(1, self.resources[0] / (self.pob * foodConsumed)) - self.pob * deathRate))

        if self.pob <= 0:
            f_deleteCity(self.name)
            return False
        
        #money
        valueFood = self.valueFood
        self.money += int(foodProduced * 0.5 * valueFood - foodWorkers - weaponsProduced - lumberjackWorkers - self.pob * self.pobSpents)
        self.money = max(0, self.money)

        #Create a new city
        if (self.money / self.pob) > 10 and self.resources[0] > 100 and self.resources[1] > 100 and self.resources[2] > 500000 and self.money > 50000 and self.pob > 10000:
            self.createNewCity()
        
        history["citys"][self.name][0].append(self.pob)
        history["citys"][self.name][1].append(self.money)

    def createNewCity(self):
        n = True
        for x in range(-1, 2):
            for y in range(-1, 2):
                if self.x + x < 0 or self.y + y < 0:
                    continue
                if tiles[self.x + x][self.y + y].type >= 1 and tiles[self.x + x][self.y + y].type <= 2 and tiles[self.x + x][self.y + y].ifCity == False and n == True and (x == 0 or y == 0):
                    f_addCity(f_generateNameRandom(6), self.kingdom, 10000, 50000, self.x + x, self.y + y) #Add new city and stuff
                    self.resources[0] -= 100
                    self.resources[2] -= 5000
                    self.money -= 50000
                    self.pob -= 10000
                    n = False
        
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
    global tiles, kingdoms, citys, history, relations
    return tiles, kingdoms, citys, history, relations

def f_optimizeHistory():
    global history

    for x in range(len(history["tiles"])):
        for y in range(len(history["tiles"][0])):
            if len(history["tiles"][x][y][0]) > 10000:
                history["tiles"][x][y][0].pop(random.randint(0, len(history["tiles"][x][y][0]) - 1) // 10)
            if len(history["tiles"][x][y][1]) > 10000:    
                history["tiles"][x][y][1].pop(random.randint(0, len(history["tiles"][x][y][1]) - 1) // 10)

    for name in history["kingdoms"]:
        if len(history["kingdoms"][name][0]) > 10000:
            history["kingdoms"][name][0].pop(random.randint(0, len(history["kingdoms"][name][0]) - 1) // 10)
        if len(history["kingdoms"][name][1]) > 10000:    
            history["kingdoms"][name][1].pop(random.randint(0, len(history["kingdoms"][name][1]) - 1) // 10)

    for name in history["citys"]:
        if len(history["citys"][name][0]) > 10000:
            history["citys"][name][0].pop(random.randint(0, len(history["citys"][name][0]) - 1) // 10)
        if len(history["citys"][name][1]) > 10000:    
            history["citys"][name][1].pop(random.randint(0, len(history["citys"][name][1]) - 1) // 10)
    return True

def f_findObject(name):
    global kingdoms, citys

    for k in kingdoms:
        if k.name == name:
            return k
    for c in citys:
        if c.name == name:
            return c
    return False

#Tile Functions

def f_createMap(sizeX: int, sizeY: int):
    global tiles, history
    tiles = []

    if type(sizeX) != int or type(sizeY) != int: #Checking for errors
        return False
    if sizeX <= 0 or sizeY <= 0 or sizeX > 100 or sizeY > 100:
        return False

    for x in range(sizeX): #create history tiles
        a = {}
        for y in range(sizeY):
            a[y] = [[], []]
        history["tiles"][x] = a

    a = []
    
    for x in range(sizeX): #Create the map and the tiles
        b = []
        c = {}
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
        
    global kingdoms, history
    kingdomNames = [k.name for k in kingdoms]
    if name in kingdomNames: #Check for a repeated kingdom name
        name = name + "(R)"

    history["kingdoms"][name] = [[], []] #Pob, Money
    kingdom = Kingdom(name, capital, pob, money)
    kingdoms.append(kingdom)
    return kingdom

def f_deleteKingdom(name: str):
    global kingdoms
    n = 0
    for k in kingdoms:
        if name == k.name:
            k.isDeleting = True
            for c in k.kingdomCitys:
                f_deleteCity(c.name)
            kingdoms.pop(n)
            gc.collect()
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
        newCapital.ifCapital = True
        return True
    return False
    
def f_updateKingdomRelations():
    global kingdoms, relations

    #Create a new relations lists
    newRelations = {}
    for k in kingdoms:
        newRelations[k.name] = {}
        for x in range(len(kingdoms)):
            #Update the relation
            relation = f_updateAKingdomRelation(k, kingdoms[x])
            newRelations[k.name][kingdoms[x].name] = relation
    #Update relations list
    relations = newRelations
    return True

def f_updateAKingdomRelation(k1: object, k2: object):
    relation = 50 #Default relation

    if k1 == k2: #Check if the kingdoms are the same
        return 100
    
    distanceBetweenCapitals = f_distanceBetweenCapitals(k1, k2) #Check the distances between the capitals
    if distanceBetweenCapitals >= 5:
        relation += distanceBetweenCapitals * 4
    elif distanceBetweenCapitals <= 3:
        relation -= (1 / distanceBetweenCapitals) * 40

    moneyProportion = k1.money / (k2.money + 1) #Check the proportion of the money
    if moneyProportion > 1.3 and moneyProportion < 0.7:
        relation += 15
    else:
        relation -= 10

    citysProportion = len(k1.citysNames) / len(k2.citysNames) #Check the proportion of the numbers of citys
    if citysProportion > 1.3 and citysProportion < 0.7:
        relation += 15
    else:
        relation -= 10

    pobProportion = k1.pob / (k2.pob + 1) #Check the proportion of pob
    if pobProportion > 1.3 and pobProportion < 0.7:
        relation += 15
    else:
        relation -= 10

    relation = max(0, relation) #Relation must be between 0 and 100
    relation = min(100, relation)

    return int(relation)

def f_distanceBetweenCapitals(k1: object, k2: object):
    x1 = k1.capital.x
    y1 = k1.capital.y
    x2 = k2.capital.x
    y2 = k2.capital.y
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return distance    

def f_declareWar():
    global kingdoms, relations

    for x in relations: #Check if the relation is 0
        for y in relations:
            if relations[x][y] <= 0:

                k1 = f_findObject(x) #Find the kingdoms objects
                k2 = f_findObject(y)

                if k1.inWar == True and k2 in k1.kingdomsInWar or k2.inWar == True and k1 in k2.kingdomsInWar: #Check if they are currently in war
                    continue

                k1.inWar = True #Declare war 
                k1.kingdomsInWar.append(k2)
                k2.inWar = True
                k2.kingdomsInWar.append(k1)
    return True

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
        
    global tiles, kingdoms, citys, history
    
    if tiles[x][y].type < 1 or tiles[x][y].type > 2:
        return False
    
    ifCapital = False
    if type(kingdom) != Kingdom: #Verify if that kingdom exists, if not, create a new one
        kingdom = f_addKingdom(f"Kingdom_of_{name}", name, pob, money)
        ifCapital = True
            
    history["citys"][name] = [[], []] #Pob, Money
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
            c.kingdom.citysNames.pop(c.kingdom.citysNames.index(c.name))

            if len(c.kingdom.kingdomCitys) == 0 and c.kingdom.isDeleting == False: #Delete the kingdom if it doesn't have any city
                f_deleteKingdom(c.kingdom.name) 
            elif c.ifCapital == True and len(c.kingdom.kingdomCitys) > 0: #If is a capital, create a new capital
                f_newCapital(c.kingdom, c.kingdom.kingdomCitys[0])
            citys.pop(n)

            tiles[c.x][c.y].ifCity = False
            tiles[c.x][c.y].city = None
            gc.collect()

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
    global tiles, citys, kingdoms

    if type(sizeX) != int:
        sizeX = 10
    if type(sizeY) != int:
        sizeY = 10 
    if type(numKingdoms) != int or numKingdoms < 1:
        numKingdoms = 1  

    tiles = f_createMap(sizeX, sizeY)
    citys = []
    kingdoms = []

    if tiles == False:
        return False

    for _ in range(numKingdoms): #Add new kingdoms
        k = f_addKingdom(f_generateNameRandom(8), None, 10000, 500)
        c = f_randomCity(f_generateNameRandom(6), k, 10000, 500)
        f_newCapital(k, c)
    return True

def f_cycle(days: int=1):
    global tiles, citys, kingdoms, day

    for d in range(days):
        for x in range(len(tiles)):
            for y in range(len(tiles[0])):
                tiles[x][y].cycle() #Tiles simulation
                if tiles[x][y].ifCity == True: #Verify if a city exists, if so, simulate it
                    tiles[x][y].city.cycle()
        day += 1
        #Update the relations between kingdoms
        f_updateKingdomRelations()
        
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
            army = 0
            for c in k.kingdomCitys:
                pob += c.pob
                money += c.money
                army += c.resources[1]
            k.pob = pob
            k.money = money
            k.army = army
            history["kingdoms"][k.name][0].append(pob)
            history["kingdoms"][k.name][1].append(money)

        f_declareWar()

        if day > 10000:
            f_optimizeHistory()

    return True

#Variables
tiles = []
kingdoms = []
citys = []
history = {"tiles": {}, "kingdoms": {}, "citys": {}}
relations = {}
day = 0

#Start

tiles = f_createMap(3, 3)