filename="alice.txt"

try:
    with open(filename) as f:
        content=f.read()
except FileNotFoundError:
    print(f"{filename} not found")
