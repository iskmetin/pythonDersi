def fact_of_fact(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc


print(fact_of_fact(5))
