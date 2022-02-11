try:
    input1 = int(input("A: "))
    input2 = int(input("B: "))
    print(input1/input2)
except ValueError:
    print("Error! Please Re-enter number")
except ZeroDivisionError:
    print("Error! You can't enter 0")
except:
    print("Error")