filmek = []
ertek = []
ketezer = []
rendezok = []

with open('0529/filmek.txt', 'r', encoding='utf-8') as f:
    for sor in f:
        sor = sor.strip().split(';')

        film = {
            'cim': sor[0],
            'rendezo': sor[1],
            'ev': int(sor[2]),
            'ertekeles': int(sor[3])
        }

        filmek.append(film)

for film in filmek:
    if film['ertekeles'] >= 8:
        ertek.append(film['cim'])

    if film['ev'] > 2000:
        ketezer.append(film)

for film in filmek:
    rendezok.append(film['rendezo'])

rendezok.sort()

with open('0529/rendezok.txt', 'w', encoding='utf-8') as w:
    for rendezo in rendezok:
        w.write(rendezo + '\n')

print(len(filmek))
print(str(ertek))
print(len(ketezer))

#feladat = olvasd be, tarol el
#            hany film van a fajlban
#            melyikek ertekelese leg 8
#            hany keszult 2000 utan
#            rendezok.txt b kiirni a rendezoket abc sorrendben