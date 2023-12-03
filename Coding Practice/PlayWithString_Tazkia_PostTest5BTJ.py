'''
Post Test Coding - Python - Pertemuan 5 BTJ Academy
Tazkia Athariza
Case : Play with String
'''

# 1. Memisahkan string menjadi list

buah = 'apel,anggur,pepaya,semangka'
listbuah = buah.split(',') # memisahkan string dengan method split berdasarkan tanda koma
print(listbuah)

hewan = 'kucing warna oren'
listhewan = hewan.split() # memisahkan string dengan method split berdasarkan spasi
print(listhewan)

# Mengganti kata pada string

makan = "saya suka makan nasi goreng"
listmakan = makan.split() # memisahkan string berdasarkan spasi
listmakan = listmakan[:-2] # menghilangkan 2 elemen terakhir pada list
listmakan.append("pizza") # menambahkan elemen baru pada list
makanganti = ' '.join(listmakan) # menggabungkan list menjadi string kembali dengan method join
print(makan)
print(makanganti)

aksesoris = "saya pakai gelang"
listakses = aksesoris.split() 
listakses = listakses[:-1] # menghilangkan 1 elemen terakhir
listakses.append("jam") 
listakses.append("tangan")
aksesorisganti = ' '.join(listakses)
print(aksesoris)
print(aksesorisganti)

# Concatenating Strings

hari = "Hari ini"
cuaca = "cuaca cerah"
print(hari + " " + cuaca)

# 4. String Interpolation Concatenation

nama = "Tazkia"
umur = 22
perkenalan = "Halo, nama saya %s dan umur saya %d" % (nama, umur) # menyisipkan variabel dengan operator %
print(perkenalan)


# Formatting String

judul = "Python Programming"
penulis = "John Doe"
tahun = 2022
formatting = f"{judul}, ditulis oleh {penulis} pada tahun {tahun}"
print(formatting)

