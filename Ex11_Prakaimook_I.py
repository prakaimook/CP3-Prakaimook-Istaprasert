number = int(input("Number of Asterisk: "))
for x in range(number):
    text = ""
    text = ((number-x+1)*" ")+((2*x+1)*"*")
    print(text)
