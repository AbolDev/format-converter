from colorama import Fore
import os, sys

def clear_screen():
    os.system("cls")

def print_header():
    print(Fore.RED + """
 ███████╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗     ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗ 
 ██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝    ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
 █████╗  ██║   ██║██████╔╝██╔████╔██║███████║   ██║       ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝
 ██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║   ██║       ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗
 ██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║   ██║       ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║
 ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                                                      """, Fore.WHITE + '''

    |---------------------------------------|
    | telegram channel: @IranCrackersTeam   |
    | telegram ID: @ABOL_CRACKER            |
    |---------------------------------------|

''')

def convert_config():
    path = input("Enter the config path => ")

    try:
        with open(path, "r", encoding="utf-8") as conf:
            conf_content = conf.read()
    except FileNotFoundError:
        print("File not found")
        sys.exit()

    file_name = os.path.basename(path)
    name = os.path.splitext(file_name)[0]

    print_options()
    typee = input("Enter the config format => ")

    config_formats = {
        "1": "anom",
        "2": "svb",
        "3": "peb"
    }

    s_type = config_formats.get(typee)
    if not s_type:
        sys.exit()

    with open(f"{name}.{s_type}", "w+", encoding="utf-8") as save:
        save.write(conf_content)

    print(f"\nfile name: {name}.{s_type}")
    input("\nPress enter to close the program ")

def print_options():
    print(Fore.LIGHTBLUE_EX + """
  [1] .anom
  [2] .svb
  [3] .peb
  """)

def main():
    clear_screen()
    print_header()
    convert_config()

if __name__ == "__main__":
    main()
