# *Changelog*

## 26 November 2026

### Diubah

- Metadata *cache* dan `environment.json` disesuaikan dengan isi yang diminta spesifikasi.
- `progress.json` menyimpan indeks citra yang sudah diekstrak.

### Dijalankan

- *Run* `TRAIN` dan `VERIFY` di Colab (*runtime* CPU), semua pemeriksaan lolos.

## 25 November 2026

### Ditambahkan

- *Notebook* dengan mode `TRAIN` dan `VERIFY`, bagian 1–12.

### Diperbaiki

- Peringatan PyTorch soal *array* NumPy yang tidak *writable*. Indeks *split* sekarang disalin dengan `.copy()`.
- *Log* ekstraksi mencatat *cache* yang dilewati seolah diekstrak ulang.
- Kolom `student_id` terbaca sebagai angka saat CSV dibaca ulang. Sekarang dibaca sebagai *string*, lalu *training* diulang.
