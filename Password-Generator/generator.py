import random
import string
import secrets

while True:
    wannagen = input("Would you like to generate a secure password / pin [Y/n]?: ")
    if wannagen == "Y":
        print("Lets get started!")
    elif wannagen == "N":
        print("Sorry to see you go!")
        quit()
    elif wannagen == "y":
        print("Lets get started!")
    elif wannagen == "n":
        print("Sorry to see you go")
        quit()
    else:
        print("Please try again!")
    
    length = int(input("How long should this password be eg. 8: "))

    password = res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(length))  

    print("Generating Password...")
    print(f"Your Generated Password is {password} ")
    print("Copy it and use it for a site") 