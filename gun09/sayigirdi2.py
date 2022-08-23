a=""
toplam=0
count=0
while a!="0":
    a=input("sayi giriniz")
    if a=="0":
        break
    toplam+=int(a)
    count+=1
print(toplam/count)

