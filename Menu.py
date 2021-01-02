import sqlite3
import Manager
import Karyawan
import Connect

class MenuUtama:
    def Menu(self):
        Connect.DataBase()
        pilihan = int(input('''
        Selamat datang!! Silahkan pilih..
        1. Manager
        2. Karyawan
        '''))
        if pilihan == 1:
            Manager.Login().LoginManager()
        elif pilihan == 2:
            Karyawan.Login().login_karyawan()
        else :
            print("Maaf Pilihan Anda Tidak Tersedia")

MenuUtama().Menu()