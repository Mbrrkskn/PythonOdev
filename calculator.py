#Toplama,çıkarma,çarpma,bölme işlemleri
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:  
        return "Hata: Sifira bölme yapilamaz!"
    return x / y
def main():
    print("Basit Hesap Makinesi Uygulamasi")
    print("İşlem yapmak istediğiniz türü seçin:")
    print("1. Toplama (+)")
    print("2. Çikarma (-)")
    print("3. Çarpma (*)")
    print("4. Bölme (/)")
    choice = input("Seçiminizi yapin (1/2/3/4): ")
    num1 = float(input("Birinci sayiyi girin: "))
    num2 = float(input("İkinci sayyi girin: "))
    # Seçilen işlemi gerçekleştirme
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Geçersiz giriş. Lütfen geçerli bir işlem seçin.")
if __name__ == "__main__":
    main()
