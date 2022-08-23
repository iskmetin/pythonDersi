while True:
    sayi = int(input("sayi giriniz"))
    if sayi>0 and sayi<10:
        for i in range(1, sayi+1):
            for j in range(1, i + 1):
                print(str(j), end="")

            for a in range(i - 1, 0, -1):
                print(str(a), end="")
            print("")
        break
    else:
        print("gecersiz sayi girdiniz")




