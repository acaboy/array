#deklarasi array
array = []
#membuat pariable total
total=0
#membuat variable n untuk menampung jumlah array
#n jumlah elemen
n = int(input("masukan jumlah elemen :"))
for x in range(n):
    #mengingputkan nilai
    nilai= float(input("masukan nilai ke-{}:".format(x+1)))
    array.append(nilai)
    print("\nhasil total adalah : {}".format(sum(array)))
    print("hasil rata rata nilai adalah : {}".format(sum(array)/n))