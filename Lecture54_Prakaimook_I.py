def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        showMenu()
    else:
        print("Please try again")
        login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input("Please select menu>>"))
    if userSelected == 1:
        print("Vat is",vatCalculator(int(input("Price:"))))
    else:
        print("Total price is",priceCalculator())

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice * vat / 100
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

login()