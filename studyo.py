from Kütüphane import *  #Daha öncesinde kodlamış olduğumuz kütüphane modülümüzü çağırıyoruz.

print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Şarkıları Göster

2. Şarkı Ekle

3. Şarkı Sil

4. Şarkıların Toplam Süresi

Çıkmak için 'q' ya basın.
***********************************""")
stüdyo=Stüdyo()

while True :
    işlem=input("İşleminizi Seçiniz :")

    if (işlem == "q"):
        print("Program Sonlandırılıyor.....")
        print("Yine bekleriz....")
        break
    elif (işlem=="1"):
        stüdyo.şarkıları_goster()
    elif(işlem=="2"):
        şarkı_ismi=input("Şarkı İsmini Giriniz :")
        sanatçı=input("Sanatçı İsmini Giriniz :")
        albüm=input("Albüm İsmini Giriniz :")
        şarkı_türü=input("Şarkı TürünüGiriniz :")
        şarkı_süresi=input("Şarkı Süresini Giriniz :")

        yeni_şarkı=Müzik(şarkı_ismi,sanatçı,albüm, şarkı_türü,şarkı_süresi)

        print("Şarkı Ekleniyor...")
        time.sleep(2)
        print("Şarkı Eklendi.")

        stüdyo.şarkı_ekle(yeni_şarkı)

    elif (işlem=="3"):
        şarkı=input("Hangi Şarkıyı Silmek İstiyorsunuz? :")

        cevap=input("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print("Şarkı Siliniyor...")
            time.sleep(2)
            stüdyo.şarkı_sil(şarkı)
            print("Şarkı Silindi silindi....")
        else :
            print("İşlem iptal Edildi.")
            break
    elif (işlem=="4"):
        stüdyo.şarkı_süresi()
        
        
        
