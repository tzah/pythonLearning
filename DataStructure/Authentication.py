auth = [["tzahi", "itay"], ["123456", "898989"]]


def auth_func():
    user_name = raw_input("Hey user please insert your name: ")
    user_pass = raw_input("Hey user please insert your password: ")
    try:
        index = auth[0].index(user_name)
        if auth[1][index] == user_pass:
            print "Welcome"
        else:
            raise Exception
    except Exception as e:
        print e.message
        print "I am sorry your user name or password didnt match"


auth_func()
