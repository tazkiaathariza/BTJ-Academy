'''
Latihan Coding - Python - Pertemuan 6 BTJ Academy
Tazkia Athariza
Case : Inventory Management
'''

# Inventaris awal kosong
inventaris = []

# Fungsi untuk menambahkan produk ke inventaris
def tambah_produk(nama, harga, jumlah):
    product = {'Name': nama, 'Price': harga, 'Amount': jumlah} # inisiasi dictionary baru
    inventaris.append(product) # push ke dalam list
    hasil = "Produk Berhasil Ditambahkan!" # notifikasi
    return hasil

# Coba tambah produk :
print(tambah_produk("Kentang", 3000, 4))
print(tambah_produk("Udang", 7000, 8))
print(tambah_produk("Ayam", 5000, 7))
print("Inventaris terbaru setelah produk ditambahkan:", inventaris)

# Fungsi untuk memperbarui jumlah produk
def perbarui_jumlah(nama_produk, jumlah_baru):
    for x in inventaris:
        if x['Name'] == nama_produk: # mencari elemen berdasarkan 'Name'
            x['Amount'] = jumlah_baru # ganti jumlah
    hasil = "Produk Berhasil Diperbaruhi!"
    return hasil

# Coba Perbaruhi :
print(perbarui_jumlah("Kentang", 777))
print(perbarui_jumlah("Ayam", 99))
print("Inventaris terbaru setelah diperbaruhi :", inventaris)

# Fungsi untuk menampilkan inventaris saat ini
def tampilkan_inventaris():
    print("Inventaris Saat Ini:")
    for x in inventaris:
        print(x)

tampilkan_inventaris()

# Fungsi untuk menghitung total nilai inventaris
def hitung_total_nilai():
    total_nilai = 0
    for x in inventaris:
        nilai = x['Price'] * x['Amount']
        total_nilai += nilai
    return total_nilai
   
print("Total nilai inventaris: ", hitung_total_nilai())
