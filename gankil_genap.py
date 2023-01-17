#mengingput angka
angka = int(input("masukan angka : "))

#jika habis dibagi nol, maka genap
if (angka % 2) == 0 :
    print("{0} adalah bilangan genap".format(angka))
    
else:
    print("{0} adalah bilangan ganjil".format(angka))