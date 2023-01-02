# membuat dictionary menggunakan {key : value}
# data_diri = {"nama" : "Naazila"}

# print(data_diri["nama"])

# untuk mengakses valuenya aja, menggunakan function values()
nilai = {"firda":89, "inaya":78, "fawwaz":90, "rahmah":75}

# for i in nilai.values():
#     print(i)

# mengakses keys-nya saja
# for i in nilai.keys():
#     print(i)

# mencetak key dan values menggunakan items()
for nama,skor in nilai.items():
    print(nama, ":", skor)
