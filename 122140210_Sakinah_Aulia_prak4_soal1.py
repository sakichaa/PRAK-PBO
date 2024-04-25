class Hewan:
  def __init__(self, nama, jenis_kelamin):
    self.nama = nama
    self.jenis_kelamin = jenis_kelamin

  def bersuara(self):
    pass  # Metode ini akan ditimpa oleh kelas turunan

  def makan(self):
    print(f"{self.nama} sedang makan.")

  def minum(self):
    print(f"{self.nama} sedang minum.")

class Kucing(Hewan):
  def __init__(self, nama, jenis_kelamin):
    super().__init__(nama, jenis_kelamin)

  def bersuara(self):
    print(f"Kucing {self.nama} bersuara: Meong!")
    
  def makan(self):
    print(f"kucing {self.nama} sedang makan: tulang" )

class Anjing(Hewan):
  def __init__(self, nama, jenis_kelamin):
    super().__init__(nama, jenis_kelamin)

  def bersuara(self):
    print(f"Anjing {self.nama} bersuara: Guk Guk!")
    
  def makan(self):
    print(f"anjing {self.nama} sedang makan: tulang" )

# Contoh penggunaan
hewan1 = Kucing("Kiki", "Betina")
hewan2 = Anjing("Ichi", "Jantan")

print(hewan1.nama)  #Output: Kiki
print(hewan2.nama)  #Output: Ichi

hewan1.bersuara()  #Output: Kucing Kiki bersuara: Meong!
hewan1.makan()     #Output: Kiki sedang makan: tulang
hewan2.bersuara()  #Output: Anjing Ichi bersuara: Guk Guk!
hewan2.makan()     #Output: Ichi sedang makan: tulang
