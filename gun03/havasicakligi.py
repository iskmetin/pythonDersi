sicaklik=int(input("hava kac derece?"))

if (sicaklik>30):
    print("hava cok sicak")
elif(sicaklik>=10 and sicaklik<=30):
    print("hava normal")
elif(sicaklik>=5 and sicaklik<10):
    print("hava biraz soguk")
else:
    print("hava buz gibi")


