test = "['bajweijjj', '1569 s', '']"

for elem in test.split(", "):
    print(elem.strip("[]"))

print([elem.strip("[]'") for elem in test.split(", ")])
