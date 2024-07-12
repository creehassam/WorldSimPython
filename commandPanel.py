from worldSimPython import *

def f_test():
    f_printer("test message")
    
def f_printer(msg, who="PANEL"):
    who = who.upper()
    print(f"{who}>{msg}")

def f_input(who="INPUT"):
    return input(f"{who}>")

def f_help():
    msg = "\nhelp --> show all the commands\ntest --> test message\nexit --> exit of the command panel\ninfo_object --> name of the object --> show the __repr__ of a object"
    f_printer(msg)

def f_checkInput(function, paramaters=0):
    if paramaters == 0:
        return function()
    elif len(answer)-1 == paramaters:
        return function(*answer[1:])
    else:
        f_printer(f"Paramaters aren't correct. Expected:{paramaters}, Recieved:{len(answer)-1}")
        return False    

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

        #---Simple functions---
        elif answer[0].lower() == "createmap": #createmap
            newTiles = f_checkInput(f_createMap, 2)
            if newTiles != False:
                tiles = newTiles
                citys = []
                kingdoms = []
                f_printer("Map created")
                
        elif answer[0].lower() == "infotiles": #infotiles
            f_printer(f_checkInput(f_infoTiles))
            
        elif answer[0].lower() == "infotile": #infotile
            f_printer(f_checkInput(f_infoTile, 2))
            
        elif answer[0].lower() == "addkingdom": #addkingdom
            if f_checkInput(f_addKingdom, 3) != False:
                f_printer("Kingdom created")
            else:
                f_printer("Kingdom not created", "error")
                
        elif answer[0].lower() == "deletekingdom": #deletekingdom
            if f_checkInput(f_deleteKingdom, 1) != False:
                f_printer("Kingdom not deleted", "error")
        
        elif answer[0].lower() == "infokingdoms": #infokingdoms
            f_printer(f_checkInput(f_infoKingdoms))
        
        elif answer[0].lower() == "infokingdom": #infokingdom
            infokingdom = f_checkInput(f_infoKingdom, 1)
            if infokingdom != False:
                f_printer(infokingdom)
            else:
                f_printer("Kingdom not found", "error")

        elif answer[0].lower() == "newcapital": #newcapital
            r = f_checkInput(f_newCapital, 2)
            if r != False:
                f_printer("New capital created")
            else:
                f_printer("Kingdom or city do not exist", "error")
                
        elif answer[0].lower() == "randomcity": #randomcity
            if f_checkInput(f_randomCity, 4) != False:
                f_printer("City created")
                
        elif answer[0].lower() == "addcity": #addcity
            if f_checkInput(f_addCity, 6) != False:
                f_printer("City created")

        elif answer[0].lower() == "deletecity": #deletecity
            r = f_checkInput(f_deleteCity, 1)
            if r != False:
                f_printer("City deleted")
            else:
                f_printer("City not deleted", "error")
        
        elif answer[0].lower() == "infocitys": #infocitys
            f_printer(f_checkInput(f_infoCitys))
                
        elif answer[0].lower() == "infocity": #infocity
            r = f_checkInput(f_infoCity, 1)
            if r != False:
                f_printer(r)
            else:
                f_printer("City not found", "error")
        
        else:
            f_printer(f"command '{answer[0]}' is not recognizable", "error")
    except Exception as error:
        f_printer(f"error unexpected: '{error}'", "error")
        

  