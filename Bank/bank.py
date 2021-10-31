import random

print("Hello, Bonjour, Guten Tag and Hi Welcome to the Online bank")
create_acc = input("Would you like to create an account (yes/no):  ")

if create_acc == 'yes':
    print("Ok Lets start")

else:
    print("Sorry to see you go!")
    quit()

username = input("Enter your username for your new bank account: ")
password = input("Enter your password for your new bank account: ")
print("To Continue to Your Bank App please enter your credentials")

login1 = input("Enter your Username: ")

if login1 == username:
    print("So far everything is valid")
else:
    print("Wrong Password!")

login2 = input("Enter your Password: ")

if login2 == password:
    print("Almost there!")

print("Congrats I see a successful login!")

bankbal = random.randint(0,100000)
walletbal = random.randint(0,1000)

print("Your bank balance is")
print(bankbal)
print("Your wallet balance is")
print(walletbal)


print("At your bank we can do a lot with your money we can withdraw and deposit ")

choices = input("To withdraw press W to Deposit Press D: ")

if choices == 'W':
    withdraw = int(input("How much would to like to withdraw: "))
    if withdraw > bankbal:
        print("Unable to withdraw bankbal is to low")
    if withdraw < bankbal:
        authW = input("To confirm you are who you are Please enter your Password: ")
    if authW == password:
        print("Withdraw Successful!")
        bankbal -= withdraw
        walletbal += withdraw

elif choices == 'D':
    deposit = int(input("How much would you like to deposit: "))
    if deposit > walletbal:
        print("Unable to deposit wallet balance is too low")
    if deposit < walletbal:
        authD = input("To confirm you are who you are Please enter your Password: ")
    if authD == password:
        print("Deposit was successful!")
        walletbal -= deposit
        bankbal += deposit

else:
    print("I do not not what you want")

print("Your bank balance is")
print(bankbal)
print("Your wallet balance is")
print(walletbal)


choices = input("To withdraw press W to Deposit Press D:  ")

if choices == 'W':
    withdraw = int(input("How much would to like to withdraw: "))
    if withdraw > bankbal:
        print("Unable to withdraw bankbal is to low")
    if withdraw < bankbal:
        authW = input("To confirm you are who you are Please enter your Password: ")
    if authW == password:
        print("Withdraw Successful!")
        bankbal -= withdraw
        walletbal += withdraw

elif choices == 'D':
    deposit = int(input("How much would you like to deposit: "))
    if deposit > walletbal:
        print("Unable to deposit wallet balance is too low")
    if deposit < walletbal:
        authD = input("To confirm you are who you are Please enter your Password: ")
    if authD == password:
        print("Deposit was successful!")
        walletbal -= deposit
        bankbal += deposit


print("For bank reasons we require to logout see you next time")
