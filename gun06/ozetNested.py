ogrenciler=[[1,"Metin","ISIK","Matematik",100],[2,"Enis","Ozdokumaci","almanca",90],
[3,"ilker","Okyar","Fizik",1000],[4,"Tarik","Akgun","Matematik",95],[5,"Bilal","ozturk","almanca",85]]

#en dusuk alan ogrencinin isim soyisim ve notunu yazdir

minNot=ogrenciler[0][4]
for ogrenci in ogrenciler:
    if minNot>ogrenci[4]:
        minNot=ogrenci[4]
for ogrenci in ogrenciler:
    if(ogrenci[4]==minNot):
        print("ogrenci adi: ",ogrenci[1],"\n","soyadi:",ogrenci[2],
              "\n",ogrenci[3],"dersi notu:",ogrenci[4])


notListesi=[]
for ogrenci in ogrenciler:
    notListesi.append(ogrenci[4])
print(min(notListesi))





