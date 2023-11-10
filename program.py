import os

files = os.listdir("C:/Users/mi17n/Desktop/HomeWork5-Task3")
txt_files = []
txt_files_dict = {}
txt_files_sorted = []
lines = ""
for file in files:
    if file.endswith(".txt"):
        txt_files.append(file)

for file1 in txt_files:
    count = 0
    for file2 in txt_files:
        with open(file1) as f1:
            with open(file2) as f2:
                lines1 = f1.readlines()
                lines2 = f2.readlines()
                if len(lines1) > len(lines2):
                    count += 1
    txt_files_dict[file1] = count

for file in txt_files:
    txt_files_sorted.append(file)

for i in range(len(txt_files)):
    for file in txt_files_dict:
        if txt_files_dict.get(file) == i:
            txt_files_sorted[i] = file
for file in txt_files_dict:
    txt_files_dict.get(file)

with open('final.txt', 'w') as ff:
    for file in txt_files_sorted:
            with open(file) as f:
                lines = f.readlines()
                if file == txt_files_sorted[0]:
                    ff.write(file + '\n')
                else:
                    ff.write('\n' + file + '\n')
                ff.write(str(len(lines)) + '\n')
                for line in lines:
                    ff.write(line)

