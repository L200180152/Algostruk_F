class mahasiswa(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uangsaku = uangsaku

a1 = mahasiswa("Andi", 11, "Lampung", 300000)
a2 = mahasiswa("Banu", 10, "Karanganyar", 230000)
a3 = mahasiswa("Izzah", 15, "Jakarta", 450000)
a4 = mahasiswa("Iqbal", 80, "Wonogiri", 275000)
a5 = mahasiswa("Aji", 50, "Karanganyar", 245000)
a6 = mahasiswa("Aziz", 43, "Sragen", 235000)
a7 = mahasiswa("Rizky", 23, "Palu", 255000)
a8 = mahasiswa("Irvan", 65, "Klaten", 210000)
a9 = mahasiswa("Brian", 76, "Klaten", 220000)
a10 = mahasiswa("Fais", 20, "Jepara", 225000)

List_mhs = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

#no7
def binsemass(kumpulan, target):
    temp = []
    low = 0
    high = len(kumpulan)-1
    while low <= high :
        mid = (high+low)//2
        if kumpulan[mid] == target:
            midkiri = mid-1
            while kumpulan[midkiri] == target:
                temp.append(midkiri)
                midkiri = midkiri -1
            temp.append(mid)
            midkanan = mid+1
            while kumpulan[midkanan] == target:
                temp.append(midkanan)
                midkanan = midkanan+1
            return temp
        elif target < kumpulan[mid]:
            high = mid-1
        else:
            low = mid+1
    return False
