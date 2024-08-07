Actual Stage --> Optimization
Actual Version --> 


This is for "worldSimPython.py". "commandPanel.py" has just this little part

in commandPanel.py, when you introduces values:
value* --> the value is the name of a object
value# --> generate a random name with "value" characters

worldSimPython values
-1 plant = 1kt (1kiloton)
-1 animal = 1kt (1kiloton)
-1 pob = 1 person
-1 food = 1t (ton)
-1 money = 1 money (its ficticial so its just "1 money" or "1 unit of money")
-100 money = 1 food

-----Classes-----

Tile
-Attributes
    -x: int
    -y: int
    -type: int
    -plants: int
    -animals: int
    -ifCity: Bool
    -city: object
-Methods
    -__init__ 
    -__repr__
    -cycle

Kingdom
-Attributes
    -name: str
    -capital: object
    -capitalName: str
    -kingdomCitys: list of objects
    -citysNames: list of str
    -pob: int
    -money: int
    -isDeleting: Bool
-Methods
    -__init__
    -__repr__

City
-Attributes
    -name: str
    -kingdom: object
    -pob: int
    -money: int 
    -resources: list of int
    -x: int 
    -y: int 
    -ifCapital: bool
-Methods
    -__init__
    -__repr__
    -cycle
    -createNewCity

-----Functions-----

functionName --> Paramaters --> What does --> Output

Basic Functions
-f_generateNameRandom --> length: int=6 --> generates a random name with the structure consonant-vowel-consonant-vowel... --> name: str
-f_day --> none --> return the value of day --> day: int
-f_updateLists --> none --> It allows me to update the main lists in commandPanel --> da lists x4

Tile Functions
-f_createMap --> sizeX: int, sizeY: int --> create a new list(tiles) of tiles --> tiles: list
-f_infoTiles --> details: int=0 --> return the size of the list tiles --> f"Tiles: ({x},{y})": str
-f_infoTile --> x: int, y: int --> Return the repr of a specific tile --> repr(tiles[x][y]): str

Kingdom Functions
-f_addKingdom --> name: str, capital: object, pob: int, money: int --> Create a new kingdom a add it to kingdoms list --> kingdom: object
-f_deleteKingdom --> name: str --> Delete a kingdom from kingdoms --> True: Bool / False: Bool
-f_infoKingdoms --> none --> Return the info of the kingdoms --> r: list
-f_infoKingdom --> name: str --> return the info of a specific kingdom --> repr(k): str / False: Bool
-f_newCapital --> kingdom: object, newCapital: object --> Assign a new capital to a kingdom --> True: Bool / False: Bool

City Functions
-f_randomCity --> name: str="no name", kingdom: object=None, pob: int=1, money: int=1 --> Create a new city in a random, but valid, position --> (True: Bool / False: Bool) / False: Bool
-f_addCity --> name: str, kingdom: object, pob: int, money: int, x: int, y: int --> Create a new city and add it to citys list --> True: Bool / False: Bool
-f_deleteCity --> name: str --> Delete a city from citys list and from... everything? i mean is deleting it lol --> True: Bool / False: Bool
-f_infoCitys --> none --> Return the info of the citys --> r: list
-f_infoCity --> name: str --> Return the info of a specific city --> repr(c): str / False: Bool

World Functions
-f_start --> sizeX: int, sizeY: int, numKingdoms: int=1 --> Starts a new map and a new game --> True: Bool
-f_cycle --> days: int=1 --> Simulates the map for x time of days-->
-----Errors/Bugs/Glitches/etc-----

-history list is very unoptimal
-f_graph() and f_map() can be broken with any input that is incorrect
-the big memory an speed issue