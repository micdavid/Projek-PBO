import sqlite3
import Connect
import getpass

class MenuKaryawan(Connect.DataBase):
    def MenuAwal(self):
        Connect.DataBase()
        MenuAwal=int(input('''
            Silahkan pilih :
        1. Tambah Data Karyawan
        2. Hapus Data Karyawan
        3. Pilih Data Karyawan
        4. Update Data Karyawan
        5. Menu barang
        6. Selesai
        Masukkan Pilihan Menu:
        '''))
        if MenuAwal == 1:
            MenuKaryawan().TambahDataKaryawan()
        elif MenuAwal == 2:
            MenuKaryawan().HapusDataKaryawan()
        elif MenuAwal == 3:
            MenuKaryawan().PilihDataKaryawan()
        elif MenuAwal == 4:
            MenuKaryawan().UpdateDataKaryawan()
        elif MenuAwal == 5:
            MenuBarang().MenuAkhir()
        elif MenuAwal == 6:
            print("Terima kasih koh")
        else:
            Login().LoginManager()

    def TambahDataKaryawan(self):
        IdKaryawan = input("Masukkan Id karyawan :")
        Password = input("Masukkan password :")
        NamaKaryawan = input("Masukkan Nama :")
        JenisKelamin = input("Masukkan Jenis Kelamin :")
        Tanggal = input("Masukkan Tanggal Lahir (dd-mm-yyyy) :")
        Alamat = input("Masukkan Alamat :")
        Nomor = input("Masukkan Nomor Telphone :")
        query = "INSERT INTO data_karyawan (id_Karyawan, nama_karyawan, password, jenis_kelamin, tanggal_lahir, alamat, no_telphone) VALUES(?, ?, ?, ?, ?, ?)"
        value = (IdKaryawan, Password, NamaKaryawan, JenisKelamin, Tanggal, Alamat, Nomor)
        self.Cursor.execute(query, value)
        self.ConDb.commit()
        self.ConDb.close()
        print("Data Berhasil Ditambahkan")
        MenuKaryawan().MenuAwal()

    def HapusDataKaryawan(self):
        DataHapus = input("Masukkan Id Karyawan :")
        query = "DELETE FROM data_karyawan WHERE id_Karyawan = ?"
        value = (DataHapus,)
        self.Cursor.execute(query, value)
        self.ConDb.commit()
        self.ConDb.close()
        print("Data ", DataHapus, " berhasil dihapus")
        MenuKaryawan().MenuAwal()

    def PilihDataKaryawan(self):
        Cari = input("Silahkan Masukkan Id karyawan :")
        query = "SELECT * from data_karyawan where id_Karyawan = ?"
        value = (Cari,)
        self.Cursor.execute(query, value)
        print (self.Cursor.fetchall())
        self.ConDb.close()
        MenuKaryawan().MenuAwal()

    def UpdateDataKaryawan(self):
        IdKaryawan = input("Masukkan Id Karyawan data yang ingin diubah:")
        NamaKaryawan = input("Masukkan Nama :")
        JenisKelamin = input("Masukkan Jenis Kelamin :")
        Tanggal = input("Masukkan Tanggal (dd-mm-yyyy):")
        Alamat = input("Masukkan Alamat :")
        Nomor = input("Masukkan Nomor Telphone:")
        query = "UPDATE data_karyawan SET nama_karyawan = ?, jenis_kelamin = ?, tanggal_lahir = ?, alamat = ?, no_telphone = ? WHERE id_Karyawan = ?"       
        value = (NamaKaryawan, JenisKelamin, Tanggal, Alamat, Nomor, IdKaryawan)
        self.Cursor.execute(query, value)
        self.ConDb.commit()
        self.ConDb.close()
        print("Data Berhasil Diubah")
        MenuKaryawan().MenuAwal()

class MenuBarang(Connect.DataBase):
    def MenuAkhir(self):
        Connect.DataBase()
        MenuAkhir=int(input('''
            Silahkan pilih :
        1. Tambah data barang
        2. Hapus data barang
        3. Pilih data barang
        4. Update data barang
        5. Lihat laporan barang
        6. Selesai
        Masukkan Pilihan Menu:
        '''))
        if MenuAkhir == 1:
            MenuBarang().TambahDataBarang()
        elif MenuAkhir == 2:
            MenuBarang().HapusDataBarang()
        elif MenuAkhir == 3:
            MenuBarang().PilihDataBarang()
        elif MenuAkhir == 4:
            MenuBarang().UpdateDataBarang()
        elif MenuAkhir == 5:
            MenuBarang().lihat_laporan()
        elif MenuAkhir == 6:
            print("Terima kasih koh")
        else:
            Login().LoginManager
    
    def TambahDataBarang(self):
        IdBarang = input("Masukkan id barang :")
        NamaBarang = input("Masukkan Nama barang:")
        JenisBarang = input("Masukkan Jenis barang :")
        StokBarang = input("Masukkan jumlah stok barang :")
        HargaBarang = input("Masukkan harga barang :")
        query = "INSERT INTO data_barang (id_barang, nama_barang, jenis_barang, stok_barang, harga_barang) VALUES(?, ?, ?, ?, ?)"
        value = (IdBarang, NamaBarang, JenisBarang, StokBarang, HargaBarang)
        self.Cursor.execute(query, value)
        self.ConDb.commit()
        self.ConDb.close()
        print("Data Berhasil Ditambahkan")
        MenuBarang().MenuAkhir()

    def HapusDataBarang(self):
        Connect.DataBase
        DataHapus = input("Masukkan Id barang :")
        query = "DELETE FROM data_barang WHERE id_barang = ?"
        value = (DataHapus,)
        self.Cursor.execute(query, value)
        self.ConDb.commit()
        self.ConDb.close()
        print("Data ", DataHapus, " berhasil dihapus")
        MenuBarang().MenuAkhir()

    def PilihDataBarang(self):
        Connect.DataBase
        Cari = input("Silahkan Masukkan id barang :")
        query = "SELECT * from data_barang where id_barang = ?"
        value = (Cari,)
        self.Cursor.execute(query, value)
        print (self.Cursor.fetchall())
        self.ConDb.close()
        MenuBarang().MenuAkhir()

    def UpdateDataBarang(self):
        Connect.DataBase
        IdBarang = input("Masukkan id barang :")
        NamaBarang = input("Masukkan Nama barang:")
        JenisBarang = input("Masukkan Jenis barang :")
        StokBarang = input("Masukkan jumlah stok barang")
        HargaBarang = input("Masukkan harga barang :")
        query = "UPDATE data_barang SET nama_barang = ?, jenis_barang = ?, stok_barang = ?, harga_barang = ? WHERE id_barang = ?"       
        value = (NamaBarang, JenisBarang, StokBarang, HargaBarang, IdBarang)
        self.Cursor.execute(query, value)
        self.ConDb.commit()
        self.ConDb.close()
        print("Data Berhasil Diubah")
        MenuBarang().MenuAkhir()

    def lihat_laporan(self):
        Connect.DataBase
        self.Cursor.execute("SELECT * from data_laporan")
        print(self.Cursor.fetchall())
        self.ConDb.close()
        MenuBarang().MenuAkhir()


class Login(Connect.DataBase):
    def LoginManager(self):
        Connect.DataBase()
        print("Selamat Datang Koh Manager")
        Username = input("Masukkan ID Anda")
        Password = getpass.getpass("Masukkan password :")
        query = 'SELECT * from data_manager WHERE id_manager="{}" AND password="{}"'.format(Username, Password)
        self.Cursor.execute(query)
        if self.Cursor.fetchone() is not None:
            print("Berhasil login!! ")
            MenuKaryawan().MenuAwal()
        else:
            print("Maaf anda gagal login")
            Login().LoginManager()
        self.ConDb.close()
