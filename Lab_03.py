print("Jövedelemszámítás\n")
brutto = int(input("Kérem a bruttó jövedelmét: "))
kor = int(input("Hány éves vagy: "))

if kor < 25:
    if brutto < 599790:
        szja = 0
    else:
        szja = (brutto - 599790) * 0.15
else:
    szja = brutto * 0.15
nyugdij = brutto *0.1
tb = brutto * 0.07
munkanelkuli = 0.015
netto = brutto- szja - nyugdij - tb - munkanelkuli

print("Jövedelem".center(50))
print("Bruttó jövedelem:".ljust(25,"_"), str(brutto).rjust(25,"_"))
print("SZJA:".ljust(25,"_"), str(szja).rjust(25,"_"))
print("Nyugdíj:".ljust(25,"_"), str(nyugdij).rjust(25,"_"))
print("TB:".ljust(25,"_"), str(tb).rjust(25,"_"))
print("Munkanélküli:".ljust(25,"_"), str(munkanelkuli).rjust(25,"_"))
print("Nettó jövedelem:".ljust(25,"_"), str(netto).rjust(25,"_"))

print("Számológép")
muvelet = input("Milyen műveletet szeretne végrehajtani (+,-,*,/):")
if muvelet not in ("+","-","*","/"):
    print("Nem jó műveletet adott meg:")
    exit()
else:
    szam1= int(input("Adj meg egy számot:"))
    szam2 = int(input("Adja meg még egy számot:"))
    if muvelet in ("+"):
        eredm = szam1 + szam2
        print("A művelet: ",szam1," + ",szam2," = ",eredm)
    elif muvelet in ("-"):
        eredm = szam1 - szam2
        print("A művelet: ",szam1," - ",szam2," = ",eredm)
    elif muvelet in ("*"):
        eredm = szam1 * szam2
        print("A művelet: ",szam1," * ",szam2," = ",eredm)
    else:
        eredm = szam1 / szam2
        print("A művelet: ", szam1, " / ", szam2, " = ", eredm)
