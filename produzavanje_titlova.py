# Станислав је ђак првог разреда и тек учи да чита. Покушава да прочита титлове на цртаном филму који гледа
# током карантина, али му често недостаје неколико секунди да би их прочитао до краја. Његова сестра жели
# да му помогне тако што ће продужити трајање сваког титла за пет секунди. Међутим, некада је пауза до
# наредног титла краћа од 5 секунди, па да се титлови не би преклапали, она титл продужава тачно до почетка
# наредног. Последњи титл се сигурно може продужити за 5 секунди. Пошто је филм дугачак, ово је напоран
# посао. Напиши програм који би Станислављевој сестри помогао да овај посао брже заврши.
# Улаз: Са стандардног улаза се уноси укупан број титлова n (1 ≤ n ≤ 1000), и након тога у наредних n
# линија подаци о титловима. За сваки титл се уноси време почетка и време краја (у односу на почетак филма),
# раздвојени размаком. Свако време задато је у облику hh:mm:ss. Филм не траје дуже од 3 сата.
# Излаз: На стандардни излаз исписати податке о продуженим титловима (у истом формату у ком су унети).
# Пример
# Улаз
# 5
# 00:01:43 00:01:48
# 00:01:56 00:01:59
# 00:02:17 00:02:23
# 00:02:24 00:02:26
# 00:02:30 00:02:38
# Излаз
# 5
# 00:01:43 00:01:53
# 00:01:56 00:02:04
# 00:02:17 00:02:24
# 00:02:24 00:02:30
# 00:02:30 00:02:43

# za trenutak h:m:s odredjuje se broj sekundi S proteklih od prethodne ponoci
def u_sekunde(h, m, s):
    return h * 60 * 60 + m * 60 + s

# za dati broj sekundi S proteklih od prethodne ponoci, odredjuje se vremenski trenutak (sat h, minut m i sekund s)
def od_sekundi(S):
    s = (S // 1) % 60
    m = (S // 60) % 60
    h = (S // (60*60)) % 24
    return (h, m, s)

def dve_pozicije(x):
    y=x
    if x < 10:
        y='0' + str(x)

    return y

n = int(input("Unesi broj titlova: "))

# dan, minut i sekund
(hp,mp,sp) = map(int,input("Unesi vreme pocetka titla u formatu hh:mm:ss  ").split(":"))

# broj sekundi od prethodne ponociinput
Sp = u_sekunde(hp, mp, sp)

# dan, minut i sekund
(hk,mk,sk) = map(int,input("Unesi vreme predvidjenog kraja titla u formatu hh:mm:ss  ").split(":"))

# broj sekundi od prethodne ponociinput
Sk = u_sekunde(hk, mk, sk)


for i in range(0,n-1):

    (ht, mt, st) = map(int, input("Unesi vreme pocetka titla u formatu hh:mm:ss  ").split(":"))
    St = u_sekunde(ht, mt, st)
    if St - Sk >= 5:
        Sk = Sk+5
        (hk, mk, sk) = od_sekundi(Sk)
        print(str(hp).zfill(2),":",str(mp).zfill(2),":",str(sp).zfill(2), " " , str(hk).zfill(2), ":", str(mk).zfill(2), ":", str(sk).zfill(2), sep="")
    else:
        Sk == St
        print(str(hp).zfill(2),":",str(mp).zfill(2),":",str(sp).zfill(2), " " , str(ht).zfill(2), ":", str(mt).zfill(2), ":", str(st).zfill(2), sep="")

    ( hp,mp,sp ) = ( ht,mt,st )
    ( hk,mk,sk ) = map(int, input("Unesi vreme predvidjenog kraja titla u formatu hh:mm:ss  ").split(":"))
    Sk = u_sekunde(hk, mk, sk)
    if i == n-2 :
        Sk = Sk + 5
        (hk,mk,sk) = od_sekundi(Sk)
        print(str(hp).zfill(2),":",str(mp).zfill(2), ":", str(sp).zfill(2), " ", str(hk).zfill(2), ":", str(mk).zfill(2), ":", str(sk).zfill(2), sep="")
