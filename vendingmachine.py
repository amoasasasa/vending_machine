# we are getting user inputs
# we are using while loop so we can continuously ask for input
# if input is not correct.
# we have three by three slot machine.
import random

MAX_LINES = 3
MIN_BET= 1
MAX_BET=100
ROWS = 3
COLS = 3

symbol_count={
    "A":3,
    "B":6,
    "C":5,
    "D":5
}
symbol_values={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def get_slot_spin(rows,cols,symbols):
    symbol=[]
    for key,value in symbols.items():
        for _ in range(value):
            symbol.append(key)
    # inside this column we are putting three other columns that 
    # will represent slot machine
    columns = []
    for _ in range(cols):
        column=[]
        allsymbol=symbol[:]
        for _ in range(rows):
            value=random.choice(allsymbol)
            allsymbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row],end="|")
            else:
                print(column[row])

def checkwining(columns,lines,multiplier,bet_amt):
    winnings=0
    lineswon=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += multiplier[symbol]*bet_amt
            lineswon.append(line+1)
    return winnings, lineswon

        
def deposit():
    while True:
        amount=input("what would u like to deposit ? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("enter the valid number.")
    return amount
    
def get_number_of_lines():
    while True:
        lines=input("enter the number of lines to bet on (1- "+ str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"lines must be between 1 and ${MAX_LINES}")
        else:
            print("enter the valid number.")
    return lines

def betamount(balance,lines):
    while True:
        bet_amount=input("what amount would u like to bet on each line ? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                bet_amt=bet_amount * lines
                if 1 <= bet_amt <= balance:
                    break
                else:
                    print(f"bet amount is exceeding ur balance ${balance}")
            else:
                print(f"bet amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("enter the valid amount.")
    return bet_amt

def game(balance):
    linenumber=get_number_of_lines()
    bet_amt=betamount(balance,linenumber)
    columns=get_slot_spin(ROWS,COLS,symbol_count)
    print_machine(columns)
    winnings,winninglines=checkwining(columns,linenumber,symbol_values,bet_amt)
    print(f"you won ${winnings}")
    print(f"you won on lines :" ,*winninglines)
    return winnings - bet_amt

def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        if balance == 0:
            print("Starting new round.")
            balance = deposit()
        spin=input("press enter to continue. (q to exit)") 
        if spin == "q":
            break
        else:
            balance += game(balance)   
main()
        