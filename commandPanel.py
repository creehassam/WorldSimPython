from worldSimPython import *

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

def f_checkInput(function, numParamaters=0):
    paramaters = []
    for x in answer[1:]: #Convert the int paramaters to int values
        try:
            if x == " ":
                continue
            elif x[-1] == "*":
                x = f_findObject(x[:-1])
                if x == False:
                    x = int(x)
            elif x[-1] == "#":
                x = x[:-1]
                x = int(x)
            else:
                x = int(x)
            paramaters.append(x)
        except:
            paramaters.append(x)
    #f_printer(paramaters, "debug") Debug issues       
    if numParamaters == 0: #Pass the values to the function
        return function()
    elif len(answer)-1 == numParamaters:
        return function(*paramaters)
    else:
        f_printer(f"Paramaters aren't correct. Expected:{numParamaters}, Recieved:{len(answer)-1}")
        return False    

def f_findObject(name):
    for k in kingdoms:
        if k.name == name:
            return k
    for c in citys:
        if c.name == name:
            return c
    return False

#Variables
debug = False

while True:
    try:
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
            if f_checkInput(f_addKingdom, 3) != False:
                f_printer("Kingdom created")
            else:
                f_printer("Kingdom not created", "error")
                
        elif answer[0].lower() == "deletekingdom" and debug: #deletekingdom
            if f_checkInput(f_deleteKingdom, 1) != False:
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
            f_printer(f_checkInput(f_infoCitys))
                
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

        else:
            f_printer(f"command '{answer[0]}' is not recognizable", "error")
    except Exception as error:
        f_printer(f"error unexpected: {error}", "error")
         