ogrenciler1=["ilker","enis","bilal","tarik"]
hocalar=["metin","mehmet","enes"]

#metin ilkerin hocasidir ...

for i in range(0,len(hocalar)) :
    for j in range(0,len(ogrenciler1)) :
        print(hocalar[i],ogrenciler1[j], "in hocasidir")

for x in hocalar:
    for a in ogrenciler1:
        print(x,a,"in hocasidir")

