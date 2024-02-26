"""
Need to figure out the format of the CSV files to be loaded in.

"""


with open("Book1.csv") as file_in:
    lines = []
    for line in file_in:
        print(line)
        lines.append(line)

print(lines)