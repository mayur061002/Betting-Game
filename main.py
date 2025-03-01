import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A": 2,
    "B": 8,
    "C": 8,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def deposit():
    while True:
        amount = input("what would you like to deposit? RS ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
        
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valif number")
        else:
            print("Please enter a number.")
        
    return lines

def get_bet():
     while True:
        amount = input("what would you like to bet on each line ? Rs ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between Rs{MIN_BET} - Rs{MAX_BET}.")
        else:
            print("Please enter a number.")
        
     return amount
 
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count): 
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        currents_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            currents_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()
        
def cheak_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
        
    return winnings, winning_lines


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"you do not have enought amount to bet on, your current balacne is: RS{balance}")
        else:
            break
    
    print(f"your betting amount is Rs {bet} on {lines} lines. Total bet is equals to: Rs{total_bet}")
    # print(balance, lines)
    
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = cheak_winnings(slots, lines, bet, symbols_value)
    print(f"You won Rs: {winnings}.")
    print(f"you won on lines: ", * winning_lines)
    return winnings - total_bet

def main():
    
    balance = deposit()
    while True:
        print(f"current balance is Rs: {balance}")
        answar = input("press enter to spin (q to quit).")
        if answar == "q":
            break
        balance += spin(balance)
        
    print("you left with Rs: {balance}")
    
main()
  