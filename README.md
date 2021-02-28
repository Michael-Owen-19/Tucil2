i. Penjelasan Singkat algoritme Decrease and Conquer yang diimplementasikan:
   a. Dari graf (DAG) yang terbentuk, di hitung semua derajat-masuk (in-degree) setiap simpul, yaitu banyaknya busur yang masuk pada simpul tersebut.
   b. Pilih semua simpul yang memiliki derajat-masuk 0. 
   c. Ambil simpul tersebut, dan hilangkan simpul tersebut beserta semua busur yang keluar dari simpul tersebut pada graf, dan kurangi derajat simpul yang berhubungan dengan simpul tersebut dengan 1.
   d. Ulangi langkah (b) dan (c) hingga semua simpul pada DAG terpilih. 

ii. Requirement program :
	- Python3

iii. Cara menggunakan program:
	 - Buka CMD
	 - Pindah ke direktori tempat anda menyimpan kode bagian src
	 - Ketik python3 13519055.py
	 - Masukkan nama File atau Direktori file dokumen yang ingin di test yang terdapat pada file test
	 - Hasil akan ditampilkan ke layar
	 
iv. Author:
    Nama : Michael Owen
    NIM  : 13519055
    Kelas: K-01
