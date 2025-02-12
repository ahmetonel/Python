print("Faktoriyel hesabi")                     #Ekrana cikti verir
sayi2=int(input("Bir sayi girin: "))           #Sayi girilmesini ister.
sayi1=sayi2+1                                  #Range son sayi alýnmadýðý icin girilen sayiya +1 ekler
s1=1
s2=1
for s1 in range(1,sayi1):                      #Birden girilen degere kadara donguyu dondurur
     s2*=s1                                    #Donguden gelen sayilari s2 ile carpar ve yeni s2 atar             
     
print(s2)                                      #Ahmet ONEL