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

# broj clanova
n = int(input("Unesi broj clanova niza: "))

# dva uzastopna clana niza cuvamo u promenljivama prethodni i tekuci
# ucitavamo prva dva clana
prethodni = int(input("Unesi clan niza: "))
tekuci = int(input("Unesi clan niza: "))

testerast = True
# znak odredjuje pozeljan odnos izmedju naredna dva elementa
# vrednost 1 ukazuje na to da prethodni treba da bude manji od tekuceg,
# a -1 da prethodni treba da bude veci od tekuceg
# na osnovu odnosa prva dva elementa odredjujemo znak za odnos
# drugog i treceg i tako nadalje
if prethodni > tekuci:
    znak = 1
elif prethodni < tekuci:
    znak = -1
else:
    testerast = False

# obradjujemo ostale elemente dok ne obradimo svih n ili dok
# ne naidjemo na dva elementa u pogresnom redosledu
i = 2

while testerast and i < n:
    # ucitavamo naredni element
    prethodni = tekuci
    tekuci = int(input("Unesi clan niza: "))

    # proveravamo da li je odnos trenutna dva ucitana elementa pogresan
    if znak * prethodni >= znak * tekuci:
        testerast = False

    # odnos naredna dva broja treba da bude suprotan
    znak = -znak

    # prelazimo na naredni element
    i += 1

    # prijavljujemo rezultat

if testerast:
    print("DA")
else:
    print("NE")
