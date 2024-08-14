import colorama


def cprint(case, text):
    colorama.init(autoreset=True)
    if case == "G":
        print(colorama.Fore.GREEN + "> " + text)
    elif case == "R":
        print(colorama.Fore.RED + "> " + text)
    elif case == "N":
        print(colorama.Fore.YELLOW + "> " + text)
