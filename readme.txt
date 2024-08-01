Actual Stage --> Testing
Actual Version --> 


This is for "worldSimPython.py". "commandPanel.py" isn't really important for documentation

-----Classes-----

Tile
-Attributes
    -x: int
    -y: int
    -type: int
    -plants: int
    -animals: int
-Methods
    -__init__ 
    -__repr__

Kingdom
-Attributes
    -name: str
    -capital: object
    -capitalName: str
    -kingdomCitys: list of objects
    -citysNames: list of str
    -money: int
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

-----Functions-----

functionName --> Paramaters --> What does --> Output

Tile Functions
-f_createMap --> sizeX: int, sizeY: int --> create a new list(tiles) of tiles --> tiles: list
-f_infoTiles --> none --> return the size of the list tiles --> f"Tiles: ({x},{y})": str
-f_infoTile --> x: int, y: int --> Return the repr of a specific tile --> repr(tiles[x][y]): str

Kingdom Functions
-f_addKingdom --> name: str, capital: object, money: int --> Create a new kingdom a add it to kingdoms list --> kingdom: object
-f_deleteKingdom --> name: str --> Delete a kingdom from kingdoms --> True: Bool / False: Bool
-f_infoKingdoms --> none --> Return the info of the kingdoms --> r: list
-f_infoKingdom --> name: str --> return the info of a specific kingdom --> repr(k): str / False: Bool
-f_newCapital --> kingdom: object, newCapital: object --> Assign a new capital to a kingdom --> True: Bool / False: Bool

CityFunctions
-f_randomCity --> name: str="no name", kingdom: object=None, pob: int=1, money: int=1 --> Create a new city in a random, but valid, position --> (True: Bool / False: Bool) / False: Bool
-f_addCity --> name: str, kingdom: object, pob: int, money: int, x: int, y: int --> Create a new city and add it to citys list --> True: Bool / False: Bool
-f_deleteCity --> name: str --> Delete a city from citys list and from... everything? i mean is deleting it lol --> True: Bool / False: Bool
-f_infoCitys --> none --> Return the info of the citys --> r: list
-f_infoCity --> name: str --> Return the info of a specific city --> repr(c): str / False: Bool

-----Errors/Bugs/Glitches/etc-----

id --> command --> error or output --> how --> possible explanation

Suggests
-A reset button

Bugs
#B0001 --> a lot of functions --> double panel message, one message unexpected --> different hows --> the second message actives despite it shouldn't
#B0004 --> f_deleteKingdom --> Doesn't return a error message when the kingdom isn't deleted and viceversa --> INPUT> deletekingdom randominput --> idk
#B0008 --> f_deleteCity --> It just doesn't work for any value dou --> any --> idk
#B0009 --> f_infoCity --> It just doesn't work for any value dou --> any --> idk

Errors
#E0006 --> f_newCapital --> It always return error unexpected: 'str' object has no attribute 'name' --> any --> maybe with the paramaters