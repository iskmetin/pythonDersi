liste=["kalem","defter","silgi","kitap"]
liste[1]="masa"
#["kalem","masa","silgi","kitap"]
liste.append("defter")
#["kalem","masa","silgi","kitap","defter"]
#2nciyi cikartir
liste.pop(2)
#["kalem","masa","kitap","defter"]

liste.insert(1,"kitaplik")
#["kalem","kitaplik","masa","kitap","defter"]

#terse cevirir
liste=liste[::-1]

print(liste)

