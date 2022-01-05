# Током неколико дана маратонац се спрема за предстојећу трку. За сваки дан познато је растојање које је
# тог дана претрчао. Одредити да ли је тркач правио напредак тј. да ли су учитани бројеви уређени у строго
# растућем редоследу.
#
# Улаз: Прва линија стандардног улаза садржи природан број N (1 ≤ N ≤ 50) који представља број дана, а
# у свакој од наредних N линија налази се по један природан број који представља број метара који је тркач
# претрчао одговарајућег дана.
#
# Излаз: На стандардном излазу исписати одговор Da ако су бројеви у строго растућем поретку и одговор Ne
# у супротном.
#
# Пример 1
# Улаз
# 4
# 19
# 20
# 22
# 23
# Излаз
# Da

# Пример 2
# Улаз
# 4
# 20
# 20
# 23
# 23
# Излаз
# Ne

n = int(input("Unesi broj dana: "))                 # broj dana za koje se meri vreme plivača
rastuci = True                                      # da li je trenutno obrađeni deo niza strogo rastući
prethodno = int(input("Unesi prvo vreme: "))        # prethodno vreme plivača

for i in range(1, n):
    tekuce = int(input("Unesi novo vreme: "))       # tekuće vreme plivača
    if prethodno >= tekuce:                         # ako danas nije više plivao nego juče
        rastuci = False                             # niz nije rastući
        break                                       # prekidamo dalju analizu
    prethodno = tekuce                              # tekuće vreme postaje prethodno

print("Da" if rastuci else "Ne")                    # prijavljujemo rezultat
