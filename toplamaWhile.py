def toplama(n1,n2):
   result=n1+n2
   print(result)
 
n0=int(input("cikis yapmak icin 0, toplama islemine devam etmek icin 1i secin:"))
while n0 == 1:  
  n1=int(input("Birinci sayi girin: "))
  n2=int(input("ikinci sayi girin: "))
  toplama(n1,n2)
  n0=int(input("cikis yapmak icin 0, toplama islemine devam etmek icin 1i secin:"))

print("cikis yapildi")  