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