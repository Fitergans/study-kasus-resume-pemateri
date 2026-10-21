# Study Kasus 2 — Bridging Global Infrastructure to Address Local Challenges in HPC

## Permasalahan
Pengelola layanan lokal perlu memproses banyak catatan sensor secara cepat. Kasus ini membandingkan komputasi serial dengan multiprocessing untuk menghitung statistik blok data.

## Tujuan
- Memahami pemecahan tugas (task parallelism).
- Membandingkan waktu serial dan paralel.
- Menyadari bahwa paralel tidak selalu lebih cepat untuk data kecil karena overhead proses.

## Implementasi
Jalankan `python src/benchmark_hpc.py`. Program membuat data sintetis, menjalankan kalkulasi serial dan paralel, lalu menampilkan waktu eksekusi dan memastikan hasilnya sama.
