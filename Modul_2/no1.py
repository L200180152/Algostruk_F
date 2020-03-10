class pesan(object):
    """
        Sebuah class bernama pesan,
        untuk memahami konsep class dan object.
    """
    def __init__(self, sebuahstring):
        self.teks = sebuahstring
    def cetakini(self):
        print(self.teks)
    def cetakpakaihurufkapital(self):
        print(str.upper(self.teks))
    def cetakpakaihurufkecil(self):
        print(str.lower(self.teks))
    def jumkar(self):
        return len(self.teks)
    def cetakjumlahkarakterku(self):
        print('kalimatku mempunyai', len(self.teks), 'karakter')
    def perbarui(self, stringbaru):
        self.teks = stringbaru

#a
    def apakahterkandung(self):
        if kata in self.teks:
            return True
        else:
            return False

#b
    def hitungkonsonan(self):
        konsonan = ['b','c','d','f','g','h','j','k','l','m','n','p','q'
                    ,'r','s','t','v','w','x','y','z','B','C','D','F','G','H'
                    ,'J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']

        hurufk = self.teks
        jumkonsonan = 0
        for i in hurufk:
            if i in konsonan:
                jumkonsonan+=1
        return jumkonsonan

#c
    
    def hitungvokal(self):
        vokal = ['a','i','u','e','o','A','I','U','E','O']

        hurufv = self.teks
        jumvokal = 0
        for i in hurufv:
            if i in vokal:
                jumvokal+=1
        return jumvokal

psn1 = pesan("surakarta")
