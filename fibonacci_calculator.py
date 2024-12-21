def fibonacci(n):
    fib_sequence = [0, 1]  # Fibonacci serisinin ilk iki elemanını başlatıyoruz. 
    # Fibonacci serisinin hesaplanması (n'in 2'den büyük olması durumunda döngü çalışacak)
    for i in range(2, n):  # Başlangıç olarak 2. elemandan (0 ve 1 zaten eklenmişti) başlıyoruz
        next_num = fib_sequence[i - 1] + fib_sequence[i - 2]  # Önceki iki sayıyı toplar
        fib_sequence.append(next_num)  # Hesaplanan sayıyı diziye ekler
    return fib_sequence  # Hesaplanan Fibonacci dizisini döndürür
# Ana fonksiyon
def main():
    print("Fibonacci Serisi Hesaplayici")
    # Kullanıcıdan alınacak n değeri (100'e kadar Fibonacci'yi hesaplamak için n'yi alıyoruz)
    try:
        n = int(input("Fibonacci serisini kaçinci sayiya kadar görmek istersiniz? (100'e kadar pozitif bir sayı): "))
        # Kullanıcıdan alınan değerin geçerli olup olmadığını kontrol etme
        if n <= 0:
            print("Lütfen pozitif bir sayi girin.")
        elif n > 100:
            print("Lütfen 100'e kadar bir sayi girin.")
        else:
            # Fibonacci serisini hesapla
            fib_sequence = fibonacci(n) 
            # Sonuçları ekrana yazdır
            print(f"\nFibonacci serisi (ilk {n} eleman):")
            print(fib_sequence)
    except ValueError:
        print("Lütfen geçerli bir sayi girin.")
if __name__ == "__main__":
    main()
