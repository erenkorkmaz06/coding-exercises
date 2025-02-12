import requests
from bs4 import BeautifulSoup
for sayfa in range(1,17):
    link= "https://www.vatanbilgisayar.com/cep-telefonu-modelleri/?page={}".format(sayfa)

    parser=BeautifulSoup(requests.get(link).content,"html.parser")

    veri= parser.find("div",{"class":"wrapper-product-main"}).find_all("div",{"class":"product-list product-list--list-page"})

    for i in veri:
        ad= i.find("div",{"class":"product-list__content"})\
            .find("div",{"class":"product-list__product-name"}).find("h3").string
        fiyat= i.find("div",{"class":"product-list__content"}).find("div",{"class":"product-list__cost"}).find("div",{"class":"productList-camp"})\
            .find("span",{"class":"product-list__price"}).string
        print(f"TELEFON MODELİ:{ad},\nTELEFON FİYATI:{fiyat}TL\n")