import random                                                           #random kutuphanesini ekler
print("1-100 arasi sayi tahmin etme") 
sayi1=int(input("0-100 arasinda bir tam sayi girin: "))
while sayi1<0 or sayi1>100:
    print("Lutfen 0-100 arasinda bir sayi girin")
    sayi1=int(input("0-100 arasinda bir tam sayi girin: "))

sayi2=random.randint(0,100)
if sayi2 == sayi1:
    print("Dogru tahmin")
else:
    print("Yanlis tahmin")
       
print("Dogru sayi " +str(sayi2))
                                                                        #Ahmet ONEL                                 