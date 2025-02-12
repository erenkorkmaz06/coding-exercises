import math
import re
import time
class calculator:
    def __init__(self):
        self.dongu= True
    def program(self):
        secım=self.menu()
        if secım=="1":
            self.toplama()
        elif secım == "2":
            self.cıkarma()
        elif secım == "3":
            self.carpma()
        elif secım == "4":
            self.bolme()
        elif secım == "5":
            self.usalma()
        elif secım == "6":
            self.kokalma()
        else:
            self.cıkıs()
    def menu(self):
        def kontrol(secım):
            if re.search("[^1-7]",secım):
                raise Exception("Lütfen Geçerli Bir İşlem Seçiniz..!")
            elif len(secım)!=1:
                raise Exception("Lütfen Geçerli Bir İşlem Seçiniz..!")
        while True:
            try:
                secım= input("Hesap Makinesine Hoşgeldiniz...\nLütfen Bir İşlem Seçiniz\n[1] Toplama\n[2] Çıkarma\n[3] Çarpma\n[4] Bölme\n[5] Üs Alma\n[6] Kök Alma\n[7] Çıkış\n")
                kontrol(secım)
            except Exception as hata:
                print(hata)
            else:
                break
        return secım
    def sayıkontrol(self,*args,bolmeMi=False):
        def sayımı(x):
            if x.isdigit() == False:
                raise Exception("Lütfen Bir Sayı Giriniz..!")
            elif bolmeMi== True:
                if int(x)==0:
                    raise Exception ("LÜTFEN SIFIR DIŞINDA BİR SAYI GİRİNİZ")
        while True:
            try:
                x = input("Lütfen {}  giriniz..!\n".format(*args))
                sayımı(x)
            except Exception as sayıhata:
                print(sayıhata)
            else:
                break
        return x
    def toplama(self):
        x= self.sayıkontrol("ilk sayıyı")
        y= self.sayıkontrol("ikinci sayıyı")
        toplam = int(x)+ int(y)
        print("Toplama İşleminin Sonucu {}".format(toplam))
        self.menudon()
    def cıkarma(self):
        x = self.sayıkontrol("ilk sayıyı")
        y = self.sayıkontrol("ikinci sayıyı")
        sonuc = int(x)-int(y)
        print(f"Çıkarma İşleminin Sonucu {sonuc}")
        self.menudon()
    def carpma(self):
        x = self.sayıkontrol("ilk sayıyı")
        y = self.sayıkontrol("ikinci sayıyı")
        sonuc = int(x)*int(y)
        print(f"Çarpma İşleminin Sonucu {sonuc}")
        self.menudon()
    def bolme(self):
        x= self.sayıkontrol("ilk sayıyı")
        y=self.sayıkontrol("ikinci sayıyı",bolmeMi=True)
        sonuc = int(x)/int(y)
        print(sonuc)
        self.menudon()
    def usalma(self):
        x = self.sayıkontrol("üssü alınacak sayıyı")
        y = self.sayıkontrol("üssü")
        sonuc = int(x)**int(y)
        print(f"Üs alma İşleminin Sonucu {sonuc}")
        self.menudon()
    def kokalma(self):
        x= self.sayıkontrol("kökü alıncak sayıyı")
        sonuc = math.sqrt(int(x))
        print(f"Kök alma İşleminin Sonucu {sonuc}")
        self.menudon()
    def cıkıs(self):
        print("Hesap Makinesinden Çıkılıyor..!")
        time.sleep(1)
        self.dongu = False
    def menudon(self):
        while True:
            x=input("Menüye dönmek için 1'e, Çıkış yapmak için 0'a basın..!\n")
            if x=="1":
                self.program()
                break
            elif x=="0":
                self.cıkıs()
                break
            else:
                print("Lütfen Geçerli Bir Rakam Giriniz")
hesapmakinesi= calculator()
while hesapmakinesi.dongu:
    hesapmakinesi.program()











