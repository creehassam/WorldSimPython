from worldSimPython import *
from graphs import *
import traceback

def f_test():
    f_printer("test message")
    
def f_printer(msg, who="PANEL"):
    who = who.upper()
    print(f"{who}>{msg}")

def f_input(who="INPUT"):
    return input(f"{who}>")

def f_help():
    msg = "Use the readme.txt for better info\nhelp --> show all the commands\ntest --> test message\ndebug --> Switchs between debug mode and user mode\nexit --> exit of the command panel"
    f_printer(msg)

def f_checkInput(function, numParameters=0):
    parameters = []
    for x in answer[1:]: #Convert the int paramaters to int values
        try:
            if x == " ":
                continue
            elif x[-1] == "*": #Searchs a object with x name
                x = f_findObject(x[:-1])
                if x == False:
                    x = int(x)
            elif x[-1] == "#": #Generates a random name with x characters
                x = x[:-1]
                x = int(x)
                parameters.append(f_generateNameRandom(x))
            elif x == "$": #Adds tiles, kingdoms and citys as paramaters
                parameters.append(tiles)
                parameters.append(kingdoms)
                parameters.append(citys)
                parameters.append(history)
                continue
            else:
                x = int(x)
            parameters.append(x)
        except:
            parameters.append(x)
    #f_printer(parameters, "debug") #Debug issues       
    if numParameters == 0: #Pass the values to the function
        return function()
    elif len(parameters) == numParameters:
        return function(*parameters)
    else:
        f_printer(f"Parameters aren't correct. Expected:{numParameters}, Recieved:{len(parameters)}")
        return False    

#Variables
debug = True

while True:
    try:
        gc.collect()
        tiles, kingdoms, citys, history, relations = f_updateLists()
        answer = f_input()
        answer = answer.split(" ")

        #---Simple Commands---

        if answer[0].lower() == "test": #test
            f_checkInput(f_test)

        elif answer[0].lower() == "exit": #exit
            exit()

        elif answer[0].lower() == "help" or answer[0].lower() == "?": #help
            f_checkInput(f_help)   

        elif answer[0].lower() == "debug": #debug
            if debug == False:
                debug = True
                f_printer("debug mode activated")
            else:
                debug = False
                f_printer("debug mode desactivated")

        #---Debug functions---

        elif answer[0].lower() == "createmap" and debug: #createmap
            newTiles = f_checkInput(f_createMap, 2)
            if newTiles != False:
                tiles = []
                tiles = newTiles
                citys = []
                kingdoms = []
                f_printer("Map created")
                
        elif answer[0].lower() == "infotiles" and debug: #infotiles
            f_printer(f_checkInput(f_infoTiles))
            
        elif answer[0].lower() == "infotile" and debug: #infotile
            f_printer(f_checkInput(f_infoTile, 2))
            
        elif answer[0].lower() == "addkingdom" and debug: #addkingdom
            if f_checkInput(f_addKingdom, 4) != False:
                f_printer("Kingdom created")
            else:
                f_printer("Kingdom not created", "error")
                
        elif answer[0].lower() == "deletekingdom" and debug: #deletekingdom
            if f_checkInput(f_deleteKingdom, 1) == False:
                f_printer("Kingdom not deleted", "error")
        
        elif answer[0].lower() == "infokingdoms" and debug: #infokingdoms
            f_printer(f_checkInput(f_infoKingdoms))
        
        elif answer[0].lower() == "infokingdom" and debug: #infokingdom
            infokingdom = f_checkInput(f_infoKingdom, 1)
            if infokingdom != False:
                f_printer(infokingdom)
            else:
                f_printer("Kingdom not found", "error")

        elif answer[0].lower() == "newcapital" and debug: #newcapital
            r = f_checkInput(f_newCapital, 2)
            if r != False:
                f_printer("New capital created")
            else:
                f_printer("Kingdom or city do not exist", "error")
                
        elif answer[0].lower() == "randomcity" and debug: #randomcity
            if f_checkInput(f_randomCity, 4) != False:
                f_printer("City created")
                
        elif answer[0].lower() == "addcity" and debug: #addcity
            if f_checkInput(f_addCity, 6) != False:
                f_printer("City created")

        elif answer[0].lower() == "deletecity" and debug: #deletecity
            r = f_checkInput(f_deleteCity, 1)
            if r != False:
                f_printer("City deleted")
            else:
                f_printer("City not deleted", "error")
        
        elif answer[0].lower() == "infocitys" and debug: #infocitys
            f_printer(f_checkInput(f_infoCitys, 1))
                
        elif answer[0].lower() == "infocity" and debug: #infocity
            r = f_checkInput(f_infoCity, 1)
            if r != False:
                f_printer(r)
            else:
                f_printer("City not found", "error")
        
        #---User functions---

        elif answer[0].lower() == "start": #start
            if f_checkInput(f_start, 3) != False:
                f_printer("Map started")

        elif answer[0].lower() == "cycle": #cycle
            if f_checkInput(f_cycle, 1) != False:
                f_printer("Simulation Completed")

        elif answer[0].lower() == "day": #day
            f_printer(f_day())

        elif answer[0].lower() == "graph": #graph
            if f_checkInput(f_graph, 7) == False:
                f_printer("Graph wasn't displayed")

        elif answer[0].lower() == "map": #map
            f_map(tiles, citys)

        elif answer[0].lower() == "relations": #relations
            f_relations(kingdoms, relations)

        else:
            f_printer(f"command '{answer[0]}' is not recognizable", "error")
    except Exception as error:
        f_printer(f"error unexpected: {traceback.format_exc()}", "error")
         