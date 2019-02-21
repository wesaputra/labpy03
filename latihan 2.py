print (' Bilangan Terbesar Dari n Buah Data Yang Dimasukan ')
max = 0
while True:
    x=int(input("Masukan Bilangan : "))
    if max < x:
        max = x
    if x==0:
        break
print ("Bilangan Terbesar Adalah : ", max)
