# Пера се игра картама. Све карте које је имао у руци је сложио тако да прво иду све карте са парним бројевима,
# а затим оне са непарним бројевима (могуће је и да је Пера имао само парне или само непарне карте). Напиши
# програм који проверава да ли је Пера исправно сложио карте.
#
# Улаз: Са стандардног улаза учитавају се бројеви карата (природни бројеви између 2 и 10) све док се не дође
# до краја улаза (он се може унети са Ctrl+Z тј. Ctrl+D). Карата има најмање две, а највише десет.
#
# Излаз: На стандардни излаз исписати da ако је Пера добро сложио карте тј. ne у супротном.
#
# ( prekid sa ctrl + D )
#
# Пример 1
# Улаз
# 2
# 6
# 4
# 5
# 3
# Излаз
# da
#
# Пример 2
# Улаз
# 2
# 6
# 3
# 5
# 4
# Излаз
# ne

OK = True                                               # da li su karte dobro složene
prethodna = int(input("Unesi prvu kartu: "))            # prethodna karta
while True:                                             # ponavljamo sledeći postupak
    try:
        tekuca = int(input("Unesi sledecu kartu: "))    # pokušavamo da učitamo tekuću kartu
    except EOFError:
        break                                           # kraja ulaza, pa prekidamo petlju

    if prethodna % 2 > tekuca % 2:                      # prethodna je neparna, a tekuća parna
        OK = False                                      # karte nisu dobro složene
        break                                           # prekidamo postupak
    prethodna = tekuca                                  # tekuća karta postaje prethodna

print("Da" if OK else "Ne")                             # ispisujemo rezultat
