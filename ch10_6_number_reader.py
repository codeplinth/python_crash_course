import json

filename="numbers.json"

try:
    with open(filename) as f:
        contents=json.load(f)
except FileNotFoundError:
    print(f"{filename} does not exist")
else:
    print(contents)