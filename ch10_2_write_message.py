"""
Writing contents to a file
"""

file_name="technologies.txt"

with open(file_name,"w") as file_object:
    file_object.write("Python\n")
    file_object.write("PySpark\n")

with open(file_name,"a") as file_object:
    file_object.write("Informatica\n")
