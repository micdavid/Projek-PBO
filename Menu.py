import sqlite3
import Main as Main
from abc import ABC, abstractmethod

ConDb = sqlite3.connect('manajementoko.db')
Cursor = ConDb.cursor()
class Masuk:
    def LoginManager(self):
        pass

    def login_karyawan(self):
        pass

class Login(Masuk):
    def LoginManager(self):
        print("Selamat Datang Koh Manager")
        username = input("Masukkan ID Anda")
        password = input("Masukkan Password Anda")
        query = 'SELECT * from data_manager WHERE username="{}" AND password="{}"'.format(username, password)
        Cursor.execute(query)
        if Cursor.fetchone() is not None:
            print("Berhasil login!! ")
            MenuUtama().MenuManager()
        else:
            print("Maaf anda gagal login")
            Login().LoginManager()

    def LoginKaryawan(self):
        print("Selamat datang gan")
        username=input("Masukkan ID anda ")
        password=input("Masukkan password anda ")
        query='SELECT * from data_karyawan WHERE username="{}" AND password="{}"' .format(username, password)
        Cursor.execute(query)
        if Cursor.fetchone() is not None:
            print("Berhasil login!! ")
            MenuUtama().MenuKaryawan()
        else:
            print("Maaf anda gagal login")
            Login().LoginKaryawan()

class MenuUtama():
    def MenuLogin(self):
        pilihan = int(input('''
        Selamat datang!! Silahkan pilih..
        1. Manager
        2. Karyawan
        '''))
        if pilihan == 1:
            Login().LoginManager()
        elif pilihan == 2:
            Login().LoginKaryawan()
        else :
            print("Maaf Pilihan Tidak Tersedia")
            MenuUtama().MenuLogin()

    def MenuManager(self):
        MenuManager=int(input('''
            Silahkan pilih :
        1. Tambah Data Karyawan
        2. Hapus Data Karyawan
        3. Lihat Data Karyawan
        4. Ubah Data Karyawan
        5. Menu barang
        6. Selesai
        Masukkan Pilihan Menu:
        '''))
        if MenuManager == 1:
            Main.TambahDataKaryawan()
            MenuUtama().MenuManager()
        elif MenuManager == 2:
            Main.HapusDataKaryawan()
            MenuUtama().MenuManager()
        elif MenuManager == 3:
            Main.LihatDataKaryawan()
            MenuUtama().MenuManager()
        elif MenuManager == 4:
            Main.UbahDataKaryawan()
            MenuUtama().MenuManager()
        elif MenuManager == 5:
            MenuUtama().MenuBarangMgr()
        elif MenuManager == 6:
            print("Terima kasih koh")
        else:
            print("Maaf anda salah input ")
            MenuUtama().MenuManager()

    def MenuKaryawan(self):
        MenuKaryawan = int(input(''' 
        Silahkan pilih dari Menu ini :
        1. Lihat profil
        2. Ubah password
        3. Menu barang
        4. Selesai
        '''))
        if MenuKaryawan == 1:
            Main.LihatProfil()
            MenuUtama().MenuKaryawan()
        elif MenuKaryawan == 2:
            Main.UbahPassword()
            MenuUtama().MenuKaryawan()
        elif MenuKaryawan == 3:
            MenuUtama().MenuBarangKry()
        elif MenuKaryawan == 4:
            print("Terima kasih gan")
        else:
            print("Maaf anda salah input ")
            MenuUtama().MenuKaryawan()

    def MenuBarangMgr(self):
        MenuBarangMgr=int(input('''
        Silahkan pilih :
        1. Tambah data barang
        2. Hapus data barang
        3. Lihat data barang
        4. Ubah data barang
        5. Lihat laporan barang
        6. Selesai
        Masukkan Pilihan Menu:
        '''))
        if MenuBarangMgr == 1:
            Main.TambahDataBarang()
            MenuUtama().MenuBarangMgr()
        elif MenuBarangMgr == 2:
            Main.HapusDataBarang()
            MenuUtama().MenuBarangMgr()
        elif MenuBarangMgr == 3:
            Main.LihatDataBarang()
            MenuUtama().MenuBarangMgr()
        elif MenuBarangMgr == 4:
            Main.UbahDataBarang()
            MenuUtama().MenuBarangMgr()
        elif MenuBarangMgr == 5:
            Main.LihatLaporan()
            MenuUtama().MenuBarangMgr()
        elif MenuBarangMgr == 6:
            print("Terima kasih koh")
        else:
            print("Maaf anda salah input ")
            MenuUtama().MenuBarangMgr()

    def MenuBarangKry(self):
        MenuBarangKry = int(input(''' 
        Silahkan pilih dari Menu ini :
        1. Lihat data barang
        2. Cek stok barang
        3. Laporan barang
        4. Selesai
        '''))
        if MenuBarangKry == 1:
            Main.LihatDataBarang()
            MenuUtama().MenuBarangKry()
        elif MenuBarangKry == 2:
            Main.CekBarang()
            MenuUtama().MenuBarangKry()
        elif MenuBarangKry == 3:
            Main.Laporkan()
            MenuUtama().MenuBarangKry()
        elif MenuBarangKry == 4:
            print("Terima kasih gan")
        else:
            print("Maaf anda salah input ")
            MenuUtama().MenuBarangKry()


user1 = MenuUtama()
user1.MenuLogin()