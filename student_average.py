def main():
    print("Öğrenci Not Ortalamasi Hesaplama Programi")
    # Toplam 20 öğrenci için notları toplayacağız
    total_students = 20  # Öğrenci sayısı
    total_score = 0  # Toplam puan başlangıçta 0
    # Kullanıcıdan her öğrencinin notunu alacağız
    try:
        for i in range(1, total_students + 1):  # 20 öğrenci için döngü
            while True:  # Geçersiz not girişi kontrolü için döngü
                try:
                    score = float(input(f"{i}. öğrencinin sinav notunu girin (0-100 arasi): "))
                    # Geçerli bir not aralığı kontrolü (0 ile 100 arasında)
                    if 0 <= score <= 100:
                        total_score += score  # Geçerli notu toplam puana ekliyoruz
                        break  # Geçerli not girildiyse döngüden çıkıyoruz
                    else:
                        print("Lütfen 0 ile 100 arasinda bir not girin.")
                except ValueError:
                    print("Geçersiz bir değer girdiniz. Lütfen sayisal bir değer girin.")
        # Ortalamayı hesaplıyoruz
        average_score = total_score / total_students
        # Sonucu ekrana yazdırıyoruz
        print(f"\n20 öğrencinin sinav notlarinin ortalamasi: {average_score:.2f}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
if __name__ == "__main__":
    main()
