'''
Post Test Coding - Python - Pertemuan 5 BTJ Academy
Tazkia Athariza
Case : Penentuan Grade Mahasiswa
'''

# fungsi untuk dipanggil kembali
def gradingnilai(nilai):
    
    # pengkondisian nilai

    if nilai >= 80 and nilai <= 100:
        grade = "A"
    elif nilai >= 65 and nilai <= 79:
        grade = "B"
    elif nilai >= 50 and nilai <= 64:
        grade = "C"
    elif nilai >= 35 and nilai <= 49:
        grade = "D"
    elif nilai < 35 and nilai >= 0:
        grade = "E"
    else:
        grade = "Nilai invalid! Masukkan nilai dengan rentang 0 - 100"
    
    return grade

# menampilkan contoh nilai dan hasil grading
print(gradingnilai(115)) # nilai invalid
print(gradingnilai(95)) # grade A
print(gradingnilai(50))
print(gradingnilai(65))
print(gradingnilai(49))
print(gradingnilai(0))
print(gradingnilai(-5)) # nilai invalid
    