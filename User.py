class User:
    def __init__(self, username, password):
        self.__username=username
        self.__password=password

    def getUsername(self):
        return self.__username

    def setUsername(self,username):
        self.__username=username

    def getPassword(self):
        return self.__password

    def setPassword(self,password):
        self.__password=password

class Manager(User):
    def __init__(self, username, password, nama):
        super().__init__(username, password)
        self.__nama=nama

    def getNama(self):
        return self.__nama
        
class Karyawan(User):
    def __init__(self, username, password, nama, jenis_kelamin, tanggal_lahir, alamat, telepon):
        super().__init__(username, password)
        self.__nama=nama
        self.__jenis_kelamin=jenis_kelamin
        self.__tanggal_lahir=tanggal_lahir
        self.__alamat=alamat
        self.__telepon=telepon

    def getNama(self):
        return self.__nama

    def setNama(self,nama):
        self.__nama=nama

    def getJeniskelamin(self):
        return self.__jenis_kelamin

    def setJeniskelamin(self,jenis_kelamin):
        self.__jenis_kelamin=jenis_kelamin

    def getTanggalahir(self):
        return self.__tanggal_lahir

    def setTanggalahir(self,tanggal_lahir):
        self.__tanggal_lahir=tanggal_lahir

    def getAlamat(self):
        return self.__alamat

    def setAlamat(self,alamat):
        self.__alamat=alamat

    def getTelepon(self):
        return self.__telepon

    def setTelepon(self,telepon):
        self.__telepon=telepon