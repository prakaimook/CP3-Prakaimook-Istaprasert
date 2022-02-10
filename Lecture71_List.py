menuList = []
priceList =[]
amountList =[]


while True:
    menuName = input("Menu name : ")
    if(menuName.lower() == "total"):
        break
    else:
        menuPrice = int(input("Price : "))
        menuAmount = int(input("Amount : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
        amountList.append(menuAmount)
def showBill():
    print("-------- My Shop ---------")
    totalPrice = 0
    for i in range(len(menuList)):
        menuTotal = priceList[i]*amountList[i]
        print(menuList[i],priceList[i],"บาท/หน่วย",amountList[i], "รวม" , menuTotal , "บาท")
        totalPrice = totalPrice + menuTotal
    print("รวม", totalPrice, "บาท")

showBill()


