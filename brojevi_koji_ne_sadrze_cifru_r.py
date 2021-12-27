# Напиши програм који одређује колико бројева на стандардном улазу не садржи цифру 5.
#
# Улаз: Свака линија стандардног улаза садржи један природан број из интервала [0, 1000000000].
#
# Излаз: На стандардни излаз исписати колико од учитаних бројева не садржи цифру 5.
#
# Пример
# Улаз
# 12
# 15
# 155
# 14
# Излаз
# 2


import sys

# provera da li dekadni zapis broja n sadrži datu cifru
def sadrzi_cifru(s, cifra):
    while True:                 # ponavljamo postupak
        if s % 10 == cifra:     # ako je poslednja cifra ona tražena
            return True         # broj sadrži cifru
        s = s // 10             # uklanjamo cifru
        if s == 0:              # ako je broj postao 0
            break               # prekidamo postupak
    return False            # cifra nije pronađena

cifra = 5
k=0

for linija in sys.stdin:
    n = int(linija)
    if sadrzi_cifru(n, cifra):
        k = k+1

print("brojevi "," " if k>0 else " ne ", "sadrze cifru " , cifra," i to ",k," puta", sep="")
