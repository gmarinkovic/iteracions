# За низ целих бројева одредити да ли је тестераст. Кажемо да је низ тестераст ако за његове чланове важи
# поредак a1 < a2, a2 > a3, a3 < a4, a4 > a5 итд. или a1 > a2, a2 < a3, a3 > a4, a4 < a5 итд.
#
# Улаз: У првој линији стандардног улаза налази се природан број N (2 ≤ N ≤ 100). У следећих N линија
# налази се по један цео број из интервала од −109 до 109. Бројеви представљају елементе низа.
#
# Излаз: На стандардни излаз приказати поруку DA ако низ јесте тестераст. Иначе приказати поруку NE.
#
# Пример 1
# Улаз
# 6
# 2
# 1
# 3
# 2
# 4
# 3
# Излаз
# DA
#
# Пример 2
# Улаз
# 6
# 1
# 2
# 3
# 4
# 5
# 6
# Излаз
# NE

def razlicitogZnaka(x, y):
    return ( x < 0 and y > 0    or    x > 0 and y < 0 )
    # pošto nema opasnosti od prekoracenja, moglo bi i
    # return x * y <

# broj clanova
n = int(input("Unesi broj clanova niza: "))

# tri uzastopna clana niza su levi, srednji, desni
# ucitavamo prva dva clana
levi = int(input("Unesi clan niza: "))
srednji = int(input("Unesi clan niza: "))

# za sada nismo nasli na elemente ciji je odnos pogresan i za niz mozemo reci da trenutno jeste testerast
# (osim ako su prva dva elementa jednaka)
testerast =  levi != srednji        # true ili false
i = 3

while testerast and i <= n:
    # ucitavamo naredni element
    desni = int(input("Unesi clan niza: "))

    # proveravamo tekuci ”zubac testere”
    if not razlicitogZnaka( srednji - levi , desni - srednji ):
        testerast = False

    levi = srednji
    srednji = desni
    i += 1

if testerast:
    print("DA")
else:
    print("NE")
