class BudgetTracker:
    def __init__(self):
        self.savings = 0
        self.exp = 0
        self.level = 1

    @property
    def target(self):
        return 100 + 2 * self.level

    def add_money(self, amount):
        if amount <= 0:
            print("Please enter a positive amount.")
            return

        self.savings += amount
        self.exp += amount  

        print(f"You added ${amount}!")
        print(f"Total Savings: ${self.savings}")
        print(f"EXP: {self.exp}")

        self.check_level_up()

    def check_level_up(self):
        while self.exp >= self.target:
            self.exp -= self.target
            self.level += 1
            print(f"Level Up! You are now level {self.level}!")
            print(f"Next level target EXP: {self.target}")



def main_menu():
    game = BudgetTracker()
    
    while True:
        print("\n====== Main Menu ======")
        print("1. Add Money")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount to add: "))
                game.add_money(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            break
        else:
            print("Invalid choice.")
        



# Running the program
if __name__ == "__main__":
    main_menu()