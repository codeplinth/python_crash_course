"""
Open a file and print the contents
"""

file_path="pi_digits.txt"

#print contents of a file
with open(file_path) as file_object:
    contents=file_object.read()
print(contents)

#print contents of a file line by line
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

#store file contents in a list
with open(file_path) as file_object:
    lines=file_object.readlines()

pi_string=""

for line in lines:
    pi_string+=line.strip()

print(f"{pi_string[:25]}...")