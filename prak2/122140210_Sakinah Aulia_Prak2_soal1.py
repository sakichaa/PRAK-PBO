#soal 1 mahasiswa
class Mahasiswa:
    def __init__(self, nim, nama, angkatan, is_mahasiswa=True):
        self._nim = nim
        self._nama = nama
        self.angkatan = angkatan
        self.is_mahasiswa = is_mahasiswa
        self._lulus_skripsi = False

    def get_nim(self):
        return self._nim

    def set_nim(self, nim):
        self._nim = nim

    def get_nama(self):
        return self._nama

    def set_nama(self, nama):
        self._nama = nama

    def set_lulus_skripsi(self, lulus_skripsi):
        self._lulus_skripsi = lulus_skripsi

    def display_info(self):
        return f"NIM: {self.get_nim()}, Nama: {self.get_nama()}, Angkatan: {self.angkatan}, " \
               f"Status Mahasiswa: {'Aktif' if self.is_mahasiswa else 'Nonaktif'}, " \
               f"Lulus Skripsi: {'Ya' if self._lulus_skripsi else 'Belum'}"

    def hitung_panjang_nama(self):
        return len(self._nama)

    def cek_status_lulus(self):
        if self.angkatan <= 2022:
            if self._lulus_skripsi:
                return "Mahasiswa sudah lulus"
            else:
                return "Mahasiswa belum lulus (Belum lulus skripsi)"
        elif self.is_mahasiswa:
            return "Mahasiswa masih aktif (Belum waktunya sidang)"
        else:
            return "Mahasiswa nonaktif"

mahasiswa1 = Mahasiswa(nim="1222140210", nama="Ica", angkatan=2022, is_mahasiswa=True)
mahasiswa2 = Mahasiswa(nim="12340000", nama="Taylor", angkatan=1980)

mahasiswa1.set_lulus_skripsi(True)

print(mahasiswa1.display_info())
print(mahasiswa1.cek_status_lulus())

print("\n")

print(mahasiswa2.display_info())
print(mahasiswa2.cek_status_lulus())
