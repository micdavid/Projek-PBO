class Barang:
    def __init__(self, idBarang, namaBarang, jenisBarang, hargaBarang, stokBarang):
        self.__idBarang=idBarang
        self.__namaBarang=namaBarang
        self.__jenisBarang=jenisBarang
        self.__hargaBarang=hargaBarang
        self.__stokBarang=stokBarang

    def getIdBarang(self):
        return self.__idBarang

    def setIdBarang(self,idBarang):
        self.__idBarang=idBarang

    def getNamaBarang(self):
        return self.__namaBarang

    def setNamaBarang(self,namaBarang):
        self.__namaBarang=namaBarang

    def getJenisBarang(self):
        return self.__jenisBarang

    def setJenisBarang(self,jenisBarang):
        self.__jenisBarang=jenisBarang

    def getHargaBarang(self):
        return self.__hargaBarang

    def setHargaBarang(self,hargaBarang):
        self.__hargaBarang=hargaBarang

    def getStokBarang(self):
        return self.__stokBarang

    def setStokBarang(self,stokBarang):
        self.__stokBarang=stokBarang
