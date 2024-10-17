class Jelszo:
    felhasznalo_jelszava = ""

    def Jelszo_bekeres (self):
        pass
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

felh_jelszo = Jelszo()
print(felh_jelszo.felhasznalo_jelszava)
felh_jelszo.Jelszo_generalas()
print(felh_jelszo.felhasznalo_jelszava)
