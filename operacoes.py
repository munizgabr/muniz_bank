import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDeposit
    [2]\tWithdraw
    [3]\tStatement
    [4]\tNew User
    [5]\tNew account
    [6]\tList accounts
    [0]\tExit
    => """
    return input(textwrap.dedent(menu))


def deposit(saldo, amount, statement, /):
    if amount > 0:
        saldo += amount
        statement += f"Deposit:\tR$ {amount:.2f}\n"
        print("\n=== Deposit successful! ===")
    else:
        print("\n@@@ Operation failed! The entered value is invalid. @@@")

    return saldo, statement


def withdraw(*, saldo, amount, statement, limit, num_withdrawals, withdrawal_limit):
    exceeded_balance = amount > saldo
    exceeded_limit = amount > limit
    exceeded_withdrawals = num_withdrawals >= withdrawal_limit

    if exceeded_balance:
        print("\n@@@ Operation failed! You don't have sufficient balance. @@@")

    elif exceeded_limit:
        print("\n@@@ Operation failed! The withdrawal amount exceeds the limit. @@@")

    elif exceeded_withdrawals:
        print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

    elif amount > 0:
        saldo -= amount
        statement += f"Withdrawal:\tR$ {amount:.2f}\n"
        num_withdrawals += 1
        print("\n=== Withdrawal successful! ===")

    else:
        print("\n@@@ Operation failed! The entered value is invalid. @@@")

    return saldo, statement


def display_statement(saldo, /, *, statement):
    print("\n================ STATEMENT ================")
    print("No transactions have been made." if not statement else statement)
    print(f"\nBalance:\tR$ {saldo:.2f}")
    print("============================================")


def create_user(users):
    cpf = input("Enter the CPF (numbers only): ")
    user = filter_user(cpf, users)

    if user:
        print("\n@@@ A user with this CPF already exists! @@@")
        return

    name = input("Enter the full name: ")
    date_of_birth = input("Enter the date of birth (dd-mm-yyyy): ")
    address = input("Enter the address (street, number - neighborhood - city/state abbreviation): ")

    users.append({"name": name, "date_of_birth": date_of_birth, "cpf": cpf, "address": address})

    print("=== User created successfully! ===")


def filter_user(cpf, users):
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None


def create_account(branch, account_number, users):
    cpf = input("Enter the user's CPF: ")
    user = filter_user(cpf, users)

    if user:
        print("\n=== Account created successfully! ===")
        return {"branch": branch, "account_number": account_number, "user": user}

    print("\n@@@ User not found, account creation process terminated! @@@")


def list_accounts(accounts):
    for account in accounts:
        line = f"""\
            Branch:\t\t{account['branch']}
            A/C:\t\t{account['account_number']}
            Holder:\t\t{account['user']['name']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))


def main():
    WITHDRAWAL_LIMIT = 3
    BRANCH = "0001"

    saldo = 0
    limit = 500
    statement = ""
    num_withdrawals = 0
    users = []
    accounts = []

    while True:
        option = menu()

        match option:
            case "1":
                amount = float(input("Enter the deposit amount: "))

                saldo, statement = deposit(saldo, amount, statement)

            case "2":
                amount = float(input("Enter the withdrawal amount: "))

                saldo, statement = withdraw(
                    saldo=saldo,
                    amount=amount,
                    statement=statement,
                    limit=limit,
                    num_withdrawals=num_withdrawals,
                    withdrawal_limit=WITHDRAWAL_LIMIT,
                )

            case "3":
                display_statement(saldo, statement=statement)

            case "4":
                create_user(users)

            case "5":
                account_number = len(accounts) + 1
                account = create_account(BRANCH, account_number, users)

                if account:
                    accounts.append(account)

            case "6":
                list_accounts(accounts)

            case "0":
                print("Thank you!")
                break

            case _:
                print("Invalid operation. Please select a valid option again.")


main()
