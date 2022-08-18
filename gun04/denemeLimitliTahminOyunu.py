
# bilgisayarin random tanimladigi sayiya esit olana kadar
# kullanicidan sayi alan , buyukse buyuk yazsin kucukse kucuk
# ve esit oldugunda kazandiniz diyen
#kullanicinin 3 tahmin hakki olsun
import random
sayi=random.randint(1,20)
denemeSayisi=0
kazandimi=True
while denemeSayisi<3:
    if denemeSayisi==0:
        tahmin = int(input("tahmin giriniz"))
        denemeSayisi += 1
    if tahmin>sayi:
        print("soylediginiz sayi buyuk")
        kazandimi = False
        denemeSayisi+=1
        tahmin = int(input("tahmin giriniz"))
    elif tahmin<sayi:
        print("soylediginiz sayi kucuk")
        kazandimi = False
        denemeSayisi += 1
        tahmin = int(input("tahmin giriniz"))
    else:
        print("Tebrikler kazandiniz")
        kazandimi=True
        break
if  kazandimi==False:
    print("kazanamadiniz maalesef")




