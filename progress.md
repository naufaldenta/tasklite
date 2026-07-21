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

### Phase 7: Implementasi Aplikasi TaskLite
- **Status:** in_progress
- Actions taken:
  - Memastikan repository bersih dan baru berisi dokumen planning.
  - Memastikan tidak ada instruksi tambahan `AGENTS.md` di workspace.
  - Memeriksa environment: Docker belum tersedia dan Python 3.12.13 tersedia.
  - Memverifikasi versi dependency utama melalui PyPI resmi.
  - Membuat skeleton Flask dan memulai virtual environment untuk smoke test.
  - Mengunci dependency, memverifikasi seluruh paket terpasang, dan menjalankan smoke test route dasar dengan hasil lulus.
  - Merapikan blank line ekstra yang ditemukan pemeriksaan whitespace Git.
  - Menambahkan konfigurasi database berbasis environment, fallback SQLite lokal, dan model `Task`.
  - Memverifikasi pembuatan tabel serta insert/read record pada SQLite in-memory.
  - Mengimplementasikan operasi Read dengan blueprint, template daftar, empty state, dan CSS responsif lokal.
  - Memverifikasi empty state dan data task tampil pada HTML.
  - Mengimplementasikan operasi Create dengan form server-rendered, penyimpanan database, redirect, dan notice sukses.
  - Memverifikasi task baru tersimpan dengan status default `pending` dan tampil pada halaman.
  - Mengimplementasikan operasi Update dengan halaman edit, perubahan detail/status, dan tombol edit responsif.
  - Memverifikasi record yang sama berubah dari `pending` menjadi `done`.
  - Mengimplementasikan operasi Delete dengan route POST, konfirmasi browser, dan notice sukses.
  - Memverifikasi record terhapus dan halaman kembali ke empty state.
  - Menambahkan lima automated test untuk empty state, Create, halaman edit, Update, dan Delete.
  - Membuat Dockerfile dengan Python slim, instalasi dependency, source code, port, user non-root, dan Gunicorn.
  - Menambahkan `.dockerignore` untuk menjaga secret, cache, dokumen, dan artefak lokal di luar build context.
  - Menjalankan audit tujuh elemen Dockerfile dan regression test aplikasi.
  - Membuat Compose dua service dengan network, `depends_on`, restart policy, health check database, dan named volume.
  - Menambahkan `.env.example` untuk repository serta `.env` lokal yang sudah dikonfirmasi diabaikan Git.
  - Menjalankan audit delapan elemen Compose dan regression test aplikasi.
  - Menambahkan endpoint `/health` dengan query `SELECT 1` serta respons JSON 200/503.
  - Menambahkan Dockerfile `HEALTHCHECK` dan automated test status database.
  - Membuat workflow GitHub Actions: checkout, setup Python, install dependency, pytest, Compose config, Docker build, multi-container smoke test, log gagal, dan cleanup.
  - Memakai `actions/checkout@v6`, `actions/setup-python@v6`, serta permission `contents: read` berdasarkan release resmi.
  - Memvalidasi sintaks YAML workflow dan Compose lalu menjalankan regression test.
- Files created/modified:
  - `app/__init__.py` dan `app/models.py` (created/updated)
  - `.gitignore`, `task_plan.md`, dan `progress.md` (updated)

## Test Results
| Test | Input | Expected | Actual | Status |
|------|-------|----------|--------|--------|
| Planning files exist | 3 file paths | Semua file tersedia | Semua file dibuat | Pass |
| DOCX page review | 3 halaman | Semua ketentuan terbaca | 3 halaman utuh dan terbaca | Pass |
| Planning requirement audit | 10 kelompok persyaratan | Semua tersedia dalam rencana | 10/10 lulus | Pass |
| Git workflow revision audit | 9 aturan | Commit/push, CRUD terpisah, prefix, keamanan, dan CI tercakup | 9/9 lulus | Pass |
| Flask skeleton smoke test | `GET /` | HTTP 200 dan teks `TaskLite siap` | Sesuai harapan | Pass |
| Database smoke test | SQLite in-memory + model `Task` | Tabel terbentuk dan record dapat disimpan/dibaca | Sesuai harapan | Pass |
| Read feature smoke test | Database kosong dan satu task | Empty state lalu task tampil pada HTML | Sesuai harapan | Pass |
| Create feature smoke test | POST judul dan deskripsi valid | Record tersimpan, redirect sukses, dan task tampil | Sesuai harapan | Pass |
| Update feature smoke test | Edit judul, catatan, dan status | Record lama diperbarui menjadi nilai baru | Sesuai harapan | Pass |
| Delete feature smoke test | Hapus satu record | Record hilang dan empty state tampil | Sesuai harapan | Pass |
| Automated CRUD tests | `pytest -q` | Minimal lima test lulus | 5 passed in 0.88s | Pass |
| Dockerfile structural audit | 7 elemen wajib | Semua elemen tersedia | 7/7 lulus | Pass |
| Regression after Dockerfile | `pytest -q` | Semua test tetap lulus | 5 passed in 0.67s | Pass |
| Compose structural audit | 8 elemen wajib | Dua service, port, network, dependency, restart, volume, dan health tersedia | 8/8 lulus | Pass |
| Environment secret check | `git check-ignore .env` | `.env` diabaikan Git | Aturan `.gitignore` terdeteksi | Pass |
| Regression after Compose | `pytest -q` | Semua test tetap lulus | 5 passed in 0.61s | Pass |
| Health endpoint tests | `pytest -q` | CRUD dan health lulus | 6 passed in 0.74s | Pass |
| Dual healthcheck audit | Dockerfile + Compose | App dan database punya mekanisme health check | Keduanya terdeteksi | Pass |
| CI and Compose YAML audit | PyYAML | Kedua file valid YAML dan struktur utama tersedia | Sesuai harapan | Pass |
| Regression before CI push | `pytest -q` | Semua test lulus | 6 passed in 0.91s | Pass |

## Error Log
| Timestamp | Error | Attempt | Resolution |
|-----------|-------|---------|------------|
| 2026-07-21 | `git status` gagal: bukan repository Git | 1 | Dicatat sebagai kondisi awal dan akan dimasukkan ke tutorial setup |
| 2026-07-21 | Render DOCX gagal: `FileNotFoundError` untuk LibreOffice/soffice | 1 | Tidak mengulang; beralih ke ekstraksi struktural dan pemeriksaan Word lokal |
| 2026-07-21 | Ekstraksi DOCX terkena `UnicodeEncodeError` pada simbol panah | 1 | Jalankan ulang dengan encoding output UTF-8 |
| 2026-07-21 | Wrapper `pdftoppm` gagal menemukan path binary | 1 | PDF sudah berhasil dibuat melalui Microsoft Word; rasterisasi dialihkan ke runtime Python |
| 2026-07-21 | Audit dua service memberi false negative akibat kapitalisasi heading | 1 | Perbaiki kondisi audit dan jalankan ulang |
| 2026-07-21 | Penghapusan folder QA ditolak kebijakan tool pada dua pendekatan | 2 | Hentikan penghapusan dan lindungi repository dengan aturan `_docx_review/` pada `.gitignore` |
| 2026-07-21 | Pemeriksaan gabungan exit 1 karena tidak ada `AGENTS.md` | 1 | Kondisi normal; pemeriksaan Docker/runtime dijalankan terpisah |
| 2026-07-21 | `docker` tidak ditemukan | 1 | Lanjutkan unit test dengan virtual environment dan tunda uji Compose runtime sampai Docker terpasang |
| 2026-07-21 | Instalasi dependency `.venv` timeout setelah 120 detik | 1 | Paket sudah lengkap; smoke test dipisahkan dan lulus |
| 2026-07-21 | Patch log gagal karena konteks Phase 7 tidak cocok | 1 | Membaca konteks aktual lalu menerapkan patch terarah |
| 2026-07-21 | Empat file awal memiliki blank line ekstra di EOF | 1 | Menghapus baris ekstra dan menjalankan ulang `git diff --check` |
| 2026-07-21 | Patch workflow CI memiliki hunk tidak valid | 1 | Tidak ada file berubah; patch diulang dengan dua hunk yang benar |

## 5-Question Reboot Check
| Question | Answer |
|----------|--------|
| Where am I? | Planning dan revisi Git workflow selesai |
| Where am I going? | Implementasi proyek dengan commit/push setelah setiap perubahan besar |
| What's the goal? | Rencana lengkap proyek CRUD multi-container UAS yang ringan untuk Windows 11 |
| What have I learned? | Lihat findings.md |
| What have I done? | Menelaah UAS, membuat rencana, dan menetapkan workflow Git granular yang telah diaudit |
