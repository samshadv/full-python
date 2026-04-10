balance = 0
is_running = True

def show_balance():
    print(f"Your balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount you want to deposit = "))
    
    if amount < 0:
        print("Deposit can't be negative")
        return 0  
    else:
        return amount

def withdraw():
    amount = float(input("Enter the amount to withdraw = "))
    
    if amount > balance:
        print("Insufficient Balance")
        return 0
    elif amount < 0:
        print("Enter a valid amount")
        return 0
    else:
        return amount

def main():
    global balance, is_running  

    while is_running:
        print("\nBanking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = int(input("Enter your choice (1-4): "))
        
        if choice == 1:
            show_balance()  
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw()   
        elif choice == 4:
            is_running = False
        else:
            print("Please enter a valid number")

    print("Thank you, have a nice day")


if __name__ == "__main__":
    main()