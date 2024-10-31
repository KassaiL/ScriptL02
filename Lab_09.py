from tkinter import *
from tkinter import messagebox

def belepes():
    pass

def regisztracio():

    def ok_gomb_kezelese():
        reg_ablak.destroy

    def jelszo_gen():
        pass

    reg_ablak = TK()
    reg_ablak.title("Regisztráció")

    f_nev_cimke = Label(reg_ablak, text="Felhasználó neve(email):")
    f_jelszo_cimke = Label(reg_ablak, text="Jelszó:")
    f_jelszo_cimke2 = Label(reg_ablak, text="Jelszó ismét:")

