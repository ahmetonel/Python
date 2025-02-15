print("Piramit")
b=int(input("Basamak sayisi girin: "))
p=[]
b1=b-1                                     #ikinci for dongusunde fazladan bos p listesini yazdirmamak icin girilen sayidan 1 cikarildi.
for i in range(0,b):
    p.append(0)

    print(p)
for i in range(0,b1):
    p.remove(0)
    print(p)                               #Ahmet ONEL


