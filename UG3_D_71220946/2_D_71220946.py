platuser = input("Masukkan Plat Nomor: ").split(' ')

try:
    plat = int(platuser[1])
    if plat >= 0 and plat <=3000:
        print("Plat nomor tersebut diperuntukan untuk mobil")
    elif plat >= 3001 and plat <= 4000:
        print("Plat nomor tersebut diperuntukan untuk motor")
    elif plat >= 4001 and plat <= 5000:
        print("Plat nomor tersebut diperuntukan untuk angkutan umum")
    elif plat >= 6000:
        print("Plat nomor tidak terindikasi ketiga angkutan tersebut ")
        
except:
    print("Plat nomor tidak terindikasi, setelah kode daerah harus berupa nomor kendaraan")