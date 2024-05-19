/* 
Matematika Diskrit Materi 04 Penggunaan Fungsi dengan Python Praktikum 4
by hafizhhasyhari
*/

# Fungsi Perkalian
def perkalian(x, y):
    return x * y

# Fungsi Pembagian 
def pembagian(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Fungsi Penjumlahan
def penjumlahan(x, y):
    return x + y

# Fungsi Pengurangan 
def pengurangan(x, y):
    return x - y

# Contoh Nilai Variabel
x = 19
y = 6

# Menjalankan program dengan contoh nilai variabel 
print("Contoh Penggunaan Fungsi")
print("Perkalian :", x, "x", y, "=", perkalian(x, y))
print("Pembagian :", x, "/", y, "=", pembagian(x, y))
print("Penjumlahan :", x, "+", y, "=", penjumlahan(x, y))
print("Pengurangan :", x, "-", y, "=", pengurangan(x, y))
