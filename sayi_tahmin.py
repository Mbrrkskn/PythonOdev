import random  # random modülünü dahil etmemiz, bilgisayarın rastgele sayı tutmasını sağlayacak
# Sayı tahmin oyunu fonksiyonu
def sayi_tahmin_oyunu():
    print("Sayi Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasinda bir sayi tuttum :) bakalim tahmin edebilecek misin?")
    # Bilgisayarın tutacağı rastgele sayı (1 ile 100 arasında)
    secret_number = random.randint(1, 100) 
    # Kullanıcının tahminini almak için değişken
    attempts = 0  # Tahmin sayısını takip etmek için bir değişken
    while True:
        try:
            # Kullanıcıdan tahmin alıyoruz
            user_tahmin = int(input("Tahmininizi girin: "))
            attempts += 1  # Her tahminde deneme sayısını arttırıyoruz
            # Kullanıcı doğru sayıyı tahmin ettiyse
            if user_tahmin < secret_number:
                print("Daha yüksek bir sayi tahmin edin.")
            elif user_tahmin > secret_number:
                print("Daha düşük bir sayi tahmin edin.")
            else:
                print(f"Tebrikler! Doğru tahmin ettiniz. Sayi {secret_number} idi.")
                print(f"Toplamda {attempts} denemede doğru cevabi buldunuz.")
                break  # Doğru tahmin yapılınca oyun sona erer
        except ValueError:
            print("Lütfen geçerli bir sayi girin.")  # Eğer kullanıcı geçerli bir sayı girmezse uyarı veririz
# Ana program fonksiyonu
def main():
    sayi_tahmin_oyunu()
# Programı çalıştırma
if __name__ == "__main__":
    main()
