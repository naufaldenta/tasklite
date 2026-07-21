# Findings & Decisions

## Requirements
- Pelajari file `Dhendra_Marutho_UAS_Cloud_Computing.docx` dan deskripsi pengguna secara menyeluruh.
- Buat planning terlebih dahulu sebelum implementasi proyek.
- Sertakan tutorial penyiapan environment localhost untuk Windows 11 yang belum memiliki Docker maupun Kubernetes.
- Rancang aplikasi CRUD multi-container yang sangat ringan tetapi memenuhi seluruh kriteria UAS.
- Minimal ada container aplikasi dan container database yang dikelola Docker Compose.
- Gunakan persistent volume, environment variable, health check, automated testing, GitHub repository, dan GitHub Actions CI/CD.
- Kubernetes, VPS, dan layanan cloud berbayar tidak wajib.
- Repository perlu memiliki riwayat commit yang menunjukkan perkembangan.

## Research Findings
- Dokumen UAS terdiri dari 3 halaman dan seluruh konten utama berada dalam tabel besar; hasil render Microsoft Word terlihat utuh tanpa clipping atau overlap yang menghilangkan ketentuan.
- Pembobotan capaian: CPMK-102 implementasi 70 poin dan CPMK-041 analisis/pemahaman 30 poin.
- Komponen wajib implementasi: CRUD + validasi + database; Dockerfile/image; Compose minimal app+database; port, network, `depends_on`, restart policy; named volume; `.env` dan `.env.example`; health check; minimal 3 automated test; Actions berisi checkout, install dependency, test, dan Docker build.
- Wajib menyimpan bukti satu workflow gagal dan satu workflow berhasil setelah perbaikan.
- Analisis wajib menjelaskan hubungan app/image/container/Compose/network/volume/CI-CD; manfaat multi-container; risiko tanpa volume; testing sebagai quality gate; dampak kegagalan service dan pemulihan; rancangan migrasi ke cloud.
- Luaran: repository GitHub, dua link workflow, laporan PDF 10-15 halaman, video 7-10 menit, diagram arsitektur, dan presentasi maksimal 8 slide.
- Demo wajib menampilkan versi Docker/Compose, `up -d`, `ps`, CRUD yang terhubung database, persistensi setelah `down` lalu `up`, test lokal, workflow gagal+perbaikan+berhasil, health check, dan simulasi gangguan.
- Rubrik final memberi bobot: fungsi+DB 10%, desain/arsitektur 10%, Dockerfile/image 10%, Compose/multi-container 15%, network/volume/env 10%, testing 10%, pipeline 15%, health/simulasi 5%, laporan/README/repo 5%, presentasi/video/pemahaman 10%.
- Docker Desktop resmi saat ini merekomendasikan mode per-user dan backend WSL 2 untuk mayoritas pengguna Windows; WSL minimum 2.1.5, Windows 11 64-bit yang didukung, virtualisasi hardware, dan 8 GB RAM tercantum sebagai prasyarat.
- Microsoft mendokumentasikan instalasi WSL dari PowerShell Administrator menggunakan `wsl --install`, kemudian restart; WSL baru memakai versi 2 secara default.
- Docker Compose tidak menunggu database benar-benar siap hanya karena container berjalan. `depends_on` dengan `condition: service_healthy` membuat aplikasi menunggu health check database lulus.
- GitHub Actions workflow disimpan sebagai YAML di `.github/workflows` dan dapat dipicu oleh push/pull request.

## Technical Decisions
| Decision | Rationale |
|----------|-----------|
| Gunakan aplikasi web server-rendered, bukan frontend terpisah | Memenuhi CRUD dengan satu container aplikasi dan mengurangi RAM, dependency, serta kompleksitas demo |
| Gunakan Python Flask + SQLAlchemy dan PostgreSQL Alpine | Flask mudah diuji dan kecil; PostgreSQL memberi database service nyata serta image Alpine yang relatif ringan |
| Tepat dua service inti: `app` dan `db` | Memenuhi rubrik multi-container dengan beban minimum; service bonus ditunda sampai core stabil |
| Gunakan Docker Compose sebagai orkestrator | UAS tidak mewajibkan Kubernetes dan Compose sudah mencakup orkestrasi deklaratif yang dinilai |
| Test endpoint menggunakan SQLite in-memory, lalu smoke test Compose dengan PostgreSQL | Unit/endpoint test cepat sebagai quality gate sebelum build; smoke test membuktikan integrasi container database nyata |
| Simulasi gangguan dengan menghentikan `db`, mengamati `/health` menjadi 503, lalu memulihkan `db` | Sederhana, aman, mudah dijelaskan, dan membuktikan dampak serta recovery service |
| Bukti pipeline gagal dibuat dengan pendekatan TDD | Tambahkan test validasi sebelum implementasinya agar kegagalan relevan dan terkontrol, lalu commit perbaikan tanpa menghapus riwayat run |

## Issues Encountered
| Issue | Resolution |
|-------|------------|
| LibreOffice/`soffice` tidak tersedia untuk renderer DOCX bawaan | Gunakan ekstraksi struktural lengkap dan cek renderer alternatif Microsoft Word |

## Resources
- `C:\laragon\www\uas_pak_dhendra\Dhendra_Marutho_UAS_Cloud_Computing.docx`
- Deskripsi UAS pada percakapan pengguna.
- Microsoft WSL install: https://learn.microsoft.com/en-us/windows/wsl/install
- Docker Desktop Windows install: https://docs.docker.com/desktop/setup/install/windows-install/
- Docker Desktop WSL 2: https://docs.docker.com/desktop/features/wsl/
- Docker Compose startup order: https://docs.docker.com/compose/how-tos/startup-order/
- GitHub Actions workflows: https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows
- GitHub Actions continuous integration: https://docs.github.com/en/actions/get-started/continuous-integration

## Visual/Browser Findings
- Page 1: identitas ujian, CPMK, ketentuan A-B, dan komponen wajib 1-5 terbaca utuh.
- Page 2: komponen testing/CI-CD, analisis, nilai tambahan, luaran, struktur laporan, video, serta bukti wajib 1-7 terbaca utuh.
- Page 3: bukti wajib 8-10, tabel rubrik 100%, format pengumpulan, dan catatan penting terbaca utuh.
- Tidak ada clipping/overlap yang mengaburkan isi; nomor halaman sesuai 1-3.
