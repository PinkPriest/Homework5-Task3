lines = ""
with open('txt-3.txt', 'w') as f3:
    with open('txt-2.txt') as f2:
        lines = f2.readlines()
    f3.write('txt-2.txt\n')
    f3.write(str(len(lines)) + '\n')
    for line in lines:
        f3.write(line)
    with open('txt-1.txt') as f1:
        lines = f1.readlines()
    f3.write('txt-1.txt\n')
    f3.write(str(len(lines)) + '\n')
    for line in lines:
        f3.write(line)

