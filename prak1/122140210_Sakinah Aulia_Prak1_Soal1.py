bot= int(input("Batas Bawah : "))
up = int(input("Batas Atas : "))

if bot < 0 or up < 0 :
    print("Batas bawah dan atas yang dimasukan tidak boleh di bawah nol")
else :
    sum = 0
    for x in range (bot, up) :
        if x % 2 == 1 :
            print(x)
            sum += x
    print("Total : ", sum)
