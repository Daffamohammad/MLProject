Latar Belakang
------------------------------------------------------------------------------------
Nilai tukar dianggap sebagai aspek penting dalam perdagangan internasional yang besar
karena globalisasi perusahaan. Nilai perdagangan internasional sangat besar, dan bahkan
fluktuasi kecil dalam nilai tukar, bahkan desimal, dapat memiliki efek yang besar.
Perubahan kecil dalam nilai tukar dapat berdampak besar, dan penjual mungkin harus
membayar lebih dari jumlah yang disepakati. Prediksi nilai tukar memiliki peran penting
dalam membantu pengambilan keputusan strategis, mulai dari investasi, perdagangan
internasional, hingga manajemen risiko ekonomi. Namun, kurs mata uang bersifat dinamis
dan dipengaruhi oleh berbagai faktor internal dan eksternal, seperti kebijakan moneter,
sentimen pasar, dan faktor geopolitik.

Pendekatan Model
------------------
Dalam proyek ini, kami menggunakan dua jenis model regresi, yaitu Linear Regression dan Ridge
Regression, untuk memprediksi kurs mata uang berdasarkan data time-series. Pemilihan model ini
didasarkan pada kemampuan keduanya dalam menangani data dengan dimensi yang sederhana, serta
kemampuan Ridge Regression dalam mengatasi multicollinearity melalui regulasi.

Dataset
-------
Dataset yang digunakan bersumber dari situs resmi Bank Indonesia. Data ini mencakup nilai tukar harian mata uang target terhadap Dolar Amerika Serikat (USD) selama lima tahun terakhir, yaitu dari tahun 2019 hingga 2023. Untuk analisis ini, kami memanfaatkan 1.396 hari terakhir sebagai data utama, setelah dilakukan proses pembersihan dan preprocessing.

Hasil
------
 1. Residual Plot Pada model Linear Regression, residual yang tersebar di sekitar garis horizontal menunjukkan bahwa model mampu menangkap pola data dengan baik.  Pada Ridge Regression, residual menunjukkan distribusi yang lebih kompleks, mengindikasikan kemungkinan underfitting atau bahwa model lebih fokus pada generalisasi.
 2. Evaluation Metrics Model linear memiliki MSE lebih rendah dan R2 lebih tinggi dibanding model ridge, menunjukkan performa yang lebih baik dalam memprediksi data. Ridge regression menghasilkan cross-validated MSE yang lebih kecil dibanding linear regression, menunjukkan kemampuan generalisasi yang lebih baik.

Diskusi
--------
Model linear yang kami buat mampu mendapatkan hasil dengan akurasi yang tinggi, yang tercermin pada R-squared score. Namun, perlu digarisbawahi kami menyadari bahwa R-Squared score belum dalam konteksi model prediksi machine learning tentu baik, dalam kasus ini kami mungkin menghadapi overfitting. Apa itu overfitting? Overfitting terjadi ketika model terlalu "belajar" dari data pelatihan, sehingga mampu menangkap noise atau detail kecil dalam data tersebut, namun gagal menangkap pola yang lebih umum. Dalam kasus overfitting, model memiliki performa yang sangat baik pada data pelatihan tetapi buruk pada data baru (set pengujian). Oleh karena itu, kami mencoba membuat model alternatif dengan menggunakan ridge regression dengan parameter yang kami set tinggi (200), menghasilkan hasil evaluasi yang lebih dapat diterima dengan acuan R-Squared maksimal 90%. Residual yang tersebar acak adalah indikator bahwa model menangkap pola yang sebenarnya dan tidak mengabaikan hubungan penting dalam data. Selisih kecil Cross-Validated MSE—MSE antara kedua metrik berarti model tidak hanya "belajar" dari data pelatihan tetapi mampu mempertahankan performa yang serupa pada data validasi.
