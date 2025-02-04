# # Soal1

# film_anda = set(input("Masukan film anda: ").split(','))
# film_teman = set(input("Masukan film teman: ").split(','))


# film_bersama= (len(film_anda.intersection(film_teman)) / (len(film_anda))*100)
# print(f'persenan kesukaan film bersama {film_bersama} %') 


#Soal 4

from tabulate import tabulate


stok_buah = {
    "ListBuah": [
        {"Nama": ["Apel"], "Stok": [25], "Harga": [10000]},
        {"Nama": ["Jeruk"], "Stok": [30], "Harga": [15000]},
        {"Nama": ["Anggur"], "Stok": [30], "Harga": [20000]}
    ]
}

while True:
    print("Selamat Datang di Pasar Buah")
    print("List Menu:")
    print("1. Menampilkan daftar buah")
    print("2. Menambah Buah")
    print("3. Menghapus Buah")
    print("4. Membeli Buah")
    print("5. Exit program")


    pilih = input("Masukkan pilihan Anda: \n")
 
    if pilih == "1":
        print()
        print("DAFTAR BUAH")
        print()
        print("Index\t |Nama\t\t\t |Stok\t  |Harga")
        for index,y in enumerate(stok_buah["ListBuah"]):
            print(f"{index}\t |{y['Nama']}\t\t |{y['Stok']}\t  |{y['Harga']}")
        print()

    elif pilih == "2":
        Nama = input("Masukkan nama buah: ")
        Stok = int(input("Masukkan stok buah: "))
        Harga = int(input("Masukkan harga buah: "))
        stok_buah["ListBuah"].append({"Nama": [Nama], "Stok": [Stok], "Harga": [Harga]})
        print()
        print()
        print("DAFTAR BUAH")
        print()
        print("Index\t |Nama\t\t\t |Stok\t  |Harga")
        for index,y in enumerate(stok_buah["ListBuah"]):
            print(f"{index}\t |{y['Nama']}\t\t |{y['Stok']}\t  |{y['Harga']}")
        print()
    
    elif pilih == "3":
        print()
        print("DAFTAR BUAH")
        print()
        print("Index\t |Nama\t\t\t |Stok\t  |Harga")
        for index,y in enumerate(stok_buah["ListBuah"]):
            print(f"{index}\t |{y['Nama']}\t\t |{y['Stok']}\t  |{y['Harga']}")
        print()
        buah_hapus = (int(input("Masukkan index buah yang ingin dihapus: ")))
        if 0 <= buah_hapus < len(stok_buah["ListBuah"]):
            keranjang_dihapus = stok_buah["ListBuah"].pop(buah_hapus)
            print(f"\nBuah '{keranjang_dihapus['Nama']}' berhasil dihapus.")
        else:
            print("\nIndex tidak valid! Silakan coba lagi.")
        print()
        print("\nData Buah Setelah Diperbarui:")
        if stok_buah["ListBuah"]:
            print("Index\t |Nama\t\t\t |Stok\t  |Harga")
            for index,y in enumerate(stok_buah["ListBuah"]):
                print(f"{index}\t |{y['Nama']}\t\t |{y['Stok']}\t  |{y['Harga']}")
        print()
        
    elif pilih == "4":
        print()
        print("DAFTAR BUAH")
        print()
        print("Index\t |Nama\t\t\t |Stok\t  |Harga")
        for index,y in enumerate(stok_buah["ListBuah"]):
            print(f"{index}\t |{y['Nama']}\t\t |{y['Stok']}\t  |{y['Harga']}")
        print()
        pilihan = int(input("Pilih index buah yang ingin dibeli: "))
        if 0 <= pilihan < len(stok_buah["ListBuah"]):
            buah = stok_buah["ListBuah"][pilihan]
            jumlah = int(input(f"Masukkan jumlah {buah['Nama'][0]} yang ingin dibeli: "))
            if jumlah <= buah["Stok"][0]:
                total_harga = jumlah * buah["Harga"][0]
                buah["Stok"][0] -= jumlah
                print(f"\nAnda berhasil membeli {jumlah} {buah['Nama'][0]} dengan total Rp{total_harga}.")
            else:
                print(f"Stok tidak cukup, Stok {buah['Nama'][0]} tinggal {buah["Stok"][0]}")
        else:
            print("Pilihan tidak valid.")
    elif pilih == "5":
        print("Exit dari program")
        break
    else:
        print("Pilihan tidak valid")