# Perulangan for

# angka = 5
# for i in range(angka):
#     i = i + 1
#     print("Perulangan ke -", i)

# # Perulangan while
# bil = 10

# while(bil <= 15):
#     print("Bilangan ", bil)
#     bil += 1
    

hasil_akhir = [
{'nama' : 'Reza', 'nilai' :70},
{'nama' : 'Ciut', 'nilai' :63},
{'nama' : 'Dian', 'nilai' :80},
{'nama' : 'Badu', 'nilai' :40}
]

for i in hasil_akhir:
    if i['nilai']>65:
        print(i['nama'])
