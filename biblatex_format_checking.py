import re

print("Please input bib path:")
path = input()
print("Show all parsed file? Y/n")
isListAll = input()

if isListAll == "Y" or isListAll == "y":
    isListAll = True

with open(path, encoding="mbcs") as file:
    i = 1
    for line in file:
        raw_line = line
        if line.startswith("@"):
            i = 1
            try:
                filename = re.search(r"@[a-z]*\{([A-Za-z0-9-]*),", line)[1]
            except TypeError as error:
                print(error, raw_line)
        elif line == "}\n":
            if isListAll == True:
                print("Checked: " + filename)
            i = 0 #quit the entry
        elif i == 1:
            line = line.split("{")
            if (not line[-1].endswith("},\n")) and (not line[-1].endswith('",\n')):
                print("Last caracter is not comma: " + filename + " | " + raw_line)
        elif line == "":
            if i == 1:
                print(filename + "is not closed with a '}'.")

