import User as User

class Karyawan(User.User):
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


    


