import sqlite3
import Connect
import getpass

class Karyawan(Connect.DataBase):
    def menu_karyawan(self,id_karyawan):
        Connect.DataBase()
        menu_karyawan = int(input(''' 
        Silahkan pilih dari Menu ini :
        1. Lihat profil
        2. Ubah password
        3. Menu barang
        4. Selesai
        '''))
        if menu_karyawan == 1:
            Karyawan().profil(id_karyawan)
        elif menu_karyawan == 2:
            Karyawan().ubah_password(id_karyawan)
        elif menu_karyawan == 3:
            MenuBarang().menu_barang()
        elif menu_karyawan == 4:
            print("Terima kasih gan")
        else:
            Login().login_karyawan()

    def profil(self,id_karyawan):
        Connect.DataBase
        query="SELECT * from data_karyawan where id_karyawan = ?"
        value=(id_karyawan,)
        self.Cursor.execute(query,value)
        print(self.Cursor.fetchall())
        self.ConDb.close()
        Karyawan().menu_karyawan(id_karyawan)

    def ubah_password(self,id_karyawan):
        Connect.DataBase 
        npw = input("Masukkan password baru")
        query = "UPDATE data_karyawan SET password = ? where id_karyawan = ?"
        value = (npw, id_karyawan)
        self.Cursor.execute(query, value)
        self.ConDb.commit()
        self.ConDb.close()
        print("Selamat, Password Anda Telah Diubah")
        Karyawan().menu_karyawan(id_karyawan)


class MenuBarang(Connect.DataBase):
    def menu_barang(self):
        Connect.DataBase()
        menu_barang = int(input(''' 
        Silahkan pilih dari Menu ini :
        1. Lihat data barang
        2. Cek stok barang
        3. Laporan barang
        4. Selesai
        '''))
        if menu_barang == 1:
            MenuBarang().lihat_barang()
        elif menu_barang == 2:
            MenuBarang().cek_barang()
        elif menu_barang == 3:
            MenuBarang().laporkan()
        elif menu_barang == 4:
            print("Terima kasih gan")
        else:
            MenuBarang().menu_barang()

    def lihat_barang(self):
        Connect.DataBase
        Cari = input("Silahkan Masukkan id barang :")
        query = "SELECT * from data_barang where id_barang = ?"
        Data = (Cari,)
        self.Cursor.execute(query, Data)
        print (self.Cursor.fetchall())
        self.ConDb.close()
        MenuBarang().menu_barang()

    def cek_barang(self):
        Connect.DataBase
        query = "SELECT * from data_barang where stok_barang <=2"
        self.Cursor.execute(query)
        print (self.Cursor.fetchall())
        print ("Segera laporkan ke Manager! ")
        self.ConDb.close()
        MenuBarang().menu_barang()

    def laporkan(self):
        IdBarang = input("Masukkan id barang :")
        IdKaryawan = input("Masukkan id anda")
        query = "INSERT INTO data_laporan (id_barang, id_karyawan) VALUES(?, ?)"
        Data = (IdBarang, IdKaryawan)
        self.Cursor.execute(query, Data)
        self.ConDb.commit()
        self.ConDb.close()
        print("Data Berhasil Ditambahkan")
        MenuBarang().menu_barang()


class Login(Connect.DataBase):
    def login_karyawan(self):
        Connect.DataBase()
        print("Selamat datang gan")
        username=input("Masukkan ID anda ")
        password=getpass.getpass("Masukkan password anda ")
        unpw='SELECT * from data_karyawan WHERE id_karyawan="{}" AND password="{}"' .format(username, password)
        self.Cursor.execute(unpw)
        if self.Cursor.fetchone() is not None:
            print("Berhasil login!! ")
            Karyawan().menu_karyawan(username)
        else:
            print("Maaf anda gagal login")
            Login().login_karyawan()
        self.ConDb.close()