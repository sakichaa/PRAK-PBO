jari_jari = int(input("jari-jari : "))
phi = 3.14

if jari_jari < 0 :
    print("jari-jari lingkaran tidak boleh negatif")
else :
    luas = phi * jari_jari ** 2
    keliling = 2 * phi * jari_jari

    print("Luas : ", luas)
    print("Keliling : ", keliling)
