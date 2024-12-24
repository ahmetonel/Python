cpt1=1                             #cpt1'e 1'i atar.
cpt2=1                             #cpt2'e 1'i atar.
cpt3=1                             #cpt3'e 1'i atar.
ytoplam=0                          #ytoplam degerine 0'i atar.
print("0-100 sayilarinin toplami") #0-100 sayilarinin toplami ciktisini verir.
for tp in range(0,101):            #0'dan 100'e kadar deger atar.
    ytoplam+=tp                    #0-100 dongusunden gelen sayilari ytoplama ile toplayip yeni degeri ytoplama atar.
print(ytoplam)                     #dongu sonunda ytoplam degerini yazdirir.


print("1-100 sayilarin carpimi")   #1-100 sayiliarin carpimi ciktisini verir.
for cp in range(1,101):            #dongu tanimlar 1'den 100'e kadar sayilari verir.
    cpt1*=cp                       #donguden gelen sayilari cpt1 degeri ile carpar ve yeni cpt1 degeri olarak dongu bitinceye kadar tanimlar.
print(cpt1)                        #dongu sonunda toplam degerini yazdirir.

print("tek sayilarin carpimi ")    #tek sayilarin carpimi ciktisini verir.
for tc in range(1,101,2):          #donguden 1den baslayarak 2'ser atlayarak yazar ve tek sayilari elde ederiz.
    cpt2*=tc                       #donguden gelen tc degerini cpt2 degerine carpip yeni deger olarak atar.
print(cpt2)                        #dongu bittikten sonra cpt3 yazdiri.
                          
print("cift sayilarin carpimi")    #Cift sayilarin carpimi ciktisini verir.
for ac in range(0,101,2):          #dongu icinde 0'dan 100'e kadar 2'ser deger atar.
    if ac > 0:                     #rangeden gelen sayilarin 0'dan buyuk olmasini saglar bu sayede carpim sifirilanmaz.
        cpt3*=ac                   #gelen ac degerini cpt3 ile carpar ve yeni cpt3'e esitler.
print(cpt3)                        #dongu bittikten sonra cp3 degerini yazdirir.

print("Ahmet ONEL")                #Ahmet ONEL