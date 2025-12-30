import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_heading():
    print("===============================")
    print("      TIC - TAC - TOE")
    print("===============================")