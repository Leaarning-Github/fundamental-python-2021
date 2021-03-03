# KONTRUKSI DASAR PYTON
# SEQUENTIAL: Eksekusi berurutan
print('Hello World!')
print('by  Wahyu')
print('Tanggal 03 Maret 2021')
print('-' * 10)

# PERCABANGAN: Ekesekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('jalan lain')

# PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1): #jumlah perulangan = 5 - 1 = 4
    print(f'Halo anak #{index_anak}')
