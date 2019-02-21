# labpy03


# Latihan 1
 
# Program Sederhana Menampilkan n Bilangan Acak Yang Lebih Kecil Dari 0.5

- Algoritma Program Menampilkan n Bilangan Acak Yang Lebih Kecil Dari 0.5

  1. Masukan Jumlah n Pengulangan
  2. Proses pengulangan sesuai jumlah pengulangan yang diinputkan
  3. Tampilkan pengulangan dengan nilai di bawah 0.5
  4. Finish
  
    Setelah kita membuat Algoritma tersebut Maka Langkah selanjutnya membuat Flowchart program Menampilkan Bilangan Acak Yang Lebih Kecil Dari 0.5.
    
## Flowchart Program

![latihan 1](https://user-images.githubusercontent.com/46749030/53195089-7d0b9600-3647-11e9-8ac9-a25c55b5c13b.jpg)

## Program Menampilkan n Bilangan Acak Yang Lebih Kecil Dari 0.5

![latihan 1 py](https://user-images.githubusercontent.com/46749030/53195284-eab7c200-3647-11e9-9a96-6ef2530dd221.jpg)

    print ('Menampilkan n Bilangan Acak yang Lebih Kecil Dari 0.5')
    jumlah =int (input( " Masukan Jumlah n : "))
    import random
    for i in range (jumlah) :
        print (" Data ke -> ", 1+i, "=",(random.uniform(0.1,0.5)))
    print ("  SELESAI  ")

## Penjelasan Program

  1. *print ('Menampilkan n Bilangan Acak yang Lebih Kecil Dari 0.5')* Untuk Menampilkan atau Mencetak kalimat *Tampilkan n Bilangan Acak yang Lebih Kecil Dari 0.5
  2. *jumlah =int (input( " Masukan Jumlah n : "))* Untuk menentukan jumlah input yang di inginkan sesuai tipe data yaitu interger tipe data bilangan bulat
  3. *import random* Untuk pengulangan secara acak
  4. *for i in range (jumlah) :* Untuk Pengulangan dengan range jumlah
  5. *print (" Data ke -> ", 1+i, "=",(random.uniform(0.1,0.5)))* Untuk menampilkan atau mencetak urutan data sesuai jumlah inputan dengan hasil di bawah 0.5

#
#

# Latihan 2

# Program Sederhana Untuk Menampilkan bilangan Terbesar dari n buah data yang di Masukkan 

- Algoritma Program Sederhana Untuk Menampilkan bilangan Terbesar dari n buah data yang di Masukkan 

  1.	Start 
  2.	input bilangan n
  3.	Jika max < x maka akan lanjut pengulangan 
  4.	Jika x==0 maka akan berhenti proses pengulangan
  5.	Dan mencetak hasil nilai maxium dari n yang di isikan
  6.	Finish

  Setelah kita membuat Algoritma tersebut Maka Langkah selanjutnya membuat Flowchart program Sederhana Untuk Menampilkan bilangan Terbesar dari n buah data yang di Masukkan 
  
## Flowchart Program

![latihan 2](https://user-images.githubusercontent.com/46749030/53196316-5ef36500-364a-11e9-9c6f-8bb4174578f2.jpg)

## Program Sederhana Untuk Menampilkan bilangan Terbesar dari n buah data yang di Masukkan 

![latihan 2 py](https://user-images.githubusercontent.com/46749030/53196363-7d596080-364a-11e9-9fcd-c6c55a4b2524.jpg)

    print (' Bilangan Terbesar Dari n Buah Data Yang Dimasukan ')
    max = 0
    while True:
        x=int(input("Masukan Bilangan : "))
        if max < x:
            max = x
        if x==0:
            break
    print ("Bilangan Terbesar Adalah : ", max)
    
## Penjelasan program

  1. *print (' Bilangan Terbesar Dari n Buah Data Yang Dimasukan ')* Untuk menampilkan kalimat Menampilkan Bilangan Terbesar Dari n Buah Data Yang Diinputkan
  2. *max = 0* kode max disini untuk menentukan nilai max nya dalah 0
  3. *while True:* Untuk perulangan hingga waktu yang tidak di tentukan atau selamanya
  4. *x=int(input("Masukan Bilangan : "))* x untuk menginput tipe data interger ( bilangan bulat )
  5. *if max < x:* jika max kurang dari x maka max = x
  6. *if x==0: break* jika x= 0 maka akan berhenti dengan syarat break yang terpenuhi
  7. print ("Bilangan Terbesar Adalah : ", max) Menampilkan *Bilangan Terbesar Adalah : Nilai maxiumnya

#
#

# Program 1

# Program Sederhana Menghitung Total Keuntungan Selama 8 Bulan

- Algoritma Program Sederhana Menghitung Total Keuntungan Selama 8 Bulan

  1.	Start
  2.	Input modal misalkan n = 100.000.000 ( deklarasikan )
  3.	Input presentase untung A=0*n, B=0*n, C=0.01*n, D=0.01*n, E=0.05*n, F=0.05*n, G=0.05*n, H=0.03*n
  4.	For i in range (len (y))  pengulangan
  5.	Print (“keuntungan bulan ke “,i+1,”sebesar:” ,y[i])
  6.	Menghitung jumlah laba keseluruhan
      x= (A+B+C+D+E+F+G+H)
  7.	Print (“ Jumlah Keuntungan Selama 8 Bulan Adalah :”)
  8.	Finish
  
## Flowchart Program 
  
![program 3](https://user-images.githubusercontent.com/46749030/53197508-f8237b00-364c-11e9-8ff2-2e59bb2dc598.jpg)
  
## Program Program Sederhana Menghitung Total Keuntungan Selama 8 Bulan

![program 1 py](https://user-images.githubusercontent.com/46749030/53197700-4b95c900-364d-11e9-8510-fc0212365b4c.jpg)

    print ( 'Total Keuntungan Selama 8 Bulan Berjalannya Usaha' )

    #Modal Awal
    n=100000000
    print ("Awal Modal : ", n )

    #presentase Keuntungan
    A=0*n
    B=0*n
    C=0.01*n
    D=0.01*n
    E=0.05*n
    F=0.05*n
    G=0.05*n
    H=0.03*n

    y=[A,B,C,D,E,F,G,H]

    for i in range (len(y)):
        print (" Keuntungan Bulan ke ",i+1 , "-> ", y[i])

    x= (A+B+C+D+E+F+G+H)
    print (" Jumlah Keuntungan Selama 8 Bulan Adalah :",x)
    
## Penjelasan Program

  1. *print ( 'Total Keuntungan Selama 8 Bulan Berjalannya Usaha' )* Untuk Menampilkan kalimat Total Keuntungan Selama 8 Bulan Berjalannya Usaha
  2. *n=100000000* Dengan pemisalan atau dideklarasikan n adalah 100000000
  3. *print ("Awal Modal : ", n )* Menampilkan kalimat Modal Awal : dan data yang berisi di n yaitu 100000000
  4. *A=0*n, B=0*n, C=0.01*n, D=0.01*n, E=0.05*n, F=0.05*n, G=0.05*n, H=0.03*n* Untuk Mendeklarasikan presentase laba tiap bulan dan di kali dengan x atau data inputan modal investasi yaitu 100000000
  5. *y=[A,B,C,D,E,F,G,H]* untuk menentukan syarat y= yang berisi A,B,C,D,E,F,G,H
  6. *for i in range (len(y)): print (" Keuntungan Bulan ke ",i+1 , "-> ", y[i])* untuk perulangan data dengan isi data yaitu Y dengan menampilkan urutan laba perbulan sesuai range yang di tentukan dengan hasil ke untukan yang di inpput dari data Y
  7. *x= (A+B+C+D+E+F+G+H) print (" Jumlah Keuntungan Selama 8 Bulan Adalah :",x)* x berisi data penjumlahan data angka yang ada didalam kode A,B,C,D,E,F,G,H yang akan di tampilakan atau dicetak di jumlah laba selama 8 bulan

#
# NAMA  : WAHYU EKA SAPUTRA

# NIM   : 311810030

# KELAS : TI.18 B.1


![sekian](https://user-images.githubusercontent.com/46749030/53198559-40439d00-364f-11e9-804a-a4774ffcf7f5.jpg)
