awal = int(input("Masukkan bilangan awal: "))
akhir = int(input("Masukkan bilangan akhir: "))

nomor = [str(i) if i % 6 != 0 and i % 8 != 0 else "" for i in range(awal, akhir+1)]

print(" ".join(nomor))
