import json
import re
import time
import random



class Site:
    def __init__(self):
        self.dongu= True
        self.verıler=self.verıal()

    def program(self):
        secım = self.menu()
        if secım == "1":
            self.gırıs()
        if secım == "2":
            self.kayıtol()
        if secım == "3":
            self.cıkıs()

    def menu(self):
        def kontrol(secım):
            if re.search("[^1-3]",secım):
                raise Exception("Lütfen 1 ile 3 arasında bir rakam giriniz..!")
            elif len(secım)!=1:
                raise Exception("Lütfen 1 ile 3 arasında bir rakam giriniz..!")
        while True:
            try:
                secım= input("Merhabalar, Korkmazlar Sitesine Hoşgeldiniz...\n\nLütfen Yapmak İstediğiniz İşlemi Seçiniz..!\n\n[1]-GİRİŞ\n\n[2]-KAYIT OL\n\n[3]-ÇIKIŞ\n\n")
                kontrol(secım)
            except Exception as hata:
                print(hata)
                time.sleep(2)
            else:
                break
        return secım
    def gırıs(self):
        print("GİRİŞ MENÜSÜNE YÖNLENDİRİLİYORSUNUZ")
        time.sleep(2)
        kullanıcıadı=input("LÜTFEN KULLANICI ADINIZI GİRİNİZ: ")
        sıfre=input("LÜTFEN ŞİFRENİZİ GİRİNİZ: ")

        sonuc= self.gırıskontrol(kullanıcıadı,sıfre)

        if sonuc==True:
            self.gırısbasarılı()
        else:
            self.gırısbasarısız()

    def gırıskontrol(self,kullanıcıadı,sıfre):
        self.verıler=self.verıal()

        try:
            for kullanıcı in self.verıler["Kullanıcılar"]:
                if (kullanıcı["Kullanıcıadı"]== kullanıcıadı) and (kullanıcı["Sifre"]== sıfre):
                    return True
        except KeyError:
            return False
        return False

    def gırısbasarılı(self):
        print("Kontrol Ediliyor..!")
        time.sleep(2)
        print("GİRİŞ BAŞARILI, KORKMAZLAR SİTESİNE HOŞGELDİNİZ..!")
        self.sonuc=False
        self.dongu=False

    def gırısbasarısız(self):
        print("!!!!KULLANICI ADI veya ŞİFRE HATALI!!!!")
        time.sleep(2)
        self.menudon()
    def kayıtol(self):
        def kontrolka(kullanıcıadı):
            if len(kullanıcıadı)<8:
                raise Exception("Kullanıcı adı en az 8 karakterden oluşmalıdır..!")
        while True:
            try:
                kullanıcıadı=input("Kullanıcı Adınız: ")
                kontrolka(kullanıcıadı)
            except Exception as hata:
                print(hata)
                time.sleep(2)
            else:
                break

        def kontrolsıfre(sıfre):
            if len(sıfre) < 8:
                raise Exception("Şifre en az 8 karakterden oluşmalıdır..!")
            elif not (re.search("[0-9]",sıfre)):
                raise Exception("Şifre en az 1  rakam içermelidir..!")
            elif not (re.search("[A-Z]",sıfre)):
                raise Exception("Şifre en az 1 tane büyük harf içermelidir..!")
            elif not (re.search("[a-z]",sıfre)):
                raise Exception("Şifre en az 1 tane küçük harf içermelidir..!")
        while True:
            try:
                sıfre = input("ŞİFRE: ")
                kontrolsıfre(sıfre)
            except Exception as hata:
                print(hata)
                time.sleep(2)
            else:
                break
        def kontrolmail(mail):
            if not ((re.search('@'  , mail)) and  (re.search(".com", mail))):
                raise Exception("Geçerli bir mail adresi giriniz...!")
        while True:
            try:
                mail = input("Mail adresiniz: ")
                kontrolmail(mail)
            except Exception as hatamail:
                print(hatamail)
                time.sleep(1)
            else:
                break
        sonuc= self.kayıtvarmı(kullanıcıadı,mail)
        if sonuc==True:
            print("Bu kullanıcı adı ve mail sistemde kayıtlı..!")
        else:
            aktivasyonkodu= self.aktıvasyongonder()
            durum=self.aktıvasyonkontrol(aktivasyonkodu)
        while True:
            if durum== True:
                self.verıkaydet(kullanıcıadı,sıfre,mail)
                break
            else:
                print("Yanlış aktivasyon kodu..!")
                self.menudon()
                break

    def kayıtvarmı(self,kullanıcıadı,mail):
        self.verıler= self.verıal()
        try:
            for kullanıcı in  self.verıler["Kullanıcılar"]:
                if (kullanıcı["Kullanıcıadı"]== kullanıcıadı) and (kullanıcı["Mail"]== mail):
                    return  True
        except KeyError:
            return False
        return False
    def aktıvasyongonder(self):

        with open("C:/Users/erenk/Desktop/Aktivasyon.txt","w",encoding="utf-8") as Dosya:
            aktivasyon=str(random.randint(10000-999999,1))
            Dosya.write("Aktivasyon Kodunuz:" + aktivasyon)
        return aktivasyon
    def aktıvasyonkontrol(self,aktivasyonkodu):
        aktivasyonkodual= input("Lütfen Mailinize Gelen Aktivasyon Kodunu Giriniz")
        if aktivasyonkodu== aktivasyonkodual:
            return True
        else:
            return False

    def verıal(self):
        try:
            with open("C:/Users/erenk/Desktop/Kullanıcılar.txt","r",encoding="utf-8") as Dosya:
                veriler=json.load(Dosya)
        except FileNotFoundError:
            with open("C:/Users/erenk/Desktop/Kullanıcılar.txt", "w", encoding="utf-8") as Dosya:
                Dosya.write("{}")
            with open("C:/Users/erenk/Desktop/Kullanıcılar.txt","r",encoding="utf-8") as Dosya:
                veriler=json.load(Dosya)
        return veriler


    def verıkaydet(self,kullanıcıadı,sıfre,mail):

        self.verıler=self.verıal()

        try:
            self.verıler["Kullanıcılar"].append({"Kullanıcıadı":kullanıcıadı,"Sifre":sıfre,"Mail": mail})
        except KeyError:
            self.verıler["Kullanıcılar"]=list()
            self.verıler["Kullanıcılar"].append({"Kullanıcıadı":kullanıcıadı,"Sifre":sıfre,"Mail": mail})

        with open("C:/Users/erenk/Desktop/Kullanıcılar.txt", "w", encoding="utf-8") as Dosya:
            json.dump(self.verıler,Dosya,ensure_ascii=False,indent=4)
            print("Kayıt Başarılı Şekilde Oluşturulmuştur...")
        self.menudon()
    def cıkıs(self):
        print("Siteden Çıkılıyor..!")
        time.sleep(2)
        self.dongu= False
    def menudon(self):
        while True:
            x=input("Ana menüye dönmek için 5'e, Çıkmak için 4'e basınız..:")
            if x=="5":
                print("Ana menüye dönülüyor..!")
                time.sleep(2)
                self.program()
                break
            elif x=="4":
                self.cıkıs()
                break
            else:
                print("Lütfen Geçerli bir sayıya basınız..!")


Sistem=Site()
while Sistem.dongu:
    Sistem.program()














