users = {}                                                   # {'kullanici_adi1:sifre1'}    sozluk

def user_check():                                            # Kullanici adi ve sifre kontrolu yapar
                                        
    u2 = input("Kullanici adini gir: ")
    p2 = input("Sifre gir: ")
    
    if u2 in users and users[u2] == p2:
        print("\nBilgisayar acildi. \nAna menuye donuldu.")
    else:
        print("Kullanici adi veya sifre hatali.")

def user_add():                                               #Yeni kullanici ekler.
    u1 = input("Yeni kullanici adi girin: ")
    if u1 in users:
        print("Bu kullanici ismi kullanilmakta...")
    else:
        p1 = input("Yeni sifre girin: ")
        users[u1] = p1
        print("Kullanici basariyla eklendi.")

def user_remove():                                            #Mevcut kullaniciyi listeden siler.
    t1 = input("Silmek istenilen kullanici: ")
    if t1 not in users:
        print("Kullanici bulunamadi.")
        return

    t2 = input("Sifreyi girin: ")
    if users[t1] == t2:
        del users[t1]
        print("Kullanici silindi.")
    else:
        print("Sifre yanlis.")

def user_islem():                                             #kullanici islem fonkisyonu
     while True:
        print("\n1. Kullanicilari listele.")
        print("2. Kullanici sifresini degistir.")
        print("3. Kullanici sil.")
        print("4. Ana menuye don.")
        
        s2 = input("Secim yapin: ")

        if s2 == "1":
            print("Kullanicilar:", list(users.keys()))
        
        elif s2 == "2":
            u4 = input("Kullanici adi girin: ")
            if u4 in users:
                p4 = input("Mevcut sifre girin: ")
                if users[u4] == p4:
                    np4 = input("Yeni sifre: ")
                    users[u4] = np4
                    print("Sifre basariyla degistirildi.")
                else:
                    print("Hatali sifre.")
            else:
                print("Kullanici bulunamadi.")

        elif s2 == "3":
            user_remove()
        
        elif s2 == "4":
            break                                             # Donguden cikarip ana menuye dondurur.
        
        else:
            print("Gecersiz secim.")

def main():                                                   #Ana fonksiyon
     while True:
        print("1. Bilgisayari ac.")
        print("2. Kullanici islemleri.")
        print("3. Cikis yap.")

        s1 = input("Islem secin: ")

        if s1 == "1":
            if len(users) == 0:
                print("Henuz kayitli kullanici yok, yeni kullanici ekleyin.")
                user_add()
            else:
                user_check()

        elif s1 == "2":
            user_islem()

        elif s1 == "3":
            print("Cikis yapiliyor...")
            break                    
        
        else:
            print("Gecersiz secim!")


main()                                                        #Ahmet ONEL                    

