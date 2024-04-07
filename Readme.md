# Tugas Praktikum 7 Utilitas Linux

Berikut adalah beberapa perintah dasar yang sering digunakan di Linux beserta penjelasannya:

1. **Menghitung Jumlah Baris pada File `/etc/passwd`**

   ```bash
   $ wc -l /etc/passwd
   ```

   Perintah ini digunakan untuk menghitung jumlah baris pada file `/etc/passwd`.

2. **Menghitung Jumlah Baris pada File `/etc/group`**

   ```bash
   $ wc -l /etc/group
   ```

   Perintah ini digunakan untuk menghitung jumlah baris pada file `/etc/group`.

3. **Membuat dan Mengedit File `burung`**

   ```bash
   $ cat > burung
   burung kakak tua
   hinggap di jendela
   nenek sudah tua
   giginya tinggal dua
   ^D
   ```

   Perintah ini membuat file `burung` dan mengisinya dengan teks tertentu.

4. **Mengambil Field ke-5 dari File `/etc/passwd` dengan Perintah `cut`**

   ```bash
   $ cut -d: -f5 /etc/passwd
   ```

   Perintah ini digunakan untuk memperoleh field ke-5 dari setiap baris pada file `/etc/passwd`. Opsi `-d:` digunakan untuk menetapkan delimiter sebagai tanda ':' karena file tersebut terstruktur dengan delimiter tersebut.

5. **Menghitung Jumlah Karakter Unik pada Karakter Pertama dari Output `who`**
   ```bash
   $ who | cut -c 1 | sort | uniq | wc
   ```
   Perintah ini digunakan untuk melihat siapa yang sedang login, mengambil karakter pertama dari setiap baris output, mengurutkan karakter-karakter tersebut, menghilangkan baris yang sama agar hanya ada satu salinan setiap karakter, dan menghitung jumlah karakter yang unik.

---

Dengan memahami dan menggunakan perintah-perintah dasar di atas, Anda dapat melakukan berbagai tugas administratif dan analisis file di sistem Linux dengan lebih efisien.
