def regisztracio():
    def felhasznalonev():
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
            return _felhasznalo_neve

    def jelszo_bekeres(hosszusag):
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
        while not hossz(jelszo, hosszusag) or not szamjegyek(jelszo) or not kisbetu(jelszo) or not  nagybetu(jelszo) or " " in jelszo:
            print("Nem megfelelő jelszó!")
            jelszo = input("Kérem a jelszót!")

    def rogzites(email, jelszo):
        with open("Dolgozok.txt", "a", encoding="utf-8") as fajl:
            fajl.write(email + ";" + jelszo + "\n")

    felhasznalo_neve = felhasznalonev()
    felhasznalo_jelszo = jelszo_bekeres(10)
    ok = jelszo_ellenorzes(felhasznalo_jelszo)
    if ok:
        rogzites(felhasznalo_neve,felhasznalo_jelszo)
    return ok

def jelszo_ellenorzes(jelszo):
    ok = False
    proba = 0
    while True:
        jelszo2 = input("Kérem ismét a jelszót: ")
        if jelszo == jelszo2:
                ok = True
                break
        else:
            proba += 1
            print("Nem megfelelő a jelszó!")
            if proba == 3:
                break
    return ok

def beleptetes():
    def felhasznalo():
        email = input("Felhasználó neve:")
        with open("Dolgozok.txt", "r", encoding="utf-8") as fajl:
            for sor in fajl:
                felhasznaloi_adatok = sor.strip().split(";")
                if felhasznaloi_adatok[0] == email:
                    jelszo = felhasznaloi_adatok[1]
                    break
        return jelszo

    def jelszoellenorzes(_jelszo):
        ok = False
        jelszo2 = input()
        if jelszo_ellenorzes(jelszo2):
            ok = True
        return ok

    jelszo = felhasznalo()
    if not jelszo:
        print("Nem vagy regisztrált felhasználó!")
    else:
        if jelszoellenorzes(jelszo):
            print("Beléphetsz")
        else:
            print("Megtagadjuk a belépést!")