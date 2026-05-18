def elso():
    szavak = []
    for szo in range(5):
        szo = str(input())
        szavak.append(szo)
    for szo in szavak:
        if len(szo) > 4:
            print(szo)

    szavak.insert(2, 'program')

    print(reversed(szavak))
    
    szamlalo = 0

    for szo in szavak:
        if len(szo) > 10:
            szamlalo += 1

    print(szamlalo)



def masodik():
    import math
    #def fugveny():
    jo_tesztak = []
    import random   
    for i in range(30):
        hossz = random.randint(1, 50)    
        if hossz >= 5:
            jo_tesztak.append(hossz)

    legnagyobb = jo_tesztak[0]
    for i in range(1, len(jo_tesztak)):
        if i > legnagyobb:
            legnagyobb = i

    print(len(jo_tesztak))
            
    print(len(jo_tesztak) * 500)
    print(jo_tesztak)

def harmadik():

    x_ek = 0
    sorok_szama = 0
    c_betusek = []
    szoveg = []

    with open('./0518_mind3/merkozesek.txt', 'r', encoding='utf-8') as f:

        for line in f:

            line = line.strip().split(';')
            szoveg.append(line)
            sorok_szama += 1

            for i in line:

                if i == 'X':
                    x_ek += 1
                if i.startswith('C' or 'c'):
                    c_betusek.append(i)

        print(sorok_szama * 2)
        print(x_ek)
        print(c_betusek)

    with open('./0518_mind3/goltalanok.txt', 'w', encoding='utf-8') as be:

        for match in szoveg:

            if match[2] == '0':
                be.write(str(match[0]))
                be.write('\n')
            if match[3] == '0':
                be.write(str(match[1]))
                be.write('\n')
        
harmadik()







