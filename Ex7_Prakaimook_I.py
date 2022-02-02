# ในการเข้าใช้งานโปรแกรมให้ผู้ล็อคอินโดยใช้ Username และ Password(ผู้เรียนกำหนดเอง)
# หากสำเร็จ โปรแกรมจะขึ้นหน้าต้อนรับและแสดงรายการสินค้าพร้อมราคา (ผู้เรียนกำหนดเอง)
# เมื่อเลือกสินค้าที่ต้องการเรียบร้อยแล้ว โปรแกรมจะถามจำนวนที่ต้องการซื้อ
# หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด
usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "Mong" and passwordInput == "123":
    print("Welcome!")
    print("Mango 30 THB")
    print("Melon 40 THB")
    print("Coconut 10 THB")
    mango = int(30)
    melon = int(40)
    coconut = int(10)
    a = int(input("How many Mango:"))
    b = int(input("How many Melon:"))
    c = int(input("How many Coconut:"))
    price = a*30 + b*40 + c*10
    print ("Total price: " , price)
