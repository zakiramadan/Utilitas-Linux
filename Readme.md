# Praktikum 7 Utilitas Linux

## TUJUAN

- Mengenal utilitas dasar Linux dan Unix
- Merangkaikan utilitas dengan pipe
- Mempelajari konsep delimiter

### 1. Tujuan dari Perintah `wc -l /etc/passwd` dan `wc -l /etc/group`

**Penjelasan:**

- Perintah `wc -l` digunakan untuk menghitung jumlah baris dalam sebuah file.
- `/etc/passwd` adalah file yang menyimpan informasi pengguna pada sistem Linux, sedangkan `/etc/group` adalah file yang menyimpan informasi grup pada sistem Linux.
- Tujuan dari perintah ini adalah untuk menghitung jumlah baris dalam file `/etc/passwd` dan `/etc/group`.

**Command:**

```bash
$ wc -l /etc/passwd
$ wc -l /etc/group
```

![App Screenshot](</Image/Nomor%20(1).png>)

![App Screenshot](</Image/Nomor%20(2).png>)

### 2. Membuat File Status dan Menggabungkannya dengan Mobil

**Penjelasan:**

- Perintah cat > status digunakan untuk membuat file bernama status dan memasukkan teks ke dalamnya.
- Teks yang dimasukkan adalah tanda hubung (-), kata "dijual", dan tanda hubung (-).
- Kemudian file status digabungkan dengan file mobil.db.

**Command:**

```bash
$ cat > status
-
-
dijual
-
dijual
-
```

![App Screenshot](</Image/Nomor%20(3).png>)

### 3. Mengganti Seluruh Huruf Hidup dari Teks Nyanyian dengan Huruf `o` Semua

Penjelasan:

- Perintah cat > burung digunakan untuk membuat file bernama burung dan memasukkan teks ke dalamnya.
- Tujuan dari perintah ini adalah untuk mengganti semua huruf hidup dalam teks nyanyian menjadi huruf "o" semua.

**Command:**

```bash
$ cat > burung
burung kakak tua
hinggap di jendela
nenek sudah tua
giginya tinggal dua
^D
```

![App Screenshot](<Nomor (4).png>)

Perintah ini membuat file `burung` dan mengisinya dengan teks tertentu.

### 4. Memeriksa /etc/passwd dan Mengambil Field ke-5 dengan Perintah cut

Penjelasan:
-vPerintah ini memeriksa file `/etc/passwd` yang menyimpan informasi pengguna pada sistem Linux.

- `-d:` digunakan untuk menentukan bahwa delimiter yang digunakan adalah tanda `:`.
- `-f5` digunakan untuk menentukan bahwa field yang ingin diambil adalah field ke-5.

**Command:**

```bash
$ cut -d: -f5 /etc/passwd
```

![App Screenshot](</Image/Nomor%20(5).png>)

### 5. Maksud dari Perintah who | cut -c 1 | sort | uniq | wc

Penjelasan:

- Perintah ini digunakan untuk menampilkan jumlah unik dari karakter pertama pada output perintah `who.`
- `who` digunakan untuk menampilkan informasi pengguna yang sedang masuk ke sistem.
- `cut -c 1` digunakan untuk mengambil karakter pertama dari setiap baris output.
- `sort` digunakan untuk mengurutkan karakter-karakter tersebut.
- `uniq` digunakan untuk menampilkan karakter-karakter unik.
- `wc` digunakan untuk menghitung jumlah karakter.

**Command:**

```bash
$ who | cut -c 1 | sort | uniq | wc
```

![App Screenshot](</Image/Nomor%20(6).png>)

## Kesimpulan

Dalam praktikum ini, telah dipelajari berbagai utilitas dasar Linux dan Unix serta cara penggunaannya. Beberapa utilitas yang dipelajari antara lain sort, pr, wc, tr, cut, head, tail, find, dan paste. Setiap utilitas memiliki fungsinya masing-masing, seperti pengurutan data, pemformatan teks, penghitungan kata, penggabungan file, dan pencarian file berdasarkan kriteria tertentu.

Dengan demikian, melalui praktikum ini diharapkan dapat meningkatkan pemahaman mengenai utilitas dasar Linux dan Unix serta kemampuan dalam menggunakan perintah-perintah tersebut secara efektif dalam lingkungan sistem operasi Linux.
