from colorama import init , Fore , Style
init ()

def display () :
    message = f"{Fore.GREEN}Bonjour tout le monde, ceci est une {Fore.CYAN}modification !{Style.RESET_ALL}"
    print ( message )

if __name__ == " __main__ ":
    display ()
