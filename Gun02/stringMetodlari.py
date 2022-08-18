text1="Hello World"
#metinin uzunlugunu bulur
print(len(text1))

#belirtilen karakterler arasini yazdirir

print(text1[0:3])
"""print(text1[0:1])
print(text1[3:10])
print(text1[-5:-3])"""

text2="ENIS"
text3="tarik"
text4="bilal ziya"
print(text2.lower())
print(text3.upper())
print(text2.capitalize())
print(text4.title())

var1="1234a"
var2="abcd1"
print(var1.isdigit()) #rakamlardan olusup olusmadigini anlariz
print(var2.isalpha()) #harflerden olusup

isim="     malatya ne guzel      "
sayi="   16    "
print(isim.find("t"))
print(isim.count("A"))
print(isim.replace("a",""))
print(isim.split("a")) #belirtilen karakterlerle bolme
print(isim.strip()) #basinda ve sonundaki bosluklari kaldirir








