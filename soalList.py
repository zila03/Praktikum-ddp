list_makanan = [
    ["bakwan","tempe","tahu"],                   
    ["nasi uduk", "nasi pecel", "sate padang"]          
]

# bagaimana memprint nasi pecel
print(list_makanan[1][1])

# print tahu
print(list_makanan[0][2])

# bagaimana memprint semuanya?
# harus keluar dari kotak

# for makanan in list_makanan:
#     # aksi buat for pertama
#     for detail_makanan in makanan:
#         # aaksi for kedua
#         print(detail_makanan)

for index1 in list_makanan[1]:
    print(index1)