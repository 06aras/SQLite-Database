import sqlite3     # Sqlite'yı dahil ediyoruz

import time

class Müzik():

    def __init__(self,şarkı_ismi,sanatçı,albüm,şarkı_türü,şarkı_süresi,):

        self.şarkı_ismi=şarkı_ismi
        self.sanatçı=sanatçı
        self.albüm=albüm
        self.şarkı_türü=şarkı_türü
        self.şarkı_süresi=şarkı_süresi


    def __str__(self):

        return "Şarkı İsmi: {}\nSanatçı: {}\nAlbüm: {}\nTür: {}\nŞarkı Süresi: {}\n".format(self.şarkı_ismi,self.sanatçı,self.albüm,self.şarkı_türü,self.şarkı_süresi)


class Stüdyo():            #Stüdyo class'ını oluşturduk.

    def __init__(self,):

        self.baglanti_olustur()


    def baglanti_olustur(self):       #sqlite veri tabanına bağlanıyoruz.

        self.baglanti = sqlite3.connect("stüdyo.db")    #stüdyo.db veritabanını oluşturup bağlanıyoruz
        self.cursor = self.baglanti.cursor()      # Cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

        bilgi = "Create Table If not exists müzikler (şarkı_ismi TEXT,sanatçı TEXT,albüm TEXT,şarkı_türü TEXT,şarkı_süresi INT)"  # Sorguyu çalıştırıyoruz.

        self.cursor.execute(bilgi)

        self.baglanti.commit()              # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.

    def baglantiyi_kes(self):
        self.baglanti.close()      #Bağlantıyı kapatıyoruz.

    def şarkıları_goster(self):

        bilgi = "Select * From müzikler"

        self.cursor.execute(bilgi)

        müzikler = self.cursor.fetchall()

        if (len(müzikler) == 0):
            print("Stüdyoda şarkı bulunmuyor...")
        else:
            for i in müzikler:
                müzik = Müzik(i[0], i[1], i[2], i[3], i[4])
                print(müzik)

    def şarkı_ekle(self,şarkı):
        bilgi = "Insert into müzikler Values(?,?,?,?,?)"

        self.cursor.execute(bilgi, (şarkı.şarkı_ismi, şarkı.sanatçı, şarkı.albüm, şarkı.şarkı_türü, şarkı.şarkı_süresi))

        self.baglanti.commit()

    def şarkı_sil(self, isim):

        bilgi = "Delete From müzikler where şarkı_ismi = ?"

        self.cursor.execute(bilgi, (isim,))

        self.baglanti.commit()
    def şarkı_süresi(self,):
        self.cursor.execute("Select * From müzikler")
        a=[]

        liste = self.cursor.fetchall()

        for i in liste :
            a.append(i[4])
        print(sum(a))


