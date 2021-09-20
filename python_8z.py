f = open('file1.txt', encoding= 'utf-8')
x = []
while True:
    char = f.read(1)
    if char == '':
        None
    else:
        x.append(char)
    if not char: 
        break
    print(char)

x.reverse()
i = 0

with open('new_file1.txt', 'a', encoding= 'utf-8') as file:
    for j in x:
        file.write(x[i])
        i += 1

f.close()
