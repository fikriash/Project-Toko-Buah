#Mini Aplikasi

coverstrip = '-'*30
Cover = " WELCOME IN DATA COLLECT APP "
menucover = "---------DAFTAR MENU---------"

DaftarBarang = ["jeruk", "apel", "jeruk", "anggur", "pear"]
fruits = ["jeruk", "apel", "anggur", "pear", "alpukat", "avocado", 
"belimbing", "bengkuang", "blueberry", "blackberry", "cempedak", 
"ceri", "delima", "duku", "durian", "jambu", "jambu air", "jambu batu",
"jambu bol", "jambu biji", "jeruk bali", "jeruk purut", "jeruk nipis",
"kedongdong", "kelapa", "lengkeng", "kersen", "kiwi", "kismis", "kurma",
"lemon", "leci", "limau", "labu","mangga", "manggis", "markisa", "melon",
"mengkudu", "mentimun", "mentimun suri", "nanas", "nangka", "naga", "paprika",
"pepaya", "pisang", "rambutan", "raspberry", "salak", "sawo", "semangka",
"sirsak", "srikaya", "strawberry", "sukun", "terong", "timun", "tomat", 
"ubi", "waluh"]


loop = True     
while loop:
    print(coverstrip)
    print(Cover)
    print(coverstrip)
    print(menucover)
    print("1. Cetak Data Barang")
    print("2. Tambah Data Barang")
    print("3. Hapus Data Barang")
    print("4. Ubah Data Barang")
    print("5. Exit")
    print(coverstrip)         
    choice = int(input("Silahkan pilih menu [1-5]: "))
    print()
     
    if choice==1:     
        print("Menu 1 has been selected")
        c1 = input("Anda yakin ingin mencetak daftar barang (Y/N)? ")
        c1 = c1.lower()
        if c1 == "y" and DaftarBarang != []:
            print(DaftarBarang)
        elif DaftarBarang == []:
            print("Daftar Barang Kosong")
        else:
            c2 = input("Ingin kembali ke menu (Y/N)? ")
            c2 = c2.lower()
            if c2 == "y":
                loop = True
            else:
                print("Thank you!!!")
                loop = False
                print()        
        ## You can add your code or functions here
    elif choice==2:
        print("Menu 2 has been selected")
        cekdata = input("Silahkan Masukkan Data yang akan ditambahkan : ")
        cekdata = cekdata.lower()
        for i in fruits:
            if cekdata in fruits:
                if cekdata in DaftarBarang:
                    m = input("Data sudah ada dalam list, tetap ditambahkan (Y/N)?")
                    m = m.lower()
                    if m == "y":
                        DaftarBarang.append(cekdata)
                        print("Data Sudah ditambahkan")
                        print(DaftarBarang)
                        break
                    else:
                        print("Data Tidak Ditambahkan")
                else:
                    DaftarBarang.append(cekdata)
                    print("Data Sudah Ditambahkan")
                    print(DaftarBarang)
                    break    
            else: 
                print("Data yang anda masukkan bukan buah")
            break
        ## You can add your code or functions here
    elif choice==3:
        print("Menu 3 has been selected")
        print(f"Beriku adalah daftar barang anda : {DaftarBarang}")
        print("""1. Hapus sebagian data\n2. Hapus seluruh data""")
        deldaftar = input("Pilih menu untuk menghapus list : ")
        if deldaftar == "1":
            try:
                pildata = input("Masukan nama buah yang ingin dihapus : ")
                pildata = pildata.lower()
                for a in DaftarBarang:
                    DaftarBarang.remove(pildata)
                    print("Data telah di hapus")
                    print(DaftarBarang)
                    break
            except:
                print(f"{pildata} tidak ada dalam daftar")
        elif deldaftar == "2":
            jwb = input("Anda yakin ingin menghapus seluruhnya (Y/N)?")
            jwb = jwb.lower()
            if jwb == "y":
                DaftarBarang.clear()
                print("Data dihapus seluruhnya")
                print(f"Daftar barang anda adalah : {DaftarBarang}")
            else:
                print("Data tidak dihapus")
        else:
            print("Angka tidak ada dalam pilihan")
        ## You can add your code or functions here
    elif choice==4:
        print("Menu 4 has been selected")
        print(f"Berikut daftar barang anda : {DaftarBarang}")
        run = True
        while run:
            try:
                datalama = input("Silahkan masukan nama buah yg ingin di ubah : ")
                datalama = datalama.lower()
                for w in DaftarBarang:
                    if datalama not in DaftarBarang:
                        print("Nama buah yang ingin anda ubah tidak ada")
                    else:
                        databaru = input("Silahkan masukan data buah baru : ")
                        databaru = databaru.lower()
                        indatalama = DaftarBarang.index(datalama)
                        DaftarBarang[indatalama] = databaru
                        print(DaftarBarang)
                        print("Data Berhasil Diubah")
                        run = False
                    break
            except:
                print("Nama buah salah")
        ## You can add your code or functions here
    elif choice==5:
        print("Thank you!!!")
        loop = False
        ## You can add your code or functions here
        # This will make the while loop to end as not value of loop is set to False
    else:
        input("Pilihan tidak ada di menu, coba lagi!")

