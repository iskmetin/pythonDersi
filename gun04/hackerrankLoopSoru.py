"""
kullanicidan  1 ile 9 arasinda bir sayi istesin ve o sayiya kadar yazdirdir
1
22
333
4444
55555
......
"""


while True:
    sayi = int(input("sayi giriniz"))
    if sayi>0 and sayi<10:
        for i in range(1,sayi+1):
            print(i*str(i))
        break
    else:
        print("gecersiz sayi girdiniz")