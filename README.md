# Proyek Akhir IF5152 Visi Komputer

***Transfer Learning* pada Data Terbatas dan Gangguan Visual**

| | |
|---|---|
| Nama | Carlo Angkisan |
| NIM | 13523091 |
| Kartu | K09 |
| *Backbone* | MobileNetV2 (`IMAGENET1K_V1`), beku |
| Resolusi *input* | 128×128 |
| Augmentasi *training* | *Rotation*, *Brightness* |
| *Dataset* | CIFAR-10 |

## Deskripsi

Empat kondisi *training linear head* (E1–E4) dibandingkan: 250 atau 1000 citra *train*, masing-masing dengan dan tanpa augmentasi. Setiap kondisi dijalankan dengan *seed* 11, 22, dan 33, lalu diuji pada *test* bersih dan enam *test* terganggu.

## Isi berkas

| Berkas | Isi |
|---|---|
| `notebook_colab.ipynb` | *Notebook* beserta *output run* `TRAIN` |
| `report_ieee.pdf` | Laporan |
| `split_manifest.csv` | Pembagian data (2500 sampel) |
| `experiment_manifest.csv` | Konfigurasi 12 *run* |
| `metrics.csv` | Metrik 84 baris |
| `predictions.csv` | Prediksi dan probabilitas tiap sampel *test* |
| `environment.json` | Versi *library* dan perangkat |
| `requirements.txt` | Daftar *library* |
| `checksums.sha256` | *Checksum* artefak |
| `checkpoints/` | 12 *checkpoint* dan 3 *head* awal |
| `logs/` | *Log* ekstraksi dan *training* |
| `figures/` | Gambar dan tabel hasil |

## *Cache* fitur

*Cache* fitur tidak dimasukkan ke ZIP dan dapat diakses di [Google Drive](https://drive.google.com/drive/folders/1Ox8Ra50JjImQJtJEmXSWA5be5xnCIZSt?usp=sharing).

| *Cache* | Isi |
|---|---|
| `train_clean`, `train_aug` | Fitur 1000 citra *train*, bersih dan augmentasi |
| `val_clean` | Fitur 500 citra *validation* |
| `test_<kondisi>` | Fitur 1000 citra *test* untuk tiap kondisi (7 *cache*) |

Tiap *cache* berisi *chunk* maksimal 250 citra, `meta.json`, dan `progress.json`.

## Cara menjalankan

1. *Upload* `notebook_colab.ipynb` ke Google Colab.
2. Atur `MODE` di bagian 2.
   - `TRAIN`: menjalankan seluruh eksperimen.
   - `VERIFY`: menghitung ulang prediksi dan metrik dari artefak yang ada tanpa *training*.
3. Jalankan *Runtime* → *Run all*.

Hasil disimpan di `MyDrive/13523091_FinalCV/`. Untuk `VERIFY`, salin isi ZIP ke folder tersebut lalu letakkan *cache* di `feature_cache/`.

## Lingkungan *run*

| | |
|---|---|
| *Platform* | Google Colab versi gratis, *runtime* CPU |
| Waktu | 26 November 2026, 06.31–06.35 WIB |
| Detail | `environment.json` |

## Asumsi

1. Dua augmentasi kartu K09 diterapkan berurutan pada setiap citra *train*, yaitu rotasi lalu *brightness*. Dari `np.random.default_rng(2026 + original_index)`, nilai pertama dipakai untuk sudut rotasi dan nilai kedua untuk faktor *brightness*.
2. `sample_id` berformat `<split resmi>_<original_index>`, misalnya `train_00059` atau `test_00021`.
3. Kolom `subset` berisi `train`, `val`, atau `test`. *Train* terbatas ditandai dengan `is_low_data = 1`.
4. Baris tiap *subset* diurutkan berdasarkan `original_index`. "Dua belas sampel *test* pertama" mengikuti urutan ini.
5. Gambar dua belas sampel *test* pertama dan contoh kesalahan memakai prediksi E4 *seed* 11. Gambar dua belas sampel menampilkan kondisi bersih serta gelap, *blur*, dan rotasi tingkat sedang, sedangkan contoh kesalahan diambil dari *test* bersih.

## Penggunaan AI

Alat: Claude Code.

- Membantu proses pengembangan kode, yang hasilnya telah ditinjau dan divalidasi kembali oleh penulis.
- Membantu penyuntingan laporan, meliputi perbaikan ejaan dan tata bahasa.
- Membantu pencarian referensi artikel ilmiah (paper).
