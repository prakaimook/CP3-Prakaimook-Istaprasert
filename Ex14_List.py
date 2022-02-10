customerList = [""]
i=1
while True:
    newMember = input("Add member:").capitalize()
    customerList.append(newMember)
    print(customerList)
    print("Number of exiting customers:", customerList.count(newMember))