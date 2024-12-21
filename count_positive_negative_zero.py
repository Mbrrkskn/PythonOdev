def main():
    print("Pozitif, Negatif ve Sifir Sayma Programi")
    # Pozitif, negatif ve sıfır sayıları saymak için başlangıçta sayaçları sıfırlıyoruz.
    positive_count = 0  # Pozitif sayılar için sayaç
    negative_count = 0  # Negatif sayılar için sayaç
    zero_count = 0  # Sıfır sayıları için sayaç
    # Kullanıcıdan 10 sayı girmesini istiyoruz
    try:
        numbers = []
        for i in range(1, 11):  # 1'den 10'a kadar döngü
            number = int(input(f"{i}. sayiyi girin: "))  # Sayıyı alıyoruz
            numbers.append(number)  # Sayıyı listeye ekliyoruz
        # Listeyi analiz ediyoruz: pozitif, negatif, sıfır
        for number in numbers:
            if number > 0:  # Pozitif sayıları kontrol ediyoruz
                positive_count += 1
            elif number < 0:  # Negatif sayıları kontrol ediyoruz
                negative_count += 1
            else:  # Sıfırları kontrol ediyoruz
                zero_count += 1
        # Sonuçları ekrana yazdırıyoruz
        print(f"Pozitif sayilar: {positive_count}")
        print(f"Negatif sayilar: {negative_count}")
        print(f"Sifir sayilari: {zero_count}")
    except ValueError:
        print("Lütfen geçerli bir sayi girin.")  # Geçersiz giriş için hata mesajı
if __name__ == "__main__":
    main()
