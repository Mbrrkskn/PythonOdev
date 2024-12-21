def is_prime(number):
    if number <= 1:   # 1 ve negatif sayılar asal sayı değildir
        return False
    if number == 2:      # 2 sayısı asal sayıdır
        return True
    if number % 2 == 0:     # 2'den büyük çift sayılar asal değildir
        return False
    # 3'ten büyük sayılar için asal sayı kontrolü (sadece tek sayılar için)
    for i in range(3, int(number ** 0.5) + 1, 2):  # Yalnızca tek sayıları kontrol ederiz
        if number % i == 0:
            return False  # Eğer bölünebiliyorsa asal değildir
    return True  # Hiçbir bölen bulunmazsa asal sayıdır
def main():
    print("Asal Sayi Kontrol Programi")
    try:
        # Kullanıcıdan sayı almak
        number = int(input("Bir sayi girin: "))
        # Sayının pozitif olduğunu kontrol etmek
        if number <= 0:
            print("Lütfen pozitif bir sayi girin.")
        else:
            # Asal sayı kontrolü ve sonucun yazdırılması
            if is_prime(number):
                print(f"{number} bir asal sayidir.")
            else:
                print(f"{number} bir asal sayi değildir.")
    except ValueError:
        print("Lütfen geçerli bir sayi girin.")  # Geçersiz giriş için hata mesajı
if __name__ == "__main__":
    main()
