# Study Kasus 6 — Attributing Direct Drivers to Deforestation Alerts with Satellite Imagery and AI

## Permasalahan
Tim lingkungan ingin memahami bagaimana perubahan tutupan vegetasi dapat ditandai dari dua citra pada waktu berbeda dan bagaimana konteks dapat dipakai untuk meninjau kemungkinan penyebab.

## Tujuan
- Membuat demonstrasi perubahan indeks vegetasi dari citra sintetis.
- Menandai piksel yang mengalami penurunan nilai.
- Menghasilkan ringkasan area perubahan.
- Menekankan bahwa penyebab deforestasi tidak dapat ditentukan hanya dari perubahan spektral.

## Implementasi
Jalankan `python src/deteksi_perubahan.py`. Program menghasilkan CSV piksel dan ringkasan perubahan. Nilai citra dibuat secara sintetis; bukan citra satelit aktual dan bukan sistem peringatan deforestasi operasional.

## Pengembangan lanjutan
Gunakan citra Sentinel-2/Landsat yang sudah diproses, hitung NDVI, lakukan masking awan, validasi sampel, dan kombinasikan data konteks (misalnya kedekatan jalan/permukiman dan izin penggunaan lahan) untuk menguji hipotesis penyebab. Semua dugaan penyebab harus diverifikasi.
