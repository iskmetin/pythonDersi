"""
***********
 *********
  *******
   *****
    ***
     *

"""
while True:
    sayi = int(input("satir sayi giriniz"))
    if sayi>0 and sayi<10:
        for i in range(1,sayi+1):
            print(" "*(i-1),end="")
            print("*"*(((sayi*2)-i*2)+1))
        break
    else:
        print("gecersiz sayi girdiniz")

