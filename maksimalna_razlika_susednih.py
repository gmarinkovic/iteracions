# Написати програм којим се за n учитаних целих бројева одређује по апсолутној вредности највећа разлика
# два суседна елемента.
#
# Улаз: У првој улазној линији учитава се природан број n (2 ≤ n ≤ 100), a у следећим n целих бројева у
# интервалу [-100,100].
#
# Излаз: Исписује се тражени број који представља највећу апсолутну разлику два суседна броја.
#
# Пример
# Улаз
# 5
# -20
# 30
# 5
# 90
# 70
# Излаз
# 85

n = int(input("Unesi broj celih brojeva: "))
# u svakom trenutku pamtimo dva elementa serije:
# prethodni i tekući
tekuci = int(input("Unesi broj: "))
maks = 0                                    # inicijalizujemo maksimum apsolutnih razlika na nulu


for i in range(1, n):
    prethodni = tekuci                      # raniji tekući sada posaje prethodni
    tekuci = int(input("Unesi broj: "))     # elementu koji sada učitavamo
    if abs(tekuci - prethodni) > maks:      # ako je potrebno
        maks = abs(tekuci - prethodni)      # ažuriramo maksimum

print("Najveca apsolutna razlika je ",maks) # ispisujemo pronađeni maksimum
