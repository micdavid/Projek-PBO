import sqlite3
import Barang as Barang
import User as User

ConDb = sqlite3.connect('manajementoko.db')
Cursor = ConDb.cursor()

def TambahDataKaryawan():
    global ConDb
    username = input("Masukkan Id karyawan :")
    password = input("Masukkan password :")
    nama = input("Masukkan Nama :")
    jenis_kelamin = input("Masukkan Jenis Kelamin :")
    tanggal_lahir = input("Masukkan Tanggal Lahir (dd-mm-yyyy) :")
    alamat = input("Masukkan Alamat :")
    telepon = input("Masukkan Nomor Telphone :")
    value = User.Karyawan(username,password,nama,jenis_kelamin,tanggal_lahir,alamat,telepon)
    query = f'INSERT INTO data_karyawan (username, password, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telphone) VALUES ("{value.getUsername()}","{value.getPassword()}","{value.getNama()}","{value.getJeniskelamin()}","{value.getTanggalahir()}","{value.getAlamat()}","{value.getTelepon()}")'
    Cursor.execute(query)
    ConDb.commit()
    print("Data Berhasil Ditambahkan")

def HapusDataKaryawan():
    global ConDb
    username = input("Masukkan Id Karyawan :")
    query = "DELETE FROM data_karyawan WHERE username = ?"
    value = (username,)
    Cursor.execute(query,value)
    ConDb.commit()
    print("Data ", username, " berhasil dihapus")

def LihatDataKaryawan():
    global ConDb
    username = input("Silahkan Masukkan Id karyawan :")
    query = "SELECT * from data_karyawan where username = ?"
    value = (username,)
    Cursor.execute(query, value)
    print (Cursor.fetchall())

def UbahDataKaryawan():
    global ConDb
    username = input("Masukkan Id Karyawan data yang ingin diubah:")
    nama = input("Masukkan Nama :")
    jenis_kelamin = input("Masukkan Jenis Kelamin :")
    tanggal_lahir = input("Masukkan Tanggal (dd-mm-yyyy):")
    alamat = input("Masukkan Alamat :")
    telepon = input("Masukkan Nomor Telphone:")
    value = User.Karyawan(username,"nul",nama,jenis_kelamin,tanggal_lahir,alamat,telepon)    
    Cursor.execute('UPDATE data_karyawan SET nama_karyawan = ?, jenis_kelamin = ?, tanggal_lahir = ?, alamat = ?, no_telphone = ? WHERE username = ?' , (value.getNama(), value.getJeniskelamin(), value.getTanggalahir(), value.getAlamat(), value.getTelepon(), value.getUsername()))
    ConDb.commit()
    print("Data Berhasil Diubah")

def LihatProfil():
    global ConDb
    username = input("Silahkan Masukkan Id anda :")
    query = "SELECT * from data_karyawan where username = ?"
    value = (username,)
    Cursor.execute(query, value)
    print (Cursor.fetchall())

def UbahPassword():
    global ConDb
    username = input("Masukkan Id anda")
    password = input("Masukkan password baru")
    nama = None
    jenis_kelamin = None
    tanggal_lahir = None
    alamat = None
    telepon = None
    value = User.Karyawan(username,password,nama,jenis_kelamin,tanggal_lahir,alamat,telepon)
    Cursor.execute("UPDATE data_karyawan SET password = ? where username = ?" , (value.getPassword(), value.getUsername()))
    ConDb.commit()
    print("Selamat, Password Anda Telah Diubah")

def TambahDataBarang():
    global ConDb
    idBarang = input("Masukkan id barang :")
    namaBarang = input("Masukkan Nama barang:")
    jenisBarang = input("Masukkan Jenis barang :")
    stokBarang = input("Masukkan jumlah stok barang :")
    hargaBarang = input("Masukkan harga barang :")
    value = Barang.Barang(idBarang, namaBarang, jenisBarang, hargaBarang, stokBarang)
    query = f'INSERT INTO data_barang (id_barang, nama_barang, jenis_barang, stok_barang, harga_barang) VALUES ("{value.getIdBarang()}","{value.getNamaBarang()}","{value.getJenisBarang()}","{value.getHargaBarang()}","{value.getStokBarang()}")'
    Cursor.execute(query)
    ConDb.commit()
    print("Data Berhasil Ditambahkan")

def HapusDataBarang():
    global ConDb
    idBarang = input("Masukkan Id barang :")
    query = "DELETE FROM data_barang WHERE id_barang = ?"
    value = (idBarang,)
    Cursor.execute(query,value)
    ConDb.commit()
    print("Data ", idBarang, " berhasil dihapus")

def LihatDataBarang():
    global ConDb
    idBarang = input("Silahkan Masukkan id barang :")
    query = "SELECT * from data_barang where id_barang = ?"
    value = (idBarang,)
    Cursor.execute(query, value)
    print (Cursor.fetchall())

def UbahDataBarang():
    global ConDb
    id_barang = input("Masukkan id barang yang akan diubah :")
    nama_barang = input("Masukkan Nama barang:")
    jenis_barang = input("Masukkan Jenis barang :")
    harga_barang = input("Masukkan harga barang :")
    stok_barang = input("Masukkan jumlah stok barang")
    value = Barang.Barang(id_barang, nama_barang, jenis_barang, harga_barang, stok_barang)     
    Cursor.execute('UPDATE data_barang SET nama_barang = ?, jenis_barang = ?, harga_barang = ?, stok_barang = ? WHERE id_barang = ?' , (value.getNamaBarang(), value.getJenisBarang(), value.getHargaBarang(), value.getStokBarang(), value.getIdBarang()))
    ConDb.commit()
    print("Data Berhasil Diubah")

def CekBarang():
    global ConDb
    query = "SELECT * from data_barang where stok_barang <=2"
    Cursor.execute(query)
    print (Cursor.fetchall())
    print ("Segera laporkan ke Manager! ")

def Laporkan():
    global ConDb
    idBarang = input("Masukkan id barang :")
    username = input("Masukkan id anda : ")
    query = "INSERT INTO data_laporan (id_barang, username) VALUES(?, ?)"
    value = (idBarang, username,)
    Cursor.execute(query,value)
    ConDb.commit()
    print("Data Berhasil Ditambahkan")

def LihatLaporan():
    global ConDb
    Cursor.execute("SELECT * from data_laporan")
    print(Cursor.fetchall())
