# Informasi biodata mahasiswa
nama = "Zaki Tirta Ramadan"
nim = "09030582226024"
kelas = "TK4B"
mata_kuliah = "Praktikum Jaringan Komputer"

# Menampilkan biodata mahasiswa ke konsol
print("Biodata Mahasiswa")
print("Nama:", nama)
print("NIM:", nim)
print("Kelas:", kelas)
print("Mata Kuliah:", mata_kuliah)

with open("biodata_mahasiswa.txt", "w") as file:
    file.write("Biodata Mahasiswa\n")
    file.write("Nama: " + nama + "\n")
    file.write("NIM: " + nim + "\n")
    file.write("Kelas: " + kelas + "\n")
    file.write("Mata Kuliah: " + mata_kuliah + "\n")
