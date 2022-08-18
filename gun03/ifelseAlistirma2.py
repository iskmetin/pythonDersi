isim=input("isminizi giriniz")

if isim.startswith("m"):
    print("m ile basliyor")
elif isim.endswith("k"):
    print("m ile baslamiyor ama k ile bitiyor")
else:
    print("normal ismin var")