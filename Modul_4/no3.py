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

#no3
def uangsakuterkecil():
    a = List_mhs[0].uangsaku
    x =[]
    for i in range(len(List_mhs)):
        if a > List_mhs[i].uangsaku:
            a = List_mhs[i].uangsaku
    for i in range(len(List_mhs)):
        if List_mhs[i].uangsaku == a:
            x.append(List_mhs[i].nama)
    return x
