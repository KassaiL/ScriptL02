class Jelszo:
    felhasznalo_jelszava = "nincs"

    def __init__(self, felhasznalo_neve = "valami"):
        self.felhasznalo_jelszava = felhasznalo_jelszava

    def jelszo_bekeres(self, hosszusag):
        def hossz(_jelszo, min_hossz):
            ok = True
            if _jelszo < min_hossz:
                ok = False
            return ok

        def szamjegyek(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isnumeric():
                    ok = True
                    break
            return ok

        def kisbetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.islower():
                    ok = True
                    break
            return ok

        def nagybetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isupper():
                    ok = True
                    break
            return ok

        jelszo = input("Kérem a jelszót!")
        while not hossz(jelszo, hosszusag) or not szamjegyek(jelszo) or not kisbetu(jelszo) or not nagybetu(
                jelszo) or " " in jelszo:
            print("Nem megfelelő jelszó!")
            jelszo = input("Kérem a jelszót!")
        self.felhasznalo_jelszava = felh_jelszo

    def Jelszo_generalas (self, hossz = 8, kisbetu = True, nagybetu = True, szam = True):
        import string
        import random
        jelszo = ""
        karaktersor = ""
        if kisbetu:
            karaktersor = string.ascii_lowercase
        if nagybetu:
            karaktersor = string.ascii_uppercase
        if szam:
            karaktersor = string.digits
        for _ in range(hossz):
            jelszo = jelszo + karaktersor[random.randint(0, len(karaktersor)-1)]
        self.felhasznalo_jelszava = jelszo

    def jelszo_ellenorzes(self):
        ok = False
        proba = 0
        while True:
            jelszo2 = input("Kérem ismét a jelszót: ")
            if self.felhasznalo_jelszava == jelszo2:
                ok = True
                break
            else:
                proba += 1
                print("Nem megfelelő a jelszó!")
                if proba == 3:
                    break
        return ok

class Felhasznalo(Jelszo):
    felhasznalo_neve = "Valaki"

    def __init__(self, felhasznalo_jelszava = "ÚJjelszó1"):
    super(),__init__(felhasznalo_jelszava)

    def felhasznalonev(self):
        _felhasznalo_neve = input("Kérem a felhasználó nevet (Email): ")
        while " " in _felhasznalo_neve or "@" not in _felhasznalo_neve or "." not in _felhasznalo_neve:
            print("Érvénytelen az email formátum!")
            if " " in _felhasznalo_neve:
                print("Szóközt használt az emailben.")
            elif "@" not in _felhasznalo_neve:
                print("Nincs benne (@)")
            else:
                print("Nincs benn (.)'")
            _felhasznalo_neve = input("Kérem a felhasználó nevet (Email): ")
        return self.felhasznalo_neve = _felhasznalo_neve

    def rogzites(self):
        with open("Dolgozok.txt", "a", encoding="utf-8") as fajl:
            fajl.write(self.felhasznalo_neve + ";" + self.felhasznalo_jelszava + "\n")

dolgozo = Felhasznalo("JElszo1")
print(dolgozo.felhasznalo_neve)
print(dolgozo.felhasznalo_jelszava)
