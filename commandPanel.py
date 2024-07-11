def test():
    printer("test message")
    
def printer(msg, who="PANEL"):
    who = who.upper()
    print(f"{who}>{msg}")

def command(who="INPUT"):
    return input(f"{who}>")

def help():
    msg = "\nhelp --> show all the commands\ntest --> test message\nexit --> exit of the command panel\nrandomint --> with two numbers, gives a random int between num1 and num2"
    printer(msg)
    
while True:
    try:
        ans = command()
        
        if ans.lower() == "test":
            test()
        elif ans.lower() == "exit":
            exit()
        elif ans.lower() == "help" or ans.lower() == "?":
            help()
        elif ans.lower() == "randomint":
            num1 = int(command("~FIRSTNUMBER"))
            num2 = int(command("~SECONDNUMBER"))
            printer(str(randomInt(num1, num2)))
        else:
            printer(f"command '{ans}' is not recognizable")
    except Exception as error:
        printer(f"error unexpected: '{error}'")
  