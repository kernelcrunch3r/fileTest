"""
File Test
Curt Vos
April 8 2022
"""

"""
f = open("txtFile2.txt", "w")
f.writelines("Hello")
f.writelines("\n")
f.writelines("There")
f.close()
"""
"""
h = open("txtFile.txt")
lines = h.readlines()
print(lines)
print(lines[0])
print(lines[1])

h.close()
"""

# changing the file location
c = 0
word = []  # set up a list to hold words
f = open("n:\\ics4u\\words.txt")
lines = f.readlines()
print(lines)

for line in lines:
    # strips out the \n and any formatting
    print("Line {}: {}".format(c, line.strip()))
    word.append("{} {}".format(c, line.strip()))
    c += 1

print(word)
print(word[5])
f.close()

h = open("n:\\ics4u\\words.txt", "a")
h.writelines("\nalpha")
h.close()
