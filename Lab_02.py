""" Az első
    kódíró labpr
"""

print("Szia DUE!")
print("Szia", "DUE!", sep="----")
print("\nSzia", "\n\tDUE!", end="")

print("""Ez több
sorba kerül""")

felhasznalo_neve="Jenő"
felhasznalo_kora="20"

print("Szia", felhasznalo_neve, "!")
print(f"Szia {felhasznalo_neve}!")

print("\nNeve: \t{0}, \nKora: \t{1}".format(felhasznalo_neve,felhasznalo_kora))

print(felhasznalo_neve.rjust(30,'.'))
print(str(felhasznalo_kora).rjust(30,'.'))

print(felhasznalo_neve.ljust(30,'.'))
print(str(felhasznalo_kora).ljust(30,'.'))

felhasznalo_nev=input("Hogy hívnak?")
felhasznalo_kor=int(input("Hány éves vagy?"))
print("Szia", felhasznalo_nev)
print("Biztosan", felhasznalo_kor, "vagy?  Nem", felhasznalo_kor + 10, "?")


