hargaBuah = [10000, 15000, 20000]
Apel= int(input('Apel:'))
Jeruk= int(input('Jeruk:'))
Anggur= int(input('Anggur:'))
Total=(Apel*int(hargaBuah[0])+Jeruk*int(hargaBuah[1])+Anggur*int(hargaBuah[2]))

print()
print('Detail Belanja')
print()
print('Apel \t :', Apel, 'x', int(hargaBuah[0]), '=', Apel*int(hargaBuah[0]))
print('Jeruk \t :', Jeruk, 'x', int(hargaBuah[1]), '=', Jeruk*int(hargaBuah[1]))
print('Anggur\t :', Anggur, 'x', int(hargaBuah[2]), '=', Anggur*int(hargaBuah[2]))
print()
print('Total Belanja :',Total)