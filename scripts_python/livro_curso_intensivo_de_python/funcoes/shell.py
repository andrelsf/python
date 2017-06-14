#
# Executa comandos via linguagem Python
#
#coding: utf-8

import os
import getpass as gp
import platform as pf

print("\nLogin as " + pf.system() + 
        " in hostname " + pf.node() + "\n")

prompt = gp.getuser() + "@" + pf.node() + " # "

while True:
    try:
        user_name = input("User: ")
        if user_name.lower() == "root":
            user_pass = gp.getpass("passwd: ")
            if "root" in user_name and user_pass == "@root":
                while True:
                    cmd = input(prompt)
                    if cmd.lower() == "h" or cmd.lower() == "help":
                        print("Enter 'Exit' for exit from cmd.")
                    elif cmd.lower() == "exit":
                        break
                    else:
                        os.system(cmd)
        elif user_name == "quit" or user_name == "exit":
            break
        else:
            print("User not found.")
    except KeyboardInterrupt:
        print("")
