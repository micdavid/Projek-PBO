import sqlite3
import karyawann as karyawan
import barangg as barang
import User as user

ConDb = sqlite3.connect('managementoko.db')
Cursor = ConDb.cursor()

def TambahDataKaryawan():
        Username = input("Masukkan Id karyawan :")
        Password = input("Masukkan password :")
        NamaKaryawan = input("Masukkan Nama :")
        JenisKelamin = input("Masukkan Jenis Kelamin :")
        Tanggal = input("Masukkan Tanggal Lahir (dd-mm-yyyy) :")
        Alamat = input("Masukkan Alamat :")
        Nomor = input("Masukkan Nomor Telphone :")
        query = "INSERT INTO data_karyawan (id_Karyawan, nama_karyawan, password, jenis_kelamin, tanggal_lahir, alamat, no_telphone) VALUES(?, ?, ?, ?, ?, ?, ?)"
        value = (IdKaryawan, Password, NamaKaryawan, JenisKelamin, Tanggal, Alamat, Nomor)
        Cursor.execute(query, value)
        ConDb.commit()
        ConDb.close()
        print("Data Berhasil Ditambahkan")
        MenuKaryawan().MenuAwal()