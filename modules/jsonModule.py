import json


def printing():
    print 'i am here'


# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
print "commit from branch that we made rebase on it"
