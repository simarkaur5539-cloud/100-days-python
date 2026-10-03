try:
    num=int(input("enter the integer"))
except ValueError:
    print("invalid input")
finally:
    print("this block will always execute")