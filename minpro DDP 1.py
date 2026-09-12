data_pelanggaran = []

while True:
    print("\nMenu Sistem Pelanggaran Mahasiswa")
    print("1. Tambah data pelanggaran")
    print("2. Lihat data pelanggaran")
    print("3. Edit data pelanggaran")
    print("4. Hapus data pelanggaran")
    print("5. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5): ").strip()

    # OPSI 1: TAMBAH DATA
    if pilihan == "1":
        print("\nTambah Data Pelanggaran")
        nim = input("Masukkan NIM: ").strip()
        nama = input("Masukkan Nama: ").strip()
        pelanggaran = input("Masukkan Jenis Pelanggaran: ").strip()
        poin = input("Masukkan Poin Pelanggaran: ").strip()

        if not poin.isdigit():
            print("Poin harus berupa angka. Data pelanggaran tidak ditambahkan.")
        else:
            data_pelanggaran.append((nim, nama, pelanggaran, int(poin)))
            print("Data pelanggaran berhasil ditambahkan!")

    # OPSI 2: LIHAT DATA
    elif pilihan == "2":
        print("\nLihat Data Pelanggaran")
        if not data_pelanggaran:
            print("Belum Ada Data Pelanggaran")
        else:
            print("-" * 80)
            print(f"{'No':<5}{'NIM':<15}{'Nama':<25}{'Jenis Pelanggaran':<25}{'Poin':<10}")
            print("-" * 80)
            for i, item in enumerate(data_pelanggaran, start=1):
                nim, nama, pelanggaran, poin = item
                print(f"{i:<5}{nim:<15}{nama:<25}{pelanggaran:<25}{poin:<10}")
            print("-" * 80)

    # OPSI 3: EDIT DATA
    elif pilihan == "3":
        print("\nEdit Data Pelanggaran")
        if not data_pelanggaran:
            print("Belum Ada Data Pelanggaran")
        else:
            print("-" * 80)
            print(f"{'No':<5}{'NIM':<15}{'Nama':<25}{'Jenis Pelanggaran':<25}{'Poin':<10}")
            print("-" * 80)
            for i, item in enumerate(data_pelanggaran, start=1):
                print(f"{i:<5}{item[0]:<15}{item[1]:<25}{item[2]:<25}{item[3]:<10}")
            print("-" * 80)

            input_index = input("Masukkan nomor data yang ingin diedit: ").strip()
            
            if input_index.isdigit():
                index = int(input_index) - 1
                if 0 <= index < len(data_pelanggaran):
                    nim = input("Masukkan NIM baru: ").strip()
                    nama = input("Masukkan Nama baru: ").strip()
                    pelanggaran = input("Masukkan Jenis Pelanggaran baru: ").strip()
                    poin = input("Masukkan Poin Pelanggaran baru: ").strip()

                    if not poin.isdigit():
                        print("Poin harus berupa angka. Data pelanggaran tidak diubah.")
                    else:
                        data_pelanggaran[index] = (nim, nama, pelanggaran, int(poin))
                        print("Data pelanggaran berhasil diubah.")
                else:
                    print("Nomor data tidak valid.")

    # OPSI 4: HAPUS DATA
    elif pilihan == "4":
        print("\nHapus Data Pelanggaran")
        if not data_pelanggaran:
            print("Belum Ada Data Pelanggaran")
        else:
            print("-" * 80)
            print(f"{'No':<5}{'NIM':<15}{'Nama':<25}{'Jenis Pelanggaran':<25}{'Poin':<10}")
            print("-" * 80)
            for i, item in enumerate(data_pelanggaran, start=1):
                print(f"{i:<5}{item[0]:<15}{item[1]:<25}{item[2]:<25}{item[3]:<10}")
            print("-" * 80)

            input_index = input("Masukkan nomor data yang ingin dihapus: ").strip()
            
            if input_index.isdigit():
                index = int(input_index) - 1
                if 0 <= index < len(data_pelanggaran):
                    del data_pelanggaran[index]
                    print("Data pelanggaran berhasil dihapus.")
                else:
                    print("Nomor data tidak valid.")
            else:
                print("Nomor data harus berupa angka!")

    # OPSI 5: KELUAR
    elif pilihan == "5":
        print("Anda Keluar Dari Program.")
        break
    else:
        print("Pilihan bukan menu yang tersedia. Silakan pilih menu yang tersedia.")