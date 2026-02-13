"""
1. Tambahkan nilai 95 ke dalam list.
2. Hapus nilai terendah dari list.
3. Urutkan list dari nilai terkecil ke terbesar.
4. Tampilkan nilai tertinggi, nilai terendah, dan jumlah data.
5. Hitung rata-rata nilai setelah semua perubahan.
6. Tampilkan seluruh isi list setelah diproses.
"""
print("Soal No 1.")
nilai = [75, 80, 65, 90, 85]
nilai.append(95)
nilai.sort()
nilai.pop(0)
print("urutan nilai dari yang terkecil hingga yang terbesar: ", nilai)
print("nilai terbesar: ", nilai[-1])
print("nilai terkecil: ", nilai[0])
print("jumlah data =", len(nilai))
i = 0
jumlah = 0
for i in range(0, len(nilai)):
    jumlah = jumlah + nilai[i]
rata = jumlah/len(nilai)
print("rata-rata =", rata)


"""
1. Tentukan keahlian yang dimiliki oleh kedua mahasiswa.
2. Tentukan keahlian yang hanya dimiliki mahasiswa A.
3. Tentukan seluruh keahlian unik dari kedua mahasiswa.
4. Periksa apakah "Java" termasuk keahlian mahasiswa B.
"""
print("Soal No 3.")
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}
i = 0
for i in range(0,len(keahlian_A)):
    if keahlian_A[i] == keahlian_B[i]:
        print(keahlian_A[i])


"""
1. Tampilkan nama mahasiswa Informatika yang memiliki IPK ≥ 3.5.
2. Hitung rata-rata IPK seluruh mahasiswa.
3. Tambahkan satu mahasiswa baru dengan:
NIM: M004
Nama: bebas
Prodi: bebas
IPK: bebas
4. Tampilkan kembali seluruh data mahasiswa setelah penambahan.
"""
print("Soal No 4.")
mahasiswa = {
"M001": {"nama": "Rina", "prodi": "Informatika", "ipk":
3.60},
"M002": {"nama": "Doni", "prodi": "Sistem Informasi",
"ipk": 3.25},
"M003": {"nama": "Lina", "prodi": "Informatika", "ipk":
3.80}
}
for x in mahasiswa.values():
    print(x)
for x in mahasiswa.keys():
    print(x)
for x in mahasiswa.items():
    print(x)

