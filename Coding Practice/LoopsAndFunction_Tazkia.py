'''
Latihan Coding - Python - Pertemuan 6 BTJ Academy
Tazkia Athariza
Case : Loops and Function
'''

# 1. Rentang angka: start = 1 dan end = 20. Tulis program menggunakan loop for untuk mencetak angka genap.

print("Angka genap :")
for e in range(1, 20):
    if e % 2 == 0: # bila dibagi 2 habis, berarti merupakan angka genap
        print(e)

# 2. Buat program yang menggunakan loop while untuk menemukan jumlah dari n angka alami pertama.

total = 0 # jumlah total di akhir
addingprocess = [] # proses penjumlahan n angka

number = 1 # deklarasi angka awal
while number <= 10: # kondisi
    total += number # adding
    addingprocess.append(total)
    number += 1

print("Step-step penjumlahan:", addingprocess)
print("Jadi, jumlah total adalah:", total)

# 3. Dengan loop for, iterasikan melalui string: my_string = 'Bangunindo' dan cetak setiap karakter.

my_btj = 'Bangunindo'

for i in my_btj:
    print(i)

# 4. Buat program yang menggunakan loop while untuk menghitung faktorial dari suatu angka num
factorial = 1

angka = 1
while angka <= 6:
    factorial = angka * factorial
    angka += 1

print("Faktorialnya adalah", factorial)

# 5. Buat program yang mengambil daftar angka dan mengembalikan jumlah dari semua elemen menggunakan loop for.

number_list = [1, 10, 3, 4, 5, 6, 7]
totalnum = 0
prosesadding = []

for x in number_list:
  totalnum += x
  prosesadding.append(totalnum)

print("Proses penjumlahan :", prosesadding)
print("Jadi total angka dalam list:", totalnum)

# 6. Buatlah sebuah fungsi bernama luas_persegi_panjang yang menerima dua parameter, panjang dan lebar

def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar 
    return luas

print("Luasnya adalah", luas_persegi_panjang(10, 5))
print("Luasnya adalah", luas_persegi_panjang(7, 3))

# 7. Tulis fungsi yang menerima satu parameter, bilangan bulat x, dan mengembalikan hasil kuadrat dari x.

def hitung_kuadrat(x):
    total = x ** 2
    return total

print("Hasil dari kuadrat 4 adalah", hitung_kuadrat(4))
print("Hasil dari kuadrat 5 adalah", hitung_kuadrat(5))

# 8.  Fungsi gabung_kata yang menerima dua string sebagai parameter dan mengembalikan hasil penggabungan keduanya dengan satu spasi.

def gabungkata(word1, word2):
    kalimat = word1 + " " + word2
    return kalimat

print(gabungkata("Selamat", "siang"))
print(gabungkata("Kota", "Palangkaraya"))

# 9. Fungsi yang menerima sebuah string dan mengembalikan jumlah huruf vokal dalam string tersebut.

def hitung_vokal(word):
    word_list = []

    for i in word:
     if i == "a" or i == "i" or i == "u" or i == "e" or i == "o":
        word_list.append(i)

    hasil = len(word_list)
    return hasil

print("Huruf vokal pada kata halo ada", hitung_vokal("halo"))
print("Huruf vokal pada kata halo ada", hitung_vokal("kenapa"))

# 10. Buatlah fungsi yang menerima satu parameter, bilangan bulat n, dan mengembalikan nilai faktorial dari n.

def hitungfaktorial(n):
    factorial = 1

    angka = 1
    while angka <= n:
        factorial = angka * factorial
        angka += 1
    
    return factorial

print("Faktorial dari 5 adalah", hitungfaktorial(5))
print("Faktorial dari 3 adalah", hitungfaktorial(3))

# 11. Fungsi yang dapat mengonversi suhu dari Celsius ke Fahrenheit

def celcius_to_fahrenheit(cel):
    fahrenheit = cel * 9/5 + 32
    return fahrenheit
   

print("Suhu dalam fahrenheit adalah", celcius_to_fahrenheit(0))
print("Suhu dalam fahrenheit adalah", celcius_to_fahrenheit(32))

# 12. Fngsi yang menerima satu parameter, jari-jari lingkaran, dan mengembalikan luas lingkaran tersebut.

def luas_lingkaran(jari):
    luaslingkaran = 3.14 * jari * jari
    return luaslingkaran

print("luas lingkaran :", luas_lingkaran(5))
print("luas lingkaran :", luas_lingkaran(2))

# 14. Fungsi yang menerima tiga parameter: a (elemen pertama), n (jumlah elemen), dan d (selisih). Fungsi ini harus mengembalikan jumlah dari deret aritmatika.

def deretaritmatika(a, n, s):
    list_deret = []
    
    for i in range(a, n, s):
        list_deret.append(i)
        
    print(list_deret)
    
    total = 0
    for x in list_deret:
        total += x
        
    return total
    
print(deretaritmatika(1, 9, 2))

# 15. Fungsi yang menerima satu parameter, bilangan bulat positif num, dan mengembalikan True jika num adalah bilangan prima, dan False jika sebaliknya.

def bilangan_prima(angka):
    hasil = None
    if angka < 2:
        hasil = "ERROR. Masukkan bilangan bulat positif"
    else:
        pembagi = 2
        while pembagi < angka:
            if angka % pembagi == 0:
                hasil = "False. Bukan bilangan prima"
                break  # keluar dari loop bila ditemukan bahwa hasil bukan bilangan prima
            pembagi += 1
        else:
            hasil = "True. Bilangan prima"
    return hasil

print(bilangan_prima(4))
print(bilangan_prima(5))
print(bilangan_prima(2))
print(bilangan_prima(7))
print(bilangan_prima(8))
