import time

from Kutuphane import *

print("""**********************************


Kutuphane Programina Hosgeldiniz

Islemler;

1. Kitaplari Goster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil

5. Baski Yukselt

Cikmak icin 'q' ya basin

*******************************
""")

kutuphane = Kutuphane()
while True:
    islem = input("Yapacaginiz Islem: ")

    if islem.upper() == "Q":
        print("Program Sonlandiriliyor......")
        time.sleep(1)
        print("Yine Bekleriz")
        break
    elif islem == "1":
        kutuphane.kitaplari_goster()

    elif islem == "2":
        isim = input("Hangi kitabi gormek istiyorsunuz? ")
        print("Kitap sorgulaniyor....")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)
    elif islem == "3":
        isim = input("Isim: ")
        yazar = input("Yazar: ")
        yayinevi = input("Yayinevi: ")
        tur = input("Tur: ")
        baski = int(input("Baski: "))

        yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski)

        print("Kitap Ekleniyor....")
        time.sleep(1)

        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap Eklendi...")

    elif islem == "4":
        isim = input("Hangi Kitabi silmek istiyorsun? ")

        cevap = input("Emin misiniz ?  (E/H)")
        if cevap == "E":
            print("Kitap Siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap Silindi")
        elif (cevap == "H"):
            continue
        else:
            pass

    elif islem == "5":
        isim = input("Hangi kitabin baskisini yukseltmek istiyorsunuz? ")
        print("Baski Yukseltiliyor....")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baski Yukseltildi....")
    else:
        print("Gecersiz Islem")
