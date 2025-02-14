
print("FizzBuzz")
n1=int(input("1-50 arasinda bir sayi girin: "))
while n1<=0 or n1>=51:
 print("1-50 arasinda sayi girin: ")
 n1=int(input("1-50 arasinda bir sayi girin: "))

if n1 >= 1 and n1<=50:
    while n1%3==0 and n1%5!=0:
        print("Fizz")
        break
    while n1%5==0 and n1%3!=0:
        print("Buzz")
        break
    while n1%3==0 and n1%5==0:
        print("FizzBuzz")
        break
    while n1%3!=0 and n1%5!=0:
        print(n1)
        break
else:
   print("1-50 arasinda sayi girin...")                #Ahmet ONEL