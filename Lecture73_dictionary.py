systemMenu = {"Rice":50,"Somtam":40,"Drink":10}
selectedMenu = []

def showBill():
    total = 0
    for i in range(len(selectedMenu)):
        print(selectedMenu[i][0],selectedMenu[i][1])
        total = total+int(selectedMenu[i][1])
        print(total)
while True:
    menuName = input("Menu name : ")
    if (menuName.lower() == "total"):
        break
    else:
        selectedMenu.append([menuName,systemMenu[menuName]])
showBill()