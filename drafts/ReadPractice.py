import os

print (os.getcwd())

with open('list.txt', encoding='utf-8') as file:
    test = file.readlines()
    words = list()
    for line in test:
        line = line.rstrip()
        line = line.replace('.',' ')
        words.extend(line.split())
    for f in words:
        print(f)
