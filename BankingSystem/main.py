from Account import Account


if __name__ == "__main__":
    print("***********************************")
    print("\tBanking System\t\t")
    print("***********************************")
    print("""\n Choose any of the below option
            1. New Account Creation
            2. Balance Check
            3. Deposit Money
            4. Withdraw Money
          """)
    option = input("Choose an option (1-4):")
    if option == "1":
        name = input("Enter name for account creation: ")
        initial_amount = input("Enter Initial amount: ")
        acct: Account = Account(name, float(initial_amount))
        acct.get_balance()
        
        
    # print(f"Balance amount {sandeep.balance}Rs")

    # sandeep.deposit(5000)
    # print(f"Balance amount {sandeep.balance}Rs")

    # sandeep.withdraw(10000)
    # sandeep.withdraw(4000)
