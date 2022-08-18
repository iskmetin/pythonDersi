#sayi istesin
"""
                *
               **
              ***
             ****

   **************
"""


while True:
    sayi = int(input("sayi giriniz"))
    if sayi>0 and sayi<10:
        for i in range(1,sayi+1):
            print((sayi-i)*" "+i*str("*"))
        break
    else:
        print("gecersiz sayi girdiniz")