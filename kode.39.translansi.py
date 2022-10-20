# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
x = float(input("Tuliskan Nilai X : "))
y = float(input("Tuliskan Nilai Y: "))
a = float(input("Tuliskan Nilai Translasi A : "))
b = float(input("Tuliskan Nilai Translasi B: "))

# Mengkonversi
x1 = x + a
x2 = y + b 

# Menampilkan Hasil
print('==========================================================')
print('Maka Hasil Translasi A(%d,%d) Terhadap (%d,%d)' %(x,y,a,b))
print('Maka X* = %d'  %(x1))
print('Maka Y* = %d'  %(x2))
print('==========================================================')
