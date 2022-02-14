import json
def readJson():
    # ข้อมูล JSON ที่เราต้องการอ่าน
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    # แปลงข้อมูลให้กลายเป็นรูปที่เราสามารถใช้ได้
    y = json.loads(x)
    # ทำการเรียกข้อมูล age ออกมาแสดง
    print(y["age"])
readJson()

