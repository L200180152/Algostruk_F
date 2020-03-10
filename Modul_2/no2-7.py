#No 2  
class Manusia(object) :
    keadaan = "Lapar"
    def __init__(self, nama) :
        self.nama = nama
        
    def ucapkanSalam(self) :
        print("Salam, namaku", self.nama)
        
    def makan(self, s):
        print("Saya baru aja makan", a)
        self.keadaan = "Kenyang"
        
    def olahraga(self, k) :
        print("Saya baru saja latihan", k)
        self.keadaan = "Lapar"

class Mahasiswa(Manusia) :
    def __init__(self,nama,NIM,kota,us) :
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        
    def __str__(self) :
        s = self.nama + ", NIM "+ str(self.NIM) + ", Tinggal di " + self.kotaTinggal + ", Uang saku Rp "+ str(self.uangSaku)+" tiap bulannya."
        return s

    def ambilNama(self):
        return self.nama
    
    def ambilNIM(self):
        return self.NIM
    
    #(a)
    def ambilKotaTinggal(self) :
        return self.kotaTinggal

    #(b)
    def perbaruiKotaTinggal(self, kotaBaru) :
        self.kotaTinggal = kotaBaru

    #(c)
    def ambilUangSaku(self):
        return self.uangSaku

    def tambahUangSaku(self, tambahUS) :
        self.uangSaku = tambahUS

    def makan(self,s):
        print("Saya baru saja makan",s,"sambil belajar.")
        self.keadaan = "Kenyang"
#No 4
    listKuliah=[]
    def tambahMakul(self, makul) :
        self.listKuliah.append(makul)
        
#No 5
    def hapusMakul(self, makul) :
        self.listKuliah.remove(makul)
        
#No 6        
class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, uangSaku, alamat):
        self.nama = nama
        self.nisn = NISN
        self.uangSaku = uangSaku
        self.alamat = alamat
        
    def __str__(self):
        a = 'Nama      : ' + str(self.nama) \
            +'NISN      : ' + str(self.nisn) \
            +'Alamat    : ' + str(self.alamat) \
            +'Uang Saku : ' + str(self.uangSaku)
        return a
    
    def ambilNama(self):
        return self.nama
    
    def ambilNisn(self):
        return self.nisn
    
    def ambilUangSaku(self):
        return self.uangSaku

    def ambilKotaTinggal(self):
        return self.kotaTinggal

    def perbaruiKotaTinggal(self,stringbaru):
        self.kotaTinggal = stringbaru

    def tambahUangSaku(self,tambah):
        self.uangSaku += tambah
        
#No 7
#
#Metode dan  state yang tampak di object itu berasal dari semua class, dari Manusia, Mahasiswa, atau MhsTIF.
#Ini adalah konsep pewarisan. MhsTIF mewarisi sifat Manusia dan Mahasiswa
#Karena MhsTIF adalah anak kelas dari Mahasiswa dan Mahasiswa adalah anak kelas Manusia
#

#No 3
a = input("Masukkan Nama      : ")
b = input("Masukkan NIM       : ")
c = input("Masukkan Kota      : ")
d = input("Masukkan Uang Saku : ")

m1 = Mahasiswa(a,b,c,d)
print(m1)

