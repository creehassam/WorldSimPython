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
        function()
    elif len(answer)-1 == paramaters:
        function(*answer[1:])
    else:
        f_printer(f"Paramaters aren't correct. Expected:{paramaters}, Recieved:{len(answer)-1}")    

while True:
    try:
        answer = f_input()
        answer = answer.split(" ")
        
        if answer[0].lower() == "test": #Simple Commands
            f_checkInput(f_test)
        elif answer[0].lower() == "exit":
            exit()
        elif answer[0].lower() == "help" or answer[0].lower() == "?":
            f_checkInput(f_help)   

        else:
            f_printer(f"command '{answer[0]}' is not recognizable")
    except Exception as error:
        f_printer(f"error unexpected: '{error}'")
        

  