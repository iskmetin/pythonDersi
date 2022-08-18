def ucgenAlan(a,h):
    return a*h/2
def kareAlan(a):
    return a*a
def dikdortgenAlan(a,b):
    return a*b
def daireAlani(r):
    return 3.14*r*r

while True:
    print("1.daire\n2.dikdortgen\n3kare\n4.ucgen")
    x=input("alanini hesaplamak istediginiz sekli secin")
    if x=="1":
        r=int(input("radiusu giriniz"))
        print(daireAlani(r))

    elif x=="2":
        a = int(input("1. kenari giriniz"))
        b = int(input("2. kenari giriniz"))
        print(dikdortgenAlan(a,b))
    elif x=="3":
        a = int(input("1 kenari giriniz"))
        print(kareAlan(a))
    elif x=="4":
        h = int(input("ucgenin yuksekligi  giriniz"))
        b = int(input("2. kenari giriniz"))
        print(dikdortgenAlan(b, h))
    else:
        print("yanlis girdiniz")
        break



