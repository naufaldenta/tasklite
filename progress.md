# Progress Log

## Session: 2026-07-21

### Phase 1: Requirements & Discovery
- **Status:** complete
- **Started:** 2026-07-21
- Actions taken:
  - Membaca aturan skill documents dan planning-with-files.
  - Membuat berkas perencanaan persisten sebelum menganalisis dokumen.
  - Memeriksa isi awal workspace; hanya terdapat dokumen sumber dan berkas planning.
  - Mengekstrak seluruh teks, tabel, dan metadata paket DOCX.
  - Mengekspor DOCX ke PDF dengan Microsoft Word dan merender 3 halaman via pypdfium2.
  - Memeriksa ketiga halaman secara visual dan mencatat seluruh persyaratan/rubrik.
  - Memverifikasi setup WSL 2, Docker Desktop, Compose health dependency, dan GitHub Actions dari dokumentasi resmi.
- Files created/modified:
  - `task_plan.md` (created)
  - `findings.md` (created)
  - `progress.md` (created)

### Phase 2: Architecture & Scope Design
- **Status:** complete
- Actions taken:
  - Memilih Flask server-rendered + PostgreSQL sebagai stack minimal.
  - Memilih dua service inti dan Docker Compose sebagai orkestrator.
  - Merancang endpoint CRUD, skema satu tabel, network, volume, environment, health check, restart policy, dan test.
  - Memetakan implementasi dan bukti terhadap rubrik UAS.
- Files created/modified:
  - `RENCANA_PROYEK_UAS.md` (created)
- Files created/modified:
  - Tidak ada.

### Phase 3: Local Environment Tutorial
- **Status:** complete
- Actions taken:
  - Menulis langkah WSL 2, Docker Desktop, Git, verifikasi, perintah harian, dan troubleshooting Windows 11.
  - Menjelaskan bahwa Python/PostgreSQL host dan Kubernetes tidak perlu dipasang.
- Files created/modified:
  - `RENCANA_PROYEK_UAS.md` (updated)

### Phase 4: Implementation Roadmap
- **Status:** complete
- Actions taken:
  - Menetapkan struktur direktori, fase implementasi, strategi commit, rencana workflow, dan skenario bukti.
  - Menyusun rencana laporan, delapan slide, dan video demonstrasi.
- Files created/modified:
  - `RENCANA_PROYEK_UAS.md` (updated)

### Phase 5: Planning Deliverable & Review
- **Status:** complete
- Actions taken:
  - Menjalankan audit otomatis untuk sepuluh kelompok persyaratan; seluruhnya lulus.
  - Menambahkan `.gitignore` agar credential dan artefak review tidak ikut repository.
- Files created/modified:
  - `RENCANA_PROYEK_UAS.md` (reviewed)
  - `.gitignore` (created)
  - `task_plan.md`, `findings.md`, dan `progress.md` (updated)

### Phase 6: Git Workflow Revision
- **Status:** complete
- Actions taken:
  - Memastikan repository sudah terhubung ke `origin` dan branch aktif adalah `main`.
  - Meninjau strategi commit lama yang masih berbahasa Inggris dan menggabungkan beberapa operasi CRUD.
  - Mengganti strategi menjadi satu perubahan fungsional per commit dan langsung push.
  - Memisahkan checkpoint Create, Read, Update, Delete, serta test masing-masing.
  - Menambahkan tabel prefix dan contoh pesan singkat berbahasa Indonesia nonformal.
  - Menjaga satu commit gagal terkontrol khusus bukti CI dan melarang push rusak pada tahap lain.
  - Menjalankan audit sembilan aturan Git; seluruhnya lulus.
- Files created/modified:
  - `RENCANA_PROYEK_UAS.md` (updated)
  - `task_plan.md`, `findings.md`, dan `progress.md` (updated)

## Test Results
| Test | Input | Expected | Actual | Status |
|------|-------|----------|--------|--------|
| Planning files exist | 3 file paths | Semua file tersedia | Semua file dibuat | Pass |
| DOCX page review | 3 halaman | Semua ketentuan terbaca | 3 halaman utuh dan terbaca | Pass |
| Planning requirement audit | 10 kelompok persyaratan | Semua tersedia dalam rencana | 10/10 lulus | Pass |
| Git workflow revision audit | 9 aturan | Commit/push, CRUD terpisah, prefix, keamanan, dan CI tercakup | 9/9 lulus | Pass |

## Error Log
| Timestamp | Error | Attempt | Resolution |
|-----------|-------|---------|------------|
| 2026-07-21 | `git status` gagal: bukan repository Git | 1 | Dicatat sebagai kondisi awal dan akan dimasukkan ke tutorial setup |
| 2026-07-21 | Render DOCX gagal: `FileNotFoundError` untuk LibreOffice/soffice | 1 | Tidak mengulang; beralih ke ekstraksi struktural dan pemeriksaan Word lokal |
| 2026-07-21 | Ekstraksi DOCX terkena `UnicodeEncodeError` pada simbol panah | 1 | Jalankan ulang dengan encoding output UTF-8 |
| 2026-07-21 | Wrapper `pdftoppm` gagal menemukan path binary | 1 | PDF sudah berhasil dibuat melalui Microsoft Word; rasterisasi dialihkan ke runtime Python |
| 2026-07-21 | Audit dua service memberi false negative akibat kapitalisasi heading | 1 | Perbaiki kondisi audit dan jalankan ulang |
| 2026-07-21 | Penghapusan folder QA ditolak kebijakan tool pada dua pendekatan | 2 | Hentikan penghapusan dan lindungi repository dengan aturan `_docx_review/` pada `.gitignore` |

## 5-Question Reboot Check
| Question | Answer |
|----------|--------|
| Where am I? | Planning dan revisi Git workflow selesai |
| Where am I going? | Implementasi proyek dengan commit/push setelah setiap perubahan besar |
| What's the goal? | Rencana lengkap proyek CRUD multi-container UAS yang ringan untuk Windows 11 |
| What have I learned? | Lihat findings.md |
| What have I done? | Menelaah UAS, membuat rencana, dan menetapkan workflow Git granular yang telah diaudit |
