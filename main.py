print("1.feladat:")
f = open('valaszok.txt', 'r')
adatok = []
hvalasz = ''
x = f.readline()
x = x.strip()
hvalasz += x
for sor in f:
    sor = sor.strip()
    sor = sor.split()
    adatok.append(sor)

print("2. hany versenyzo vett reszt a teszversenyen?")
n = len(adatok)
print("Tesztversenyen resztvevok szama", n)

print("3.feladat:")
print("versenyzo azonositoja:")
azon = input()
print("A versenyzo azonositoja =", azon)
for val in adatok:
    if val[0] == azon:
        print(val[1], "(versenyzo valasza)")
        valasz3 = val[1]
    else:
        print("A kod helytelen")

print("4. feladat:")
print(" a helyes megoldasok és versenyzo valaszai")
valasz = hvalasz + "(a helyes valaszok)"
print(valasz)
valasz4 = ''
n4 = len(hvalasz)
for i in range(n4):
    if hvalasz[i] == valasz3[i]:
        valasz4 += '+'
    else:
        valasz4 += ' '
print('{0}\t(a versenyzo helyes valaszai)'.format(valasz4))

print("5. feladat: ")
print("hany versenyzonek lett helyes")
print("Kerem a sorszamot!")
n5 = int(input())
db5 = 0
for valasz5 in adatok:
    if valasz5[1][n5] == hvalasz[n5]:
        db5 += 1
print("A feladatra {0} fő, a versenyzők {1} %-a adott helyes választ.".format(db5, round(db5/n*100, 2)))

print('6. feladat: versenyzok pontszama')
g = open('pontok.txt', 'w')
pontok = []
for valasz6 in adatok:
    pont6 = 0
    for i in range(14):
        if i <= 5 and valasz6[1][i] == hvalasz[i]:
            pont6 += 3
        if 6 <= i <= 10 and valasz6[1][i] == hvalasz[i]:
            pont6 += 4
        if 11 <= i <= 13 and valasz6[1][i] == hvalasz[i]:
            pont6 += 5
        if i == 14 and valasz6[1][i] == hvalasz[i]:
            pont6 += 6
    pontok.append(pont6)

for i6 in range(len(adatok)):
    ki6 = adatok[i6][0] + ' ' + str(pontok[i6]) + '\n'
    g.write(ki6)
g.close()

print("7. feladat: A verseny legjobbjai:")
pontok7 = []
for i in range(n):
    x = pontok[i]
    y = adatok[i][0]
    adat7 = [x, y]
    pontok7.append(adat7)
pont_rend = sorted(pontok7, reverse = True)

db = 1
i = 0
while db <= 3:
    print(db, '.dij','(',pont_rend[i][0], 'pont):', pont_rend[i][1])
    while pont_rend[i+1][0] == pont_rend[i][0]:
        i += 1
        print(db, '.dij','(',pont_rend[i][0], 'pont):', pont_rend[i][1])
    db += 1
    i += 1