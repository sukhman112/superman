from config import *
import PySimpleGUI as sg

def balance():

    balance = 0

    for t in transactions:
        balance += int(t)
    return balance

def validate_int(output):

    while True:
        try:
            value = str(input(output))
            break
        except:
            sg.popup("Du angav inget testa igen")
    return value

def print_transactions():
    
    line = 0
    balance = 0
    output = ("\nAlla transaktioner:"
            "\n{:>3} {:>12} {:>12}"
            "\n----------------------".format("Nr","Händelse","Saldo"))
    
    for t in transactions:
        line += 1
        balance += int(t)
        output += ("\n{:>2}. {:>9} kr {:>9} kr".format(line,t, balance))
    
    return output



def check_file_exists():


    try:
        with open(filename,"x"):
            print("Filen skapades")
        
        with open(filename, "a") as f:
            f.write("{}\n".format(1000))
    
    except:
        return

def read_file():

    check_file_exists()

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                transactions.append(rad)
    


def add_transactions(banklista,toFile=False):


    transactions.append(banklista)
    if toFile:
        write_transactions_to_file(banklista)



def write_transactions_to_file(banklista):

    with open(filename, "a") as f:
        f.write("{}\n".format(transactions))
        