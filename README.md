# ✈️ Sentani Airport (DJJ) Real-Time Flight Board

Website ini adalah papan informasi keberangkatan pesawat dari **Bandar Udara Sentani (DJJ)** yang diperbarui secara otomatis menggunakan Python.

### 🚀 Fitur & Teknologi
- **100% Python**: Logika pengambilan data dan generator HTML.
- **Automated**: Menggunakan **GitHub Actions** untuk update data setiap hari secara terjadwal.
- **Responsive Design**: Dibangun dengan **Bootstrap 5** dan tema Dark Mode yang profesional.
- **Serverless**: Di-host secara gratis di **GitHub Pages**.

### 🛠️ Cara Kerja
1. GitHub Actions menjalankan `main.py` sesuai jadwal (cron).
2. Skrip Python memproses data penerbangan terbaru.
3. Template HTML dirender menggunakan `Jinja2`.
4. Hasil render (`index.html`) di-push kembali ke repository untuk memperbarui tampilan web.
