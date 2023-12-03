'''
Post Test Coding - Python - Pertemuan 5 BTJ Academy
Tazkia Athariza
Case : Pengunjung Bar
'''

# fungsi untuk dipanggil kembali

def barvisitor(nama, umur, uang):

    if nama == None: # persyaratan nama
        print("Anda tidak boleh masuk! isi nama terlebih dahulu")
    else:
        if umur < 17: # persyaratan umur
            if uang < 50000: # persyaratan uang
                print("Anda harus pulang! Uang tidak cukup. Harga jus 50 ribu")
            else:
                sisauang = uang - 50000
                print("Kembalian anda = ", sisauang)
        else:
            if uang < 300000:
                print("Anda harus pulang! Uang tidak cukup. Harga anggur 300 ribu")
            else:
                sisauang = uang - 300000
                print("Kembalian anda = ", sisauang)


# menampilkan hasil
barvisitor(None, 18, 350000)
barvisitor("Tazkia", 16, 25000)
barvisitor("Tazkia", 16, 80000)
barvisitor("Tazkia", 18, 75000)
barvisitor("Tazkia", 18, 350000)
