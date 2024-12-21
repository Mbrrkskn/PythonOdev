# Celsius'tan Fahrenheit'a dönüşüm fonksiyonu
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
# Fahrenheit'tan Celsius'a dönüşüm fonksiyonu
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
# Kullanıcıdan sıcaklık değeri ve dönüşüm tipi alma
def main():
    try:
        # Kullanıcıdan sıcaklık değeri alma
        temperature = float(input("Sıcaklık değerini girin: "))
        
        # Kullanıcıdan dönüşüm tipi alma
        conversion_type = input("Dönüşüm tipi (C->F veya F->C): ").strip()

        # Dönüşüm işlemi ve sonuç yazdırma
        if conversion_type == "C->F":
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature} °C, {result:.2f} °F'ye eşittir.")
        elif conversion_type == "F->C":
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature} °F, {result:.2f} °C'ye eşittir.")
        else:
            print("Geçersiz dönüşüm tipi. Lütfen 'C->F' veya 'F->C' yazınız.")

    except ValueError:
        print("Lütfen geçerli bir sıcaklık değeri giriniz.")
# Ana fonksiyonu çağırma
if __name__ == "__main__":
    main()
