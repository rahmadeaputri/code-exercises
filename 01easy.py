def sumArray():
    # Input pertama: panjang array
    panjang_array = int(input("Masukkan panjang array: ").strip())
    
    # Input ke2: isi array sebagai daftar bilangan bulat
    ar = list(map(int, input(f"Masukkan {panjang_array} angka (dipisahkan dengan spasi): ").rstrip().split()))
    
    # Memastikan bahwa panjang array sesuai dengan yang diinputkan
    if len(ar) != panjang_array:
        print("Jumlah elemen yang dimasukkan tidak sesuai dengan panjang array.")
        return
    
    # Menghitung jumlah elemen dalam array
    total = sum(ar)
    
    # Output: jumlah isi array
    print(f"Jumlah elemen array: {total}")

# Memanggil fungsi
sumArray()