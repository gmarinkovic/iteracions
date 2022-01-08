# Милица је направила списак рођендана својих другарица. Поређала је датуме њиховог рођења хронолошки
# (од најдавнијег до најскоријег). Напиши програм који проверава да ли је Милица то добро урадила.
#
# Улаз: Са стандардног улаза учитава се број n (1 ≤ n ≤ 100). У наредних n линија налази се n исправних,
# међусобно различитих датума. Датуми су записани тако што су записани дан, месец и година, раздвојени
# размацима.
#
# Излаз: У јединој линији стандардног излаза исписати DA ако су датуми исправно (растуће) поређани, тј. NE
# ако нису.
#
# Пример
# Улаз
# 3
# 3 7 2005
# 14 8 2006
# 10 5 2006
# Излаз
# NE

def posle(datum1, datum2):
    (d1, m1, g1) = datum1
    (d2, m2, g2) = datum2
    return (g1 > g2) or (g1 == g2 and m1 > m2) or (g1 == g2 and m1 == m2 and d1 > d2)

def citaj_datum():
    (d, m, g) = map(int, input("Unesi datum u formatu dd.mm.yyyy : ").split("."))
    return (d, m, g)

n = int(input("Unesi broj kontrolisanih datuma: "))

prethodni = citaj_datum()
poredjani = True

for i in range(1, n):
    tekuci = citaj_datum()
    if not posle(tekuci, prethodni):
        poredjani = False
        break
    prethodni = tekuci

print("DA" if poredjani else "NE")
