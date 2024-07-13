Actual Stage --> Make the documentation
Actual Version --> 


This is for "worldSimPython.py". "commandPanel.py" isn't really important for documentation

-----Classes-----

Tile
-Attributes
    -x
    -y
    -type
    -plants
    -animals
-Methods
    -__init__ 
    -__repr__

Kingdom
-Attributes
    -name
    -capital
    -capitalName
    -citys
    -citysNames
    -money
-Methods
    -__init__
    -__repr__

City
-Attributes
    -name
    -kingdom
    -pob
    -money
    -resources
    -x
    -y
    -ifCapital
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
