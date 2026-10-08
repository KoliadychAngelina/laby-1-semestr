from colorama import Fore, Style, init

init(autoreset=True)

def print_colored_text(text: str) -> str:
    return f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}"