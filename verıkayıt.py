import re
import time
from re import search
from time import sleep
class Kayıt:
    def __init__(self,programad):
        self.programad = programad
        self.dongu = True
    def program(self):
        secım = self.menu()
        if secım=="1":
            print("Kayıt Ekleme Menüsüne Yönlendiriliyorsunuz...!")
            time.sleep(1)
            self.kayıtekle()
        elif secım=="2":
            print("Kayıt Silme Menüsüne Yönlendiriliyorsunuz...!")
            time.sleep(1)
            self.kayıtcıkar()
        elif secım=="3":
            print("Kayıtlara Erişiliyor...!")
            time.sleep(1)
            self.kayıtoku()
        else :
            self.cıkıs()
    def menu(self):
        def kontrol(secım):
            if re.search("[^1-4]",secım):
                raise Exception("Lütfen 1 ile 4 arasında bir sayı giriniz...!")
            elif len(secım)!=1:
                raise Exception("Lütfen 1 ile 4 arasında bir sayı giriniz...!")
        while True:
            try:
                secım= input("Merhabalar, {} Otomasyon Sistemine Hoşgeldiniz\nLütfen Yapmak istediğiniz İşlemi Seçiniz...\n\n[1] Kayıt Ekle\n[2] Kayıt Sil\n[3] Kayıt Okuma\n[4] Çıkış\n".format(self.programad))
                kontrol(secım)
            except Exception as Hata:
                print(Hata)
                time.sleep(3)
            else:
                break
        return secım
    def kayıtekle(self):
        def Kontrolad(ad):
            if ad.isalpha()== False:
                raise Exception("Ad Sadece harflarden oluşmalıdır...!")
        while True:
            try:
                ad= input("Adınız: ")
                Kontrolad(ad)
            except Exception as hataad:
                print(hataad)
                time.sleep(1)
            else:
                break
        def Kontrolsoyaad(soyad):
            if soyad.isalpha()== False:
                raise Exception("Soyad Sadece harflarden oluşmalıdır...!")
        while True:
            try:
                soyad= input("Soyadınız: ")
                Kontrolsoyaad(soyad)
            except Exception as hatasoyad:
                print(hatasoyad)
                time.sleep(1)
            else:
                break
        def Kontrolyas(yas):
            if yas.isdigit()== False:
                raise Exception("Yaş sadece rakamlardan oluşmalıdır...!")
        while True:
            try:
                yas= input("Yaşınız: ")
                Kontrolyas(yas)
            except Exception as hatayas:
                print(hatayas)
                time.sleep(1)
            else:
                break
        def Kontroltc(tc):
            if tc.isdigit()== False:
                raise Exception("TC  sadece rakamlardan oluşmalıdır...!")
            if len(tc)!=11:
                raise Exception("TC 11 rakamdan oluşmalıdır...!")
        while True:
            try:
                tc= input("TC numaranız: ")
                Kontroltc(tc)
            except Exception as hatatc:
                print(hatatc)
                time.sleep(1)
            else:
                break
        def Kontrolmail(mail):
            if not ((re.search('@'  , mail)) and  (re.search(".com", mail))):
                raise Exception("Geçerli bir mail adresi giriniz...!")
        while True:
            try:
                mail= input("Mail adresiniz: ")
                Kontrolmail(mail)
            except Exception as hatamail:
                print(hatamail)
                time.sleep(1)
            else:
                break
        with open("C:/Users/erenk/Desktop/BİLGİLER.txt", "r", encoding="utf-8") as Dosya:
            satırsayısı= Dosya.readlines()
        if len(satırsayısı)==0:
            Id=1
        else:
            with open("C:/Users/erenk/Desktop/BİLGİLER.txt", "r", encoding="utf-8") as Dosya:
                Id=int(Dosya.readlines()[-1].split("-")[0])+1
        with open("C:/Users/erenk/Desktop/BİLGİLER.txt", "a+", encoding="utf-8") as Dosya:
            print("Veriler İşleniyor...!")
            time.sleep(3)
            Dosya.write("{}-{} {} {} {} {}\n".format(Id,ad,soyad,yas,tc,mail))
            print("Veriler İşlendi...!")
        self.menudon()
    def kayıtcıkar(self):
        y= input("Lütfen Silmek İstediğiniz Kişinin Id Numarasını Giriniz...:")
        with open("C:/Users/erenk/Desktop/BİLGİLER.txt", "r", encoding="utf-8") as Dosya:
            liste= []
            liste2= Dosya.readlines()
            for i in range(0,len(liste2)):
                liste.append(liste2[i].split("-")[0])
        del liste2[liste.index(y)]
        with open("C:/Users/erenk/Desktop/BİLGİLER.txt", "w+", encoding="utf-8") as YeniDosya:
            for i in liste2:
                YeniDosya.write(i)
        print("Kayıt Siliniyor...!")
        time.sleep(1)
        print("Kayıt Silinmiştir...!")
        self.menudon()
    def kayıtoku(self):
        with open("C:/Users/erenk/Desktop/BİLGİLER.txt", "r", encoding="utf-8") as Dosya:
            for i in Dosya:
                print(i)
        self.menudon()
    def cıkıs(self):
        print("Otomasyondan çıkılıyor...!")
        time.sleep(1)
        self.dongu = False
    def menudon(self):
        while True:
            x = input("Ana menüye dönmek istiyorsanız 6'ya, Çıkış için 7'ye basınız...!\n")
            if x=="6":
                print("Ana menüye dönülüyor...!")
                time.sleep(1)
                self.program()
                break
            elif x=="7":
                self.cıkıs()
                break
            else:
                print("Lütfen geçerli bir rakam giriniz")
Sistem = Kayıt("EREN")
while Sistem.dongu:
    Sistem.program()

















