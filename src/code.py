import random

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım bulabilecek misin?")
    
    tutulan_sayi = random.randint(1, 100)
    deneme_sayisi = 0
    
    while True:
        try:
            tahmin = int(input("Tahmininiz: "))
            deneme_sayisi += 1
            
            if tahmin < tutulan_sayi:
                print("Daha büyük bir sayı söyleyin.")
            elif tahmin > tutulan_sayi:
                print("Daha küçük bir sayı söyleyin.")
            else:
                print(f"Tebrikler! Sayıyı {deneme_sayisi}. denemede doğru bildiniz.")
                break
        except ValueError:
            print("Lütfen sadece geçerli bir sayı girin.")

if __name__ == "__main__":
    sayi_tahmin_oyunu()