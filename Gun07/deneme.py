def seslileriCikar(str):
    str=str.lower()
    list1=["a","e","u","i","o","ü","ö"]
    for char in str:
        for char2 in list1:
            if char==char2:
                str = str.replace(char,"")
    return str
print(seslileriCikar("mEtin"))


