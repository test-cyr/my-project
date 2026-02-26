

with open('log.txt', 'r') as file:
    for line in file:
        if "ERROR" in line:
            print(line)
