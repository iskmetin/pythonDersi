x="bIlal ZiYA ozTUrk"


def isimDuzelt(x):

    list1 = x.split()
    x=""
    for i in range(0,len(list1)-1):
        list1[i]=list1[i].capitalize()
        x+=list1[i]+" "
    list1[len(list1)-1]=list1[len(list1)-1].upper()
    x+=list1[len(list1)-1]
    return x




while True:
    x=input("Isminizi giriniz")
    if x.lower()=="x":
        break
    print(isimDuzelt(x))



#