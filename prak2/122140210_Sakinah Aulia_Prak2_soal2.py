#soal 2: kendaraan
class Kendaraan:
    def __init__(self, nama, kecepatan_maksimum):
        self.nama = nama
        self._kecepatan = 0 # Kecepatan awal
        self.kecepatan_maksimum = kecepatan_maksimum
        print(f"{self.nama} dibuat.")

    def __del__(self):
        print(f"{self.nama} dihancurkan.")

    @property
    def kecepatan(self):
        return self._kecepatan

    def tambah_kecepatan(self, tambah):
        if self._kecepatan + tambah <= self.kecepatan_maksimum:
            self._kecepatan += tambah
            print(f"{self.nama} menambah kecepatan menjadi {self._kecepatan}.")
        else:
            print(f"Kecepatan maksimum {self.nama} telah tercapai.")

    def display_info(self):
        print(f"Informasi {self.nama}: Kecepatan = {self.kecepatan}, Kecepatan Maksimum = {self.kecepatan_maksimum}")


def main():
    while True:
        print("Selamat datang di Program Simulasi Kendaraan!")
        nama_kendaraan = input("Masukkan nama kendaraan: ")

        try:
            kecepatan_maksimum = int(input("Masukkan kecepatan maksimum kendaraan: "))
        except ValueError:
            print("Kecepatan maksimum harus berupa angka.")
            continue

        kendaraan = Kendaraan(nama_kendaraan, kecepatan_maksimum)

        while True:
            kendaraan.display_info()
            try:
                tambah_kecepatan = int(input("Tambah kecepatan (0 untuk keluar): "))
            except ValueError:
                print("Kecepatan harus berupa angka.")
                continue

            if tambah_kecepatan == 0:
                break

            kendaraan.tambah_kecepatan(tambah_kecepatan)

        play_again = input("Apakah Anda ingin membuat kendaraan lagi? (y/n): ")
        if play_again.lower() != 'y':
            print("Terima kasih sudah menggunakan program!")
            break


if __name__ == "__main__":
    main()
