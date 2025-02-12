import numpy as np
def tahminci():
    sayı = np.random.randint(0,101)
    durum= True
    while durum==True:
        tahmin= int(input("Lütfen 0 ile 100 arasında bir tahminde bulunun\n"))
        if sayı==tahmin:
            print("Tahmininz Doğru Tebrikler")
            durum= False
        elif sayı < tahmin:
            print("Tahmininz Yanlış Lütfen daha küçük bir sayı deneyin..!")
        elif sayı >tahmin:
            print("Tahmininz Yanlış Lütfen daha büyük bir sayı deneyin..!")
tahminci()
