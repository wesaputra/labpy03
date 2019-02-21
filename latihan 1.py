print ('Menampilkan n Bilangan Acak yang Lebih Kecil Dari 0.5')
jumlah =int (input( " Masukan Jumlah n : "))
import random
for i in range (jumlah) :
    print (" Data ke -> ", 1+i, "=",(random.uniform(0.1,0.5)))
print ("  SELESAI  ")