def arithmetic_operation(str):
    str = str.replace(" ", "")
    sonuc = 0
    if str.__contains__("+"):
        list = str.split("+")
        sonuc = int(list[0]) + int(list[1])
    elif str.__contains__("-"):
        list = str.split("-")
        sonuc = int(list[0]) - int(list[1])
    elif str.__contains__("*"):
        list = str.split("*")
        sonuc = int(list[0]) * int(list[1])
    elif str.__contains__("/"):
        list = str.split("/")
        if (list[1] == "0"):
            return "bolen sifir olamaz"
        sonuc = int(list[0]) / int(list[1])

    return sonuc


print(arithmetic_operation("5 / 0"))
