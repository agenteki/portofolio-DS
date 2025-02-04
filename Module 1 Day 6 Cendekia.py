# # Soal1

# film_anda = set(input("Masukan film anda: ").split(','))
# film_teman = set(input("Masukan film teman: ").split(','))


# film_bersama= (len(film_anda.intersection(film_teman)) / (len(film_anda))*100)
# print(f'persenan kesukaan film bersama {film_bersama} %') 


#Soal 4
# list_buah = {
#     0:{"Index": 0 , "Nama": "Apel" ,"Stok": 20 , "Harga":10000},
#     1:{"Index": 1 , "Nama": "Jeruk" ,"Stok": 15 , "Harga":15000},
#     2:{"Index": 2 , "Nama": "Anggur" ,"Stok": 25 , "Harga":20000}}

list_buah = {
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
        print("DAFTAR BUAH")
        print()
        print("Index\t |Nama\t\t |Stok\t\t |Harga")
        for i in list_buah:
            print(f'{int(list_buah[i]["Index"])}\t |{str(list_buah[i]["Nama"])}\t\t |{int(list_buah[i]["Stok"])}\t\t |{str(list_buah[i]["Harga"])}')

    elif pilih == "2":
        Nama = input("Masukkan nama buah: ")
        Stok = int(input("Masukkan stok buah: "))
        Harga = int(input("Masukkan harga buah: "))
        stok_buah["ListBuah"].append({"Nama": [Nama], "Stok": [Stok], "Harga": [Harga]})
    
    elif pilih == "3":
        print("Anda menghapus buah 3")
    elif pilih == "4":
        print("Anda membeli buah 4")
    elif pilih == "5":
        print("Exit dari program")
        break
    else:
        print("Pilihan tidak valid")