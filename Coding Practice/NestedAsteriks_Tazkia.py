'''
Latihan Coding - Python - Pertemuan 6 BTJ Academy
Tazkia Athariza
Case : Nested Asteriks
'''

# 1. Membuat baris bintang
rows1 = int(input("Masukkan jumlah baris: "))

for x in range (rows1):
    print('*')

# 2. Membuat baris bintang dengan perulangan bersarang
rows2 = int(input("Masukkan jumlah baris untuk nested loop: "))

for x in range(rows2):
    for i in range(rows2):
        print('*', end="")
    print()

# 3. Membuat tangga bintang dengan nested loops
rows3 = int(input("Masukkan jumlah baris untuk tangga: "))

for x in range(rows3 + 1):
    for i in range(x):
        print('*', end="")
    print()

#. Membuat tangga bintang terbalik
rows4 = int(input("Masukkan jumlah baris untuk tangga terbalik: "))

for x in range(rows4, 0, -1):
    for i in range(rows4, x, -1):
        print('', end='')
    for r in range(1, x + 1):
        print('*', end='')
    print()


