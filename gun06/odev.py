"""
ic ice liste sorusu

ogrenciler=[[1,"Metin","ISIK","Matematik",80],[2,"Enis","Ozdokumaci","almanca",90],[3,"ilker","Okyar",
"Fizik",100],[4,"Tarik","Akgun","Matematik",95],[5,"Bilal","ozturk","almanca",85]]



bu sekilde ic ice liste olusturun.icerideki listelerin 0.inci elemani ogrenci numarasi olsun
kullanici ogrenci numarasini gidiriginde ekrana sunu yazdirsin

ornek
ogrenci numarasi giriniz=1
Ogrenci adi=Metin
soyadi=ISIK
Matematik dersi notu=80

"""
ogrenciler=[[1,"Metin","ISIK","Matematik",80],[2,"Enis","Ozdokumaci","almanca",90],[3,"ilker","Okyar",
"Fizik",100],[4,"Tarik","Akgun","Matematik",95],[5,"Bilal","ozturk","almanca",85]]

ogrenciNo=int(input("ogrenci numarasini girin"))

for ogrenci in ogrenciler:
    if(ogrenci[0]==ogrenciNo):
        print("ogrenci adi: ",ogrenci[1],"\n","soyadi:",ogrenci[2],"\n",ogrenci[3],"dersi notu:",ogrenci[4])





