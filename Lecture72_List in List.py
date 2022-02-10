#Declare list
menuList = []
priceList = []
amountList = []

#Loop for gettin input info
while True:
    menuName = input("Menu name : ")
    if(menuName.lower() == "total"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuAmount = int(input("Amount : "))
        menuList.append([menuName ,menuPrice ,menuAmount])

# Create function showBill()
def showBill():
    print("-------- My Shop ---------")
    totalPrice = 0
    for i in range(len(menuList)):
        menuTotal = menuList[i][1] * menuList[i][2]
        print(menuList[i][0],menuList[i][2]," @",menuList[i][1], "Baht each" , " = " ,menuTotal,"Baht")
        totalPrice = totalPrice + menuTotal
    print("Total", totalPrice, "บาท")

showBill()


