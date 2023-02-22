curah = float(input("Masukkan nilai curah hujan: "))

if curah <= 0:
    print("Curah Terang/Berawan")
elif curah > 0.5 and curah < 20:
    print("Curah hujan ringan")
elif curah >= 50 and curah <=100:
    print("Curah hujan lebat")
elif curah >= 100:
    print("Curah hujan extreme")

else :
    print("Curah hujan belum teridentifikasi")