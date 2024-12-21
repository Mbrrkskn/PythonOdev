# Basamak toplamını hesaplayan fonksiyon
def digit_sum(number):
    total = 0  # Başlangıçta toplamı sıfırla başlatıyoruz.
    # Sayının her bir basamağını alıp toplama ekliyoruz.
    while number > 0:
        total += number % 10  # Son basamağı alıyoruz ve toplamı artırıyoruz.
        number //= 10  # Sayıyı bir basamak sola kaydırıyoruz (tam sayı bölme).
    return total  # Hesaplanan toplamı döndürüyoruz.
# Ana program fonksiyonu
def main():
    print("5 Sayinin Basamak Toplamini Hesaplama")
    try:
        # Kullanıcıdan 5 farklı sayı alıyoruz.
        numbers = []
        for i in range(1, 6):
            number = int(input(f"{i}. sayiyi girin: "))
            numbers.append(number)  # Sayıyı listeye ekliyoruz.
        # Basamak toplamlarını hesaplayıp ekrana yazdırıyoruz.
        for i, number in enumerate(numbers, start=1):
            total = digit_sum(number)  # Basamak toplamını hesaplıyoruz.
            print(f"{number} sayisinin basamak toplami: {total}")
    except ValueError:
        print("Lütfen geçerli bir sayi girin.")  # Geçersiz giriş için hata mesajı.
if __name__ == "__main__":
    main()
