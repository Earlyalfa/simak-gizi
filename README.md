# NutriSi: Analisis Gizi Seimbang (Makan Bergizi Gratis)

NutriSi adalah sebuah platform berbasis web yang dirancang untuk mendukung standardisasi porsi gizi dalam program nasional Makan Bergizi Gratis (MBG). Dengan memanfaatkan teknologi Computer Vision, sistem ini mampu melakukan pemindaian otomatis (Scan) terhadap foto menu makanan dalam *ompreng* untuk mengevaluasi kelayakan gizi makro secara real-time berdasarkan standar Angka Kecukupan Gizi (AKG) Kemenkes.

---

## Anggota Tim (CC26-PSU323)
1. **Lipiya Agustina** (CDCC525D6X0303 )
2. **Early Alfa Sheilawati** (CDCC525D6X0093)
3. **Cheva Anggara Putra** (CACC589D6Y0471)
4. **Naraya Albani** (CACC129D6Y0171)
5. **Ana Setiawati** (CFCC899D6X1416) 
6. **Intan Mayangsari** (CFCC899D6X1100)

---

## Fitur Utama Dashboard
* **Otomatisasi Pemindaian Menu:** Menerjemahkan deteksi objek makanan dari kamera menjadi data nutrisi numerik siap olah.
* **Filter Parameter Program:** Navigasi taktis untuk menyesuaikan target gizi berdasarkan tingkat sekolah sasaran (TK, SD, SMP, SMA).
* **Audit Kelayakan Real-Time:** Klasifikasi otomatis status kecukupan gizi (Kurang, Layak Edar, Berlebih) beserta rekomendasi taktis untuk dapur umum.
* **Visualisasi Distribusi Gizi:** Grafik interaktif menggunakan Streamlit untuk memantau proporsi kalori, protein, lemak, dan karbohidrat.

---

## Tahap Pembersihan Data (Data Pre-processing)
Sebelum data hasil pemindaian dihitung oleh sistem dashboard, fungsi analisis data melakukan pembersihan otomatis untuk menjaga integritas data:
* **`drop_duplicates()`**: Mengeliminasi deteksi ganda akibat *glitch* pada kamera AI.
* **`.fillna(0)`**: Mengantisipasi nilai kosong (*missing values*) agar kalkulator dashboard tidak mengalami *crash*.
* **`.astype()`**: Mengunci konsistensi tipe data numerik untuk visualisasi grafik yang presisi.

---

## Cara Menjalankan Aplikasi Streamlit 

### 1. Prasyarat 
Sudah menginstal Python (versi 3.8 atau yang lebih baru).

### 2. Instalasi Library
Buka terminal atau command prompt (CMD), lalu instal *library* yang dibutuhkan dengan perintah:
```bash
pip install streamlit pandas matplotlib seaborn