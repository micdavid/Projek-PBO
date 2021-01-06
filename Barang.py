class Barang:
    def __init__(self, id_barang, nama_barang, jenis_barang, harga_barang, stok_barang):
        self.__id_barang=id_barang
        self.__nama_barang=nama_barang
        self.__jenis_barang=jenis_barang
        self.__harga_barang=harga_barang
        self.__stok_barang=stok_barang

    def getIdBarang(self):
        return self.__id_barang

    def setIdBarang(self,id_barang):
        self.__id_barang=id_barang

    def getNamaBarang(self):
        return self.__nama_barang

    def setNamaBarang(self,nama_barang):
        self.__nama_barang=nama_barang

    def getJenisBarang(self):
        return self.__jenis_barang

    def setJenisBarang(self,jenis_barang):
        self.__jenis_barang=jenis_barang

    def getHargaBarang(self):
        return self.__harga_barang

    def setHargaBarang(self,harga_barang):
        self.__harga_barang=harga_barang

    def getStokBarang(self):
        return self.__stok_barang

    def setStokBarang(self,stok_barang):
        self.__stok_barang=stok_barang
