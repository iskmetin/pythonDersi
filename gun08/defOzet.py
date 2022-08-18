ogrenciListesi = [["metin", "ISIK", "0665565654"], ["enis", "oz", "0665565654"]]


def isimSor():
    isim = input("isim  giriniz")

    return isim


def soyisimSor():
    soyisim = input("soyisim  giriniz")

    return soyisim


def noSor():
    no = "a"
    while not (no.isdigit()) or (len(no) != 12):
        no = input("numara giriniz")

    return no


def ogrenciEkle():
    list = []
    isim = isimSor()
    soyisim = soyisimSor()
    no = noSor()
    list.append(isim)
    list.append(soyisim)
    list.append(no)
    ogrenciListesi.append(list)
    print(ogrenciListesi)


def ogrenciNumaraDuzenle():
    ogrenciIsmi = isimSor()
    for i in range(0, len(ogrenciListesi)):
        if ogrenciIsmi == ogrenciListesi[i][0]:
            ogrenciListesi[i][2] = noSor()
            print("kayit duzenlendi")


def ogrenciSil():
    ogrenciIsmi = isimSor()
    for i in range(0, len(ogrenciListesi)):
        if ogrenciIsmi == ogrenciListesi[i][0]:
            del ogrenciListesi[i]
            break


str = ""
while str.lower != "x":
    str = input("1.ogrenci ekle\n2.ogrenci no duzenle\n3.ogrenci sil")
    if str == "1":
        ogrenciEkle()
        print(ogrenciListesi)
    elif str == "2":
        ogrenciNumaraDuzenle()
        print(ogrenciListesi)

    elif str == "3":
        ogrenciSil()
        print(ogrenciListesi)
    else:
        print("yanlis girdiniz")
