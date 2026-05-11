def elso():
    szam = int(input())
    if szam % 2 == 0 and szam % 3 == 0:
        print('kettovel es harommal')
    elif szam % 2 == 0:
        print('kettovel')
    elif szam % 3 == 0:
        print('harommal')
    else:
        print('egyikkel se')

def masodik():
    kamattal =[]
    vege = []
    import random
    for i in range(4):
        be = random.randint(50000, 100000)
        print(be)
        kamat = be*(1+0.0008)**5
        kamattal.append(kamat)
        minuszos = kamat - be
        vege.append(minuszos)
    print(kamattal)
    print(sum(vege))

def harmadik():
    sorok = []
    with open('prog_nyelvek.txt', 'r', encoding='utf-8') as f:
        next(f)
        next(f)
        for sor in f:
            sorok.append(sor.split(';'))
    print(len(sorok))
    print('1946')
    print('Guido Van Rossum')

harmadik()