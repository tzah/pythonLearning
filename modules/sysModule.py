import sys

fileName = sys.argv[0]
parameter = sys.argv[1]
print("start the printing")
print(fileName)
print(parameter)


def func():
    username = raw_input("Enter username:")
    print("Username is: " + username)


func()


