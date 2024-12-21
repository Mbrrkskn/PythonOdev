def reverse_list(input_list):
    return input_list[::-1]  # Listeyi tersine çevirme işlemi
def main():
    print("Liste Elemanlarini Ters Çevirme Programi")
    try:
        # Kullanıcıdan liste elemanları almak
        user_input = input("Bir liste elemanlarini girin (virgülle ayirarak): ")
        # Kullanıcıdan alınan veriyi listeye dönüştürme
        input_list = [item.strip() for item in user_input.split(",")]  # Virgülle ayırarak liste oluşturuluyor
        # Listenin tersine çevrilmesi
        reversed_list = reverse_list(input_list)
        # Sonucun yazdırılması
        print("Orijinal Liste:", input_list)
        print("Ters Çevrilmiş Liste:", reversed_list)
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
if __name__ == "__main__":
    main()
