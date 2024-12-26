print("1'den girilen sayiya kadar olan sayilar toplanacaktir ")  #1'den girilen sayiya kadar olan sayilar toplanacaktir ciktisini verir.
n1=int(input("Bir sayi giriniz: "))                              #n1'e deger atamak icin girdi alir.
n2=n1+1                                                          #range fonksiyonunda son sayi alinmadigi icin degere +1 eklenir.
tp=0                                                             #tp=0 degeri atanir
toplam=0                                                         #toplam=0 degeri atanir.
for tp in range(n2):                                             #0'dan girilen n2 degerine kadar dongunun calismasini saglar.
    toplam+=tp                                                   #tp degerini girilen sayiya kadar toplar ve toplama atar.
print(toplam)                                                    #toplam degerini yazdirir.
                                                                 #Ahmet ONEL