# Study Kasus 1 — Make Sense of Data with Analytics and AI

## Permasalahan
Sebuah UMKM ingin memahami pola penjualan dan memperkirakan penjualan periode berikutnya berdasarkan data transaksi bulanan.

## Tujuan
- Menghitung ringkasan penjualan.
- Menemukan produk dengan penjualan tertinggi.
- Membuat prediksi baseline menggunakan regresi linear.

## Implementasi
Dataset contoh berada di `data/penjualan.csv`. Jalankan:
```bash
pip install -r requirements.txt
python src/analisis_penjualan.py
```
Program menampilkan ringkasan total penjualan per produk dan prediksi sederhana. Dataset kecil ini hanya untuk demonstrasi; hasil prediksi bukan jaminan penjualan aktual.
