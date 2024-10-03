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