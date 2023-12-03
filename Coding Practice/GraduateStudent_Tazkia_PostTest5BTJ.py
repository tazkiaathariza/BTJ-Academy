'''
Post Test Coding - Python - Pertemuan 5 BTJ Academy
Tazkia Athariza
Case : Penentuan Lulus atau Tidaknya Mahasiswa

Pseudocode :
1. Mulai
2. Masukkan nama, nilai, dan absen
3. Jika nilai > 100 atau nilai < 0, status = "ERROR"
4. Jika nilai >= 75 dan absen < 4, status = "LULUS"
5. Jika nilai < 75 dan absen > 4, status = "TIDAK LULUS"
6. Tampilkan nama dan status
7. Selesai
'''

# membuat fungsi
def graduateornot(nama, nilai, absen):
    
    if nilai > 100 or nilai < 0:  #cek jumlah nilai valid atau tidak
        status = "ERROR! MASUKAN NILAI DALAM RENTANG 0 - 100"
    else:
        if nilai >= 75 and absen < 4:
            status = nama + " " + "dinyatakan LULUS"
        else:
            status = nama + " " + "dinyatakan TIDAK LULUS"

    return status

# menampilkan hasil
print(graduateornot("Tazkia", 85, 3))
print(graduateornot("Gollum", 75, 5))
print(graduateornot("Nave", 50, 3))
print(graduateornot("John", 106, 8))
