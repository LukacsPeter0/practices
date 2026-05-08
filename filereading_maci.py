szoveg = []
javitott = []
with open('szoveg.txt', 'r', encoding='utf-8') as f:
    for i in f:
        line = f.readline().strip().split(';')
        szoveg_asd = {line[0], line[1]}
        szoveg.append(szoveg_asd)

with open('out.txt', 'w', encoding='utf-8') as w:
    w.write(str(szoveg))



