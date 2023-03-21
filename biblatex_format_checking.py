import re

print("Please input bib path:")
path = input()
print("Show all parsed file? Y/n")
isListAll = input()
if isListAll == "Y" or isListAll == "y":
    isListAll = True

try:
    file = open(path, encoding="mbcs")
    print("mbcs encoding")
except:
    try:
        file = open(path, encoding="UTF-8")
        print("UTF-8 encoding")
    except:
        print("File is neither encoding in mbcs nor in UTF-8")
        print("Please enter your encoding system:")
        style = input()
        file = open(path, encoding=style)
print("---- Parsing ----")

i = 1
counter = 0
for line in file:
    raw_line = line
    if line.startswith("@"):
        i = 1
        try:
            filename = re.search(r"@[\w]*\{([\w-]*),", line)[1]
        except TypeError:
            filename = line.split("{")[1][0:-2]
            print("Not recommended bib reference name: ", filename)
    elif line == "}\n":
        if isListAll == True:
            print("Checked: " + filename)
        i = 0 #quit the entry
        counter += 1
    elif i == 1:
        if line == "\n":
            print(filename + " is not closed with a '}' or has an empty line inside the curly brackets.")
            i = 0 #quit the entry but maybe has other syntactic errors
            continue
        line = line.split("{")
        if re.finditer(r"&", line[-1]):
            for i in re.finditer(r"&", line[-1]):
                if line[-1][i.start() - 1] != '\\':
                    print("'&' instead of '\&': " + filename + " | " + raw_line)
        if (not line[-1].endswith("},\n")) and (not line[-1].endswith('",\n')):
            print("Last caracter is not comma: " + filename + " | " + raw_line)

file.close()
print("Total entries checked: " + str(counter))