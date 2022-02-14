import csv
#ส่วนการเปิดไฟล์ CSV ที่ชื่อ employee_file.txt
with open('Lecture87_employee_file.csv', mode='w') as Lecture87_employee_file:
    #ส่วนการกำหนดการเขียนไฟล์
    employee_writer = csv.writer(Lecture87_employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #ส่วนการเพิ่มข้อมูล
    employee_writer.writerow(['John Smith','Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
    employee_writer.writerow(['Mong', 'MD', 'April'])