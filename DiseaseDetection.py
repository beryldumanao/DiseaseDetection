import time
import os

# ==================== FUNGSI TAMBAHAN ====================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def garis():
    print("-" * 65)

def loading(text, durasi=1.5):
    print(text, end="")
    for _ in range(3):
        time.sleep(durasi / 3)
        print(".", end="", flush=True)
    print("\n")

def header():
    clear()
    print("+----------------------------------------+")
    print("|        Selamat Datang di Aplikasi      |")
    print("|            Cek Kesehatan Anda          |")
    print("+----------------------------------------+")
    print("")

# ======================== PROGRAM ========================

while True:
    header()

    # ------- Input Nama -------
    while True:
        nama = input("Masukkan Nama Anda : ")

        if nama.strip() == "":
            print("❗ Nama tidak boleh kosong!\n")
            continue

        if nama.replace(" ", "").isalpha():
            break
        else:
            print("❗ Nama hanya boleh berisi huruf!\n")

    loading(f"Halo {nama}, sedang mempersiapkan sistem")

    # ------- Konfirmasi Cek Kesehatan -------
    pilihan = input(f"Halo {nama}, apakah Anda ingin mendeteksi penyakit? (y/n) : ").lower()
    print("")

    if pilihan == "n":
        print("Terima kasih telah menggunakan aplikasi. 🙏")
        break

    gejala = []

    if pilihan == "y":
        clear()
        header()
        print(f"👤 {nama}, pilih gejala utama yang Anda rasakan:\n")
        print("1. Batuk")
        print("2. Demam")
        print("3. Pusing")
        print("4. Sakit perut\n")

        user_input = input("Masukkan pilihan [1/2/3/4] : ")
        print("")

        # ===================== GEJALA BATUK =====================
        if user_input == "1":
            gejala.append("Batuk")
            print("Gejala tambahan apa yang Anda rasakan?")
            print("1. Sulit bernapas / napas cepat")
            print("2. Sakit tenggorokan\n")
            pilih = input("Pilih : ")

            if pilih == "1":
                gejala.append("Sulit bernapas / napas cepat")
                print("\nApakah ada gejala tambahan lagi?")
                print("1. Dada terasa sesak")
                print("0. Tidak ada\n")
                pilih2 = input("Pilih : ")
                if pilih2 == "1":
                    gejala.append("Dada terasa sesak")

            elif pilih == "2":
                gejala.append("Sakit tenggorokan")

        # ===================== GEJALA DEMAM =====================
        if user_input == "2":
            gejala.append("Demam")
            print("Gejala tambahan?")
            print("1. Batuk")
            print("2. Mual")
            print("3. Sakit kepala")
            print("4. Sesak Napas\n")
            pilih = input("Pilih : ")

            # Batuk
            if pilih == "1":
                gejala.append("Batuk")
                print("\nGejala tambahan?")
                print("1. Hilang indera penciuman")
                print("2. Pilek")
                print("3. Sakit Tenggorokan")
                print("0. Tidak ada\n")
                pilih1 = input("Pilih : ")

                if pilih1 == "1": gejala.append("Hilang indera penciuman")
                elif pilih1 == "2": gejala.append("Pilek")
                elif pilih1 == "3": gejala.append("Sakit tenggorokan")

            # Mual
            if pilih == "2":
                gejala.append("Mual")
                print("\nGejala tambahan?")
                print("1. Nyeri belakang mata")
                print("0. Tidak ada\n")
                pilih1 = input("Pilih : ")
                if pilih1 == "1": gejala.append("Nyeri belakang mata")

            # Sakit kepala
            if pilih == "3":
                gejala.append("Sakit kepala")
                print("\nGejala tambahan?")
                print("1. Nafsu makan turun")
                print("0. Tidak ada\n")
                pilih1 = input("Pilih : ")
                if pilih1 == "1": gejala.append("Nafsu makan turun")

            # Sesak napas
            if pilih == "4":
                gejala.append("Sesak napas")
                print("\nGejala tambahan?")
                print("1. Nyeri dada saat bernapas")
                print("0. Tidak ada\n")
                pilih1 = input("Pilih : ")
                if pilih1 == "1": gejala.append("Nyeri dada saat bernapas")

        # ===================== GEJALA PUSING =====================
        if user_input == "3":
            gejala.append("Pusing")
            print("Gejala tambahan?")
            print("1. Demam")
            print("2. Mual\n")
            pilih = input("Pilih : ")
            if pilih == "1": gejala.append("Demam")
            elif pilih == "2": gejala.append("Mual")

        # ===================== GEJALA SAKIT PERUT =====================
        if user_input == "4":
            gejala.append("Sakit perut")
            print("Gejala tambahan?")
            print("1. Mual\n")
            pilih = input("Pilih : ")

            if pilih == "1":
                gejala.append("Mual")
                print("\nGejala tambahan lagi?")
                print("1. Kesulitan bernapas")
                print("0. Tidak ada\n")
                pilih2 = input("Pilih : ")
                if pilih2 == "1":
                    gejala.append("Kesulitan bernapas")

        # ======================== HASIL DIAGNOSA =========================
        clear()
        header()

        garis()
        print("🩺 HASIL PENYAKIT SEMENTARA")
        garis()
        print(f"Gejala yang Anda rasakan : {', '.join(gejala)}\n")

        # ===================== LOGIKA DIAGNOSA =====================

        if gejala == ["Batuk", "Sulit bernapas / napas cepat"]:
            hasil = "Asma"

        elif "Batuk" in gejala and "Sulit bernapas / napas cepat" in gejala and "Dada terasa sesak" in gejala:
            hasil = "Asma"

        elif "Batuk" in gejala and "Sakit tenggorokan" in gejala:
            hasil = "Flu"

        elif "Demam" in gejala and "Batuk" in gejala and "Hilang indera penciuman" in gejala:
            hasil = "COVID-19"

        elif "Demam" in gejala and "Batuk" in gejala:
            hasil = "Infeksi Saluran Pernapasan Akut (ISPA)"

        elif "Mual" in gejala and "Nyeri belakang mata" in gejala:
            hasil = "Demam Berdarah Dengue (DBD)"

        elif "Mual" in gejala:
            hasil = "Infeksi Saluran Pencernaan"

        elif "Sakit kepala" in gejala and "Nafsu makan turun" in gejala:
            hasil = "Tipes"

        elif "Sakit kepala" in gejala:
            hasil = "Flu"

        elif "Sesak napas" in gejala:
            hasil = "Infeksi Paru-Paru (Pneumonia)"

        elif "Pusing" in gejala and "Demam" in gejala:
            hasil = "Flu"

        elif "Pusing" in gejala and "Mual" in gejala:
            hasil = "Vertigo"

        elif "Sakit perut" in gejala and "Mual1" in gejala and "Kesulitan bernapas" in gejala:
            hasil = "Asam Lambung"

        elif "Sakit perut" in gejala and "Mual1" in gejala:
            hasil = "Masalah Pencernaan Umum"

        else:
            hasil = "Tidak diketahui / gejala tidak cocok"

        print(f"💡 Kemungkinan penyakit: {hasil}")
        garis()

    # ===================== TANYA ULANG =====================
    ulang = input("\nIngin mengecek lagi? (y/n) : ").lower()
    if ulang == "n":
        print("\nProgram ditutup. Terima kasih telah menggunakan aplikasi. 🙏")
        break
