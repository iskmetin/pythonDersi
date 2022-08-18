
# bilgisayarin random tanimladigi sayiya esit olana kadar
# kullanicidan sayi alan , buyukse buyuk yazsin kucukse kucuk
# ve esit oldugunda kazandiniz diyen
#kullanicinin 3 tahmin hakki olsun
import random
sayi=random.randint(1,100)
tahmin=int(input("tahmin giriniz"))

while tahmin!=sayi:
    if tahmin>sayi:
        print("soylediginiz sayi buyuk")
        tahmin = int(input("tahmin giriniz"))
    elif tahmin<sayi:
        print("soylediginiz sayi kucuk")
        tahmin = int(input("tahmin giriniz"))
print("tebrikler bildiniz")




