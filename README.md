# GitHub Contribution Graph Automation

Skrip otomatis untuk menjaga grafik kontribusi GitHub tetap hijau dengan membuat commit harian secara terjadwal.

## Struktur Proyek

- `.github/workflows/contrib-scheduler.yml` - GitHub Actions workflow untuk jadwal commit
- `scripts/commit-and-push.sh` - Skrip Bash untuk membuat perubahan
- `scripts/commit-and-push.py` - Skrip Python sebagai alternatif
- `contrib.txt` - File yang diperbarui setiap hari untuk menciptakan commit

## Persiapan dan Konfigurasi

### Opsi 1: Menggunakan GitHub Personal Access Token (PAT) - Disarankan

**Kelebihan:**
- Commit akan muncul sebagai Anda, bukan sebagai github-actions[bot]
- Commit akan terhitung dalam grafik kontribusi

**Kekurangan:**
- Memerlukan pembuatan token dengan akses

**Langkah-langkah:**

1. **Buat Personal Access Token (PAT) baru:**
   ```bash
   # Kunjungi: https://github.com/settings/tokens
   # Klik "Generate new token" -> "Generate new token (classic)"
   ```

2. **Setel scope minimal (paling aman):**
   - `repo` - Untuk mengakses repositori pribadi dan publik
   - `workflow` - Untuk mengupdate GitHub Actions
   - `read:org` - Jika repositori Anda di organisasi

3. **Simpan PAT sebagai Secret di repositori Anda:**
   - Buka repositori Anda di GitHub
   - Klik tab "Settings"
   - Dari sidebar kiri, pilih "Secrets and variables" > "Actions"
   - Klik "New repository secret"
   - Nama secret: `GH_PAT`
   - Isi secret: Paste PAT yang Anda buat sebelumnya
   - Klik "Add secret"

4. **Setel identitas Git (opsional tapi disarankan):**
   - Tambahkan dua secret tambahan:
     - Nama: `GIT_USER_NAME`, Isi: Nama GitHub Anda (misal: `johndoe`)
     - Nama: `GIT_USER_EMAIL`, Isi: Email yang terhubung ke akun GitHub Anda (misal: `johndoe@example.com`)

### Opsi 2: Menggunakan GITHUB_TOKEN (built-in)

**Kelebihan:**
- Tidak perlu membuat token tambahan
- Sudah tersedia secara otomatis

**Kekurangan:**
- Commit mungkin muncul sebagai `github-actions[bot]`
- Commit oleh bot TIDAK SELALU dihitung dalam grafik kontribusi
- Hanya commit dari akun nyata yang dihitung dalam grafik kontribusi

**Catatan penting tentang GITHUB_TOKEN:**
- Jika menggunakan GITHUB_TOKEN, pastikan `GIT_USER_NAME` dan `GIT_USER_EMAIL` cocok dengan akun GitHub Anda
- Namun, commit oleh `github-actions[bot]` tidak akan menampilkan grafik kontribusi hijau untuk akun Anda

## Konfigurasi Jadwal (Cron)

Jadwal saat ini diatur untuk berjalan setiap hari pukul 09:00 UTC:

```yaml
schedule:
  - cron: '0 9 * * *'
```

Untuk mengubah jadwal, ubah format cron sesuai kebutuhan:
- `0 9 * * *` = Setiap hari pukul 09:00 UTC
- `0 15 * * *` = Setiap hari pukul 15:00 UTC
- `0 9 * * 1-5` = Setiap hari kerja (Senin-Jumat) pukul 09:00 UTC

Lihat [crontab.guru](https://crontab.guru/) untuk bantuan membuat format cron.

## Pengujian Workflow

1. **Manual run (untuk pengujian):**
   - Buka tab "Actions" di repositori Anda
   - Temukan workflow "Daily Contribution Scheduler"
   - Klik "Run workflow" atau "Run workflow manually"
   - Cek log untuk memastikan semuanya berjalan dengan baik

2. **Cek grafik kontribusi:**
   - Kunjungi profil GitHub Anda: `https://github.com/username`
   - Cek apakah ada blok hijau yang baru muncul

## Aturan Grafik Kontribusi GitHub

Grafik kontribusi menghitung commit berdasarkan:

1. **Identitas penulis:** Email di commit harus cocok dengan email yang terhubung ke akun GitHub Anda
2. **Branch:** Commit harus di default branch atau branch lain yang dihitung
3. **Waktu:** Commit harus dilakukan dalam rentang waktu 24 jam terakhir
4. **Repositori publik:** Kontribusi di repositori publik lebih diutamakan
5. **Akun nyata:** Commit dari bot mungkin tidak dihitung sebagai kontribusi individu

## Variasi untuk Tampilan "Alami"

Jika ingin membuat commit terlihat lebih alami (acak), Anda bisa:
- Mengubah skrip commit-and-push.sh untuk menambahkan beberapa entri per hari
- Mengacak waktu jadwal cron (misalnya acak antara jam 8-10 pagi)
- Mengganti pesan commit dengan berbagai pesan (bug fix, enhancement, documentation, dll.)

## Security dan Etika

⚠️ **PERINGATAN:** Gunakan solusi ini hanya untuk:
- Repositori pribadi Anda
- Repositori yang Anda miliki
- Repositori yang diperuntukkan khusus untuk grafik kontribusi

Jangan gunakan untuk:
- Menipu grafik kontribusi di repositori orang lain
- Melakukan commit ke repositori milik orang lain tanpa izin
- Melanggar kebijakan GitHub

## Troubleshooting

Jika workflow gagal:
1. Cek log Actions untuk melihat error
2. Pastikan PAT memiliki scope yang benar
3. Pastikan email di `GIT_USER_EMAIL` cocok dengan akun GitHub Anda
4. Pastikan workflow memiliki akses untuk push ke default branch

## File dan Environment

File contoh:
```
example.env
GH_PAT=your_personal_access_token_here
GIT_USER_NAME=your_github_username
GIT_USER_EMAIL=your_github_email@example.com
```

## Catatan Teknis

- Solusi ini membuat perubahan kecil ke file `contrib.txt` setiap hari
- Perubahan ini cukup untuk membuat commit yang akan dihitung dalam grafik kontribusi
- Pastikan repositori publik untuk hasil terbaik dalam grafik kontribusi