tautan aplikasi: https://muhammad-rizky413-footballshop.pbp.cs.ui.ac.id

## TUGAS 6
- Apa perbedaan antara synchronous request dan asynchronous request?
    Synchronous Request

    Asynchronous Request


- Bagaimana AJAX bekerja di Django (alur request–response)?
    1. User melakukan aksi di halaman web
        Event JavaScript menangkap aksi seperti klik tombol “Kirim”, ubah pilihan dropdown, atau ketik di input.
    2. JavaScript mengirim request AJAX ke server Django
        Data dikirim ke URL tertentu yang sudah diatur di urls.py. Request ini bisa berupa GET (mengambil data) ataupun POST(mengirim data).
    3. Django menerima request
        Request masuk ke view yang sesuai di views.py kemudian data diproses seperti biasa. Biasanya view tidak merender template HTML penuh, tapi hanya mengirim JSONResponse atau data kecil.
    4. Server mengirim response balik ke browser
        Django mengembalikan data dalam format JSON (bukan HTML penuh).
    5. JavaScript menerima dan menampilkan hasil
        JavaScript membaca response dan memperbarui bagian tertentu di halaman.

- Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
    1. AJAX hanya memperbarui bagian tertentu dari halaman sehingga tidak perlu reload seluruh halaman.
    2. Mengurangi beban server dan bandwidth karena hanya mengirim data kecil.
    3. Pengalaman pengguna (UX) lebih baik karena pengguna tidak melihat “refresh” halaman.
    4. Bisa memperbarui konten secara real-time berdasarkan respons server tanpa reload sehingga interaksi dinamis.
    5. Server cukup mengirim JSON sehingga bisa diolah dengan bebas di JavaScript.
    6. Lebih cocok untuk aplikasi interaktif seperti dashboard admin, SPA (Single Page Application), atau fitur drag-drop.

- Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
    1. Gunakan HTTPS (SSL/TLS)
    2. Gunakan CSRF Token di AJAX
    3. Validasi input di sisi server
    4. Jangan kirim data sensitif ke frontend
    5. Gunakan Django Authentication System
    6. Batasi percobaan login (Brute Force Protection)
    7. Gunakan session Django, bukan manual token
    8. Sanitasi & escape data sebelum ditampilkan
    9. Gunakan HttpOnly & Secure untuk cookie

- Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
    1. Halaman terasa lebih cepat & responsif
    2. Interaksi lebih halus dan tidak terputus
    3. Mempercepat navigasi dan alur kerja
    4. Fokus pengguna tidak teralihkan
    5. Transisi data terasa real-time
    6. UX lebih interaktif dan modern

## TUGAS 5
- Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
    Urutan prioritas pengambilan CSS selector:
    1. Inline styles
        Aturan CSS yang langsung ditulis di atribut style pada elemen HTML, dianggap paling spesifik karena developer secara eksplisit nempelkan aturan ke elemen tersebut.
    2. ID selectors
        Selector yang menggunakan tanda # untuk menunjuk elemen berdasarkan id yang bersifat unik di halaman.
    3. Classes selector
        Selector dengan tanda titik (.) untuk menargetkan elemen berdasarkan class. Class bisa dipakai berulang kali di banyak elemen, sehingga spesifik tapi tidak seunik ID.
    4. Element selector
        Selector yang langsung menargetkan elemen berdasarkan nama tag HTML (seperti p, h1, div) atau pseudo-element (::before, ::after). Prioritasnya rendah karena sifatnya terlalu umum (bisa berlaku untuk banyak elemen sekaligus).

- Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
    Responsive design adalah pendekatan desain web yang membuat tampilan website otomatis menyesuaikan ukuran layar perangkat yang digunakan (desktop, tablet, smartphone). Konsep ini penting karena:
    1. Pengguna mengakses web dari berbagai device baik mobile maupun desktop.
    2. UX yang fleksibel membuat website mudah digunakan tanpa perlu zoom in/out atau scroll horizontal.
    3. Satu website bisa menyesuaikan di semua perangkat tanpa membuat versi yang terpisah.

    Contoh aplikasi yang sudah menerapkan:
    1. Instagram (web)
        Layoutnya menyesuaikan layar, dimana di desktop muncul feed + sidebar dan di mobile hanya feed penuh tanpa sidebar.
    2. Tokopedia
        Tampilan produk, tombol, dan navigasi otomatis menyesuaikan ukuran layar sehingga nyaman digunakan di HP.
    Kedua aplikasi ini sangat mengutamakan kenyamanan pengguna lintas perangkat, terutama karena mayoritas user mengakses melalui smartphone.

    Contoh aplikasi yang belum menerapkan:
    1. Website sekolah/universitas lama dengan layout fixed (misalnya academic.cs.ui.ac.id)
        Jika dibuka di desktop ataupun device lain yang tidak sesuai dengan tampilannya, ada beberapa kendala teks terlalu kecil, tombol susah diklik, dan pengguna harus zoom in/out manual.
    Website lama ini biasanya masih menggunakan desain statis tanpa media queries, sehingga tampilannya tidak fleksibel mengikuti ukuran layar.

- Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
    1. Margin
        Merupakan ruang kosong di luar elemen yang digunakan untuk memberi jarak antar elemen. Margin berfungsi mengatur jarak antar elemen agar tidak saling menempel. Contoh implementasi:
        div {
            margin: 20px; // memberi jarak 20px di semua sisi elemen
        }
    
    2. Border
        Merupakan garis tepi yang mengelilingi elemen dan berada di antara margin dan padding. Border berfungsi untuk menandai batas elemen secara visual, bisa berupa garis solid, putus-putus, berwarna, dll. Contoh Implementasi:
        div {
            border: 4px solid white; // border tebal 4px, solid, warna putih
        }
    
    3. Padding
        Merupakan ruang kosong di dalam elemen yang terletak antara konten dan border. Padding berfungsi memberi jarak antara isi (teks/gambar) dengan tepi border. Contoh implementasi:
        div {
        padding: 15px; // memberi ruang 15px antara teks dan border
        }


- Jelaskan konsep flex box dan grid layout beserta kegunaannya!
    1. Flexbox (Flexible Box Layout)
        Merupakan model layout 1 dimensi yang digunakan untuk menyusun elemen secara fleksibel dalam satu arah, baik horizontal (row) maupun vertikal (column). Flexbox berfungsi untuk:
        - Membuat elemen sejajar secara otomatis tanpa harus hitung manual dengan float atau position.
        - Memudahkan pengaturan alignment (rata kiri, kanan, tengah, atau rata di antara).
        - Cocok untuk layout yang lebih fokus ke satu baris atau satu kolom.

    2. Grid Layout
        Merupakan model layout 2 dimensi yang memungkinkan penempatan elemen dalam baris (rows) dan kolom (columns) secara bersamaan. Grid Layout berfungsi untuk:
        - Membuat struktur layout kompleks seperti tabel, dashboard, atau halaman penuh.
        - Fleksibel untuk mengatur ukuran, posisi, dan jarak antar elemen di grid.
        - Cocok untuk layout yang lebih fokus ke dua dimensi (rows + columns).

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
    1.  Implementasikan fungsi untuk menghapus dan mengedit product.
        Menghapus product
        - Membuat fungsi baru dengan nama delete_product yang menerima parameter request dan id pada views.py di folder main untuk menghapus data product.
        - Mengimport fungsi tadi ke urls.py yang ada pada folder main.
        - Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor.
        - Memperbarui potongan kode di loop product_list agar terdapat tombol hapus untuk setiap produk yang ada pada main.html di folder main/templates.
        
        Mengedit product
        - Membuat fungsi baru bernama edit_product yang menerima parameter request dan id di views.py yang ada pada subdirektori main.
        - Membuat berkas HTML baru dengan nama edit_product.html pada subdirektori main/templates.
        - Mengimport fungsi tadi ke urls.py yang ada pada folder main.
        - Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor.
        - Memperbarui potongan kode di loop product_list agar terdapat tombol edit untuk setiap produk yang ada pada main.html di folder main/templates.

    2.  Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
        a. Kustomisasi halaman login, register, tambah product, edit product, dan detail product semenarik mungkin.
            Halaman login
            - Menggunakan base template dan title khusus halaman login.
            - Menambahkan background abu-abu muda dengan card putih di tengah layar.
            - Memberikan header menarik dengan judul besar dan subteks sambutan.
            - Menampilkan error form dan error field dengan styling berbeda agar lebih jelas.
            - Menggunakan input modern dengan efek fokus berwarna biru.
            - Tombol login dibuat full width, warna biru dengan efek hover.
            - Menampilkan pesan sukses/error/info dengan badge berwarna.
            - Menyediakan link ke halaman register dengan tampilan call-to-action di bawah form.

            Halaman register
            - Menggunakan base template dengan title khusus halaman register.
            - Latar belakang abu-abu muda, card putih dengan shadow di tengah layar.
            - Header menarik dengan judul Join Us dan subteks ajakan membuat akun.
            - Validasi form ditampilkan rapi dengan box error berwarna merah.
            - Input field diberi label jelas, padding besar, dan efek fokus biru.
            - Tombol submit full width berwarna biru dengan efek hover + ring.
            - Pesan sukses/error/info ditampilkan dalam box warna berbeda sesuai status.
            - Link ajakan ke halaman login disediakan di bawah form agar mudah diakses.

            Tambah product
            - Menggunakan base template dengan title khusus Create Product.
            - Latar belakang abu-abu muda, form card putih dengan border dan padding besar di tengah halaman.
            - Menyediakan navigasi Back to Product(s) agar pengguna bisa kembali dengan mudah.
            - Header form dengan judul besar dan deskripsi singkat tujuan form.
            - Setiap field form diberi label jelas, area input yang lebar, dan pesan error merah di bawahnya.
            - Tersedia teks bantuan (help_text) untuk field yang membutuhkannya.
            - Bagian aksi di bawah form memiliki dua tombol: Cancel (abu-abu) dan Publish Product (biru).
            - Layout tombol responsif: pada layar kecil ditampilkan vertikal, pada layar besar ditampilkan horizontal.

            Edit product
            - Menggunakan base template dengan title khusus Edit Product.
            - Latar belakang abu-abu muda, form card putih dengan border dan padding besar.
            - Menyediakan navigasi Back to Product(s) di atas halaman.
            - Header form dengan judul Edit Product dan deskripsi singkat.
            - Setiap field form diberi label jelas, area input yang lebar, pesan error merah, dan teks bantuan jika ada.
            - Bagian aksi di bawah form punya dua tombol: Cancel (abu-abu) untuk kembali, dan Update Product (biru) untuk menyimpan perubahan.
            - Layout tombol responsif: pada layar kecil vertikal, pada layar besar horizontal.

            Detail product
            - Menggunakan base template dengan title dinamis sesuai nama produk.
            - Latar belakang abu-abu muda, konten di tengah dengan lebar maksimal besar.
            - Navigasi balik ke daftar produk dengan teks Back to Product(s).
            - Card artikel putih dengan border dan rounded corners sebagai container detail produk.
            - Header menampilkan kategori produk sebagai badge berwarna biru, serta badge tambahan untuk Featured bila aktif.
            - Judul produk ditampilkan besar (text-3xl hingga text-4xl), bold, dengan spacing rapi.
            - Informasi tambahan berupa tanggal pembuatan dan jumlah views dalam format rapi.
            - Thumbnail produk (jika ada) ditampilkan besar dengan tinggi responsif (64–96) dan rounded.
            - Deskripsi produk ditampilkan dengan gaya prose rapi, teks abu-abu, dan mendukung line break.
            - Bagian bawah menampilkan informasi author, berupa username pemilik produk atau Anonymous jika tidak ada user, dengan teks pendukung yang lebih kecil.

        b. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
            1. Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
            2. Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
            - Membuat struktur card product baru yang menggunakan container dengan kelas Tailwind seperti bg-blue-50 border border-blue-200 rounded-lg shadow-sm untuk memberi nuansa warna biru.
            - Menambahkan bagian thumbnail produk (jika ada), ditampilkan di bagian atas card dengan style object-cover rounded-t-lg agar gambar proporsional dan rapi.
            - Menampilkan nama produk dengan font tebal (font-semibold text-gray-900) serta deskripsi singkat dalam teks yang lebih ringan (text-gray-600).
            - Memberikan section aksi (action buttons) seperti Edit dan Delete di bagian bawah card untuk mempermudah pengelolaan produk bagi user yang memposting produk.
            - Mengatur card dalam layout grid responsive (misalnya grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6) supaya tampilan menyesuaikan ukuran device.

        c. Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
            - Menambahkan tombol Edit di card product dengan styling bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors, menggunakan URL {% url 'main:edit_product' product.id %} dan diletakkan di bagian bawah card dalam container flex justify-between.
            - Tambahkan tombol Delete di card product dengan styling bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700 transition-colors, menggunakan URL {% url 'main:delete_product' product.id %} dan diposisikan sejajar dengan tombol Edit menggunakan flex justify-between.

        d. Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
            - Membuat struktur utama navbar menggunakan elemen <nav> dengan kelas fixed top-0 left-0 w-full bg-white border-b border-gray-200 shadow-sm z-50, sehingga navbar selalu berada di atas layar dan terlihat jelas pada semua halaman.
            - Menambahkan wrapper max-w-7xl mx-auto flex justify-between items-center h-16 untuk mengatur tata letak logo, menu, dan user section agar sejajar secara horizontal.
            - Mengatur navigasi desktop dengan <div class="hidden md:flex">, sehingga link seperti Home dan Create Product hanya tampil pada layar medium ke atas.
            - Membuat section user desktop (login/register atau info user + logout) juga menggunakan <div class="hidden md:flex">, sehingga tampil rapi di layar besar.
            - Menambahkan hamburger button dengan <div class="md:hidden">, sehingga pada layar kecil (mobile) menu utama diganti tombol toggle.
            - Membuat mobile menu dropdown dalam <div class="mobile-menu hidden md:hidden">, yang berisi link navigasi dan user section versi mobile, ditampilkan secara vertikal.
            - Menggunakan JavaScript sederhana dengan event listener menu.classList.toggle("hidden") untuk menampilkan/menyembunyikan mobile menu ketika tombol hamburger ditekan.
            - Memastikan seluruh link navigasi diberi efek interaktif dengan kelas Tailwind seperti hover:text-gray-900 atau hover:bg-blue-700 agar lebih menarik dan user friendly di semua ukuran device.

## TUGAS 4
-  Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
    AuthenticationForm adalah form bawaan Django yang digunakan untuk menangani proses login user. Form ini menyediakan field username dan password lalu melakukan validasi apakah kombinasi keduanya sesuai dengan data user yang tersimpan di database. Jika valid, maka user dianggap berhasil login, dan jika tidak valid, form otomatis menampilkan pesan error yang sesuai. Dengan begitu, AuthenticationForm mempermudah proses autentikasi tanpa perlu membuat form login dari nol.
    Kelebihan:
    1. Tidak perlu bikin form login manual karena ini bawaan django.
    2. Terintegrasi dengan sistem auth Django sehingga otomatis bekerja dengan model User & backend.
    3. Validasi otomatis, yaitu memeriksa apakah username & password benar.
    4. Pesan error siap pakai, misalnya "Please enter a correct username and password".
    5. Sudah dapat menangani hashing password dan proteksi secara umum.
    Kekurangan:
    1. Tampilan sederhana sehingga perlu di-style ulang dengan CSS/Bootstrap agar lebih menarik.
    2. Tidak ada fitur penting lainnya seperti CAPTCHA atau 2FA sehingga harus dibuat manual.
    3. Kurang fleksibel untuk custom workflow jika aplikasi butuh autentikasi berbeda (misalnya API token, OAuth, dsb).
    4. Hanya mendukung login dengan username sehingga harus di customize untuk penggunaaan parameter lain seperti email atau nomor telepon.

- Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
    Autentikasi 
    Merupakan proses untuk memverifikasi identitas user. Django mengimplementasikan autentikasi ini melalui model User, sistem session, serta backend autentikasi yang memvalidasi kredensial. Misalnya saat login dengan AuthenticationForm, Django akan memeriksa apakah data yang dimasukkan sesuai dengan akun yang ada di database, lalu jika berhasil status login user akan disimpan di session.

    Otorisasi 
    Merupakan proses untuk menentukan hak akses user setelah identitasnya terverifikasi. Django mengatur otorisasi dengan sistem permission, group, serta atribut khusus seperti is_staff dan is_superuser. Dengan mekanisme ini, kita bisa membatasi user biasa hanya untuk membaca data, sementara admin diberi izin untuk menambah atau menghapus. Dalam tugas ini, otorisasi diwujudkan dengan penggunaan decorator @login_required.

- Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
    Session
    Kelebihan:
    1. Lebih aman karena data sensitif disimpan di server, bukan di browser user.
    2. Mendukung data kompleks seperti object di Python, bukan hanya string.
    3. Integrasi dengan autentikasi karena Django sudah langsung pakai session untuk login user.
    Kekurangan:
    1. Membebani server karena semua state user disimpan di server, jadi butuh resource ekstra.
    2. Tetap memerlukan identifier (session ID) yang dikirim lewat cookie.
    3. Jika ada banyak server, session harus disinkronkan lewat database atau cache sehingga scalingnya lebih sulit.

    Cookies
    Kelebihan:
    1. Data langsung disimpan di browser user sehingga tidak terlalu membebani server.
    2. Persisten karena bisa bertahan walaupun browser ditutup (diatur secara manual).
    3. Mudah diakses baik oleh server maupun JavaScript di client.
    Kekurangan:
    1. Kurang aman karena data ada di sisi client sehingga rawan manipulasi atau pencurian.
    2. Ukurannya terbatas yaitu maksimal sekitar 4KB per cookie.
    3. User bisa mematikan atau menghapus cookies yang ada di aplikasinya.

- Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
    Cookies secara default tidak sepenuhnya aman dalam pengembangan web, karena mereka disimpan di sisi client dan bisa diakses atau dimodifikasi oleh user maupun script berbahaya. Risiko yang sering muncul misalnya pencurian cookie melalui serangan Cross-Site Scripting (XSS), atau penyalahgunaan cookie autentikasi melalui serangan Cross-Site Request Forgery (CSRF). Selain itu, cookie juga bisa dicuri saat transmisi data jika tidak dienkripsi dengan HTTPS.
    Django menghandle beberapa kasus yang rawan terjadi dengan beberapa pendekatan, seperti SESSION_COOKIE_HTTPONLY yang membuat cookie tidak bisa diakses oleh JavaScript sehingga lebih aman dari XSS, SESSION_COOKIE_SECURE yang memastikan cookie hanya dikirim lewat HTTPS agar tidak bocor di koneksi tidak terenkripsi, serta CSRF_COOKIE_HTTPONLY dan CSRF_COOKIE_SECURE yang berfungsi sama, tetapi khusus untuk cookie CSRF. 

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1.  Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna mengakses aplikasi sebelumnya sesuai dengan status login/logoutnya.
    Registrasi
    - Menambahkan import UserCreationForm dan messages pada views.py yang ada pada subdirektori main. UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web.
    - Menambahkan fungsi register ke views.py yang berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form. Ada beberapa hal yang dimuat di fungsi seperti:
        a. form = UserCreationForm(request.POST) untuk membuat UserCreationForm baru dari yang sudah di-impor sebelumnya dengan memasukkan QueryDict berdasarkan input dari user pada request.POST.
        b. form.is_valid() untuk memvalidasi isi input dari form tersebut.
        c. form.save() untuk membuat dan menyimpan data dari form tersebut.
        d. messages.success(request, 'Your account has been successfully created!') untuk menampilkan pesan kepada pengguna setelah melakukan suatu aksi.
        e. return redirect('main:show_main') untuk melakukan redirect setelah data form berhasil disimpan.
    - Membuat berkas HTML baru dengan nama register.html pada direktori main/templates yang berfungsi menampilkan menu register.
    - Mengimpor fungsi register yang sudah dibuat tadi ke urls.py yang ada pada subdirektori main.
    - Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

    Login
    - Mengimport authenticate, login, dan AuthenticationForm pada bagian paling atas views.py yang ada pada subdirektori main.
    - Menambahkan fungsi login_user ke dalam views.py yang berfungsi untuk mengautentikasi pengguna yang ingin login. Ada beberapa hal yang dimuat di fungsi seperti:
        a. if request.method == 'POST' digunakan untuk memeriksa apakah pengguna mengirimkan permintaan login melalui halaman login. Jika ya, form harus divalidasi terlebih dahulu sebelum melakukan login ke sistem Django.
        b. login(request, user) digunakan untuk melakukan proses login. Jika pengguna valid, fungsi ini akan membuat session untuk pengguna yang berhasil login.
        c. Blok else: dijalankan ketika pengguna baru mengakses halaman login. Django akan membuat objek AuthenticationForm berdasarkan request pengguna, lalu merendernya di halaman melalui context.
    - Membuat berkas HTML baru dengan nama login.html pada direktori main/templates yang berfungsi menampikan menu login.
    - Mengimpor fungsi login yang sudah dibuat tadi ke urls.py yang ada pada subdirektori main.
    - Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

    Logout
    - Mengimport logout pada bagian paling atas bersama dengan authenticate dan login di views.py yang ada pada subdirektori main.
    - Menambahkan fungsi logout_user ke dalam fungsi views.py yang berfungsi untuk melakukan mekanisme logout. Ada beberapa hal yang dimuat di fungsi seperti:
        a. logout(request) digunakan untuk menghapus sesi pengguna yang saat ini masuk.
        b. return redirect('main:login') mengarahkan pengguna ke halaman login dalam aplikasi Django.
    - Menambahkan potongan kode anchor untuk tombol logout setelah hyperlink tag untuk Add News di berkas main.html yang ada pada direktori main/templates.
    Potongan kode ini memuat {% url 'main:logout' %} yang digunakan untuk mengarah ke URL secara dinamis berdasarkan app_name dan name yang sudah didefinisikan di urls.py.
    app_name merupakan nama app yang didefinisikan di dalam berkas urls.py. Jika app menggunakan atribut app_name di urls.py, maka ini akan dipakai untuk merujuk pada app tersebut. Jika app_name tidak didefinisikan maka nama app yang digunakan adalah nama dari folder app yang dibuat. view_name merupakan nama dari URL yang diinginkan, didefinisikan melalui parameter name dalam path() di urls.py. Karena app disini didefinisikan dengan nama main dan kita ingin menampilkan menu logout, maka parameternya diisi dengan main:logout.
    - Mengimpor fungsi login yang sudah dibuat tadi ke urls.py yang ada pada subdirektori main.
    - Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

    2.  Membuat dua (2) akun pengguna dengan masing-masing tiga (3) dummy data menggunakan model yang telah dibuat sebelumnya untuk setiap akun di lokal.
    Setelah servernya sudah running dan semua fitur baru sudah dites, register dua akun dengan nama Budi dan Agus. Setelah itu, login untuk masing-masing akun lalu menambahkan tiga barang yang cocok dengan tema aplikasi yang dibuat yaitu Football Shop.

    3. Menghubungkan model Product dengan User.
    - Mengimport User dari django.contrib.auth.models di models.py pada subdirektori main.
    - Menambahkan blok kode user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) pada class Product yang telah dibuat sebelumnya.
    Potongan kode ini berfungsi untuk menghubungkan satu produk dengan satu user melalui sebuah relationship yaitu many-to-one relationship, dimana setiap produk dapat terasosiasi dengan seorang user. Tambahan null=True memungkinkan produk yang sudah ada sebelumnya tetap valid tanpa harus memiliki user dan on_delete=models.CASCADE berarti jika user dihapus, semua produk milik user tersebut juga akan ikut terhapus.
    - Melakukan migrasi model agar data yang baru ini termigrasi ke database.
    - Mengubah potongan kode pada fungsi create_product di views.py yang ada pada subdirektori main. Dilakukan penambahan parameter commit=False pada potongan kode yang berfungsi agar Django tidak langsung menyimpan objek hasil form ke database. Dengan begitu, kita memiliki kesempatan untuk memodifikasi objek tersebut terlebih dahulu sebelum disimpan. Pada kasus ini, kita memanfaatkan kesempatan tersebut untuk mengisi field user dengan nilai request.user, yaitu pengguna yang sedang login. Dengan cara ini, setiap objek yang dibuat akan secara otomatis terhubung dengan pengguna yang membuatnya.
    - Memodifikasi fungsi show_main untuk menampilkan halaman utama setelah user login dan dilengkapi dengan filter produk berdasarkan penjual. Filter ini diambil dari query parameter filter pada URL, dengan dua opsi: "my" untuk menampilkan hanya produk yang dijual oleh user yang sedang login, dan "all" untuk menampilkan semua produk yang ada. Selain itu, informasi user seperti name diambil langsung dari username user yang sedang login.
    - Menambahkan tombol filter My dan All pada halaman main.html.
    - Menambahkan blok kode untuk menampilkan nama seller di product_detail.html. Informasi seller merefleksikan penjual produk, bukan user yang sedang login.

    4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last_login pada halaman utama aplikasi.
    - Menambahkan import HttpResponseRedirect, reverse, dan datetime pada bagian paling atas views.py di subdirektori main.
    - Mengubah bagian kode di fungsi login_user untuk menyimpan cookie baru bernama last_login yang berisi timestamp terakhir kali pengguna melakukan login. Kita dapat memperoleh ini dengan mengganti kode yang ada pada blok if form.is_valid(). Beberapa modifikasinya meliputi:
        a. login(request, user) berfungsi untuk melakukan login menggunakan sistem autentikasi Django.
        b. response = HttpResponseRedirect(reverse("main:show_main")) akan menetapkan redirect ke halaman main setelah response diterima.
        c. response.set_cookie('last_login', str(datetime.datetime.now())) berfungsi untuk mendaftarkan cookie last_login di response dengan isi timestamp terkini.
    - Pada fungsi show_main, menambahkan potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context. Kita mengakses cookie yang terdaftar di request dengan request.COOKIES.get('last_login', 'Never'). Penbambahan method .get() digunakan untuk mengambil nilai cookie dengan aman, dimana jika cookie last_login tidak ada atau sudah dihapus maka akan mengembalikan nilai default yaitu Never. Selain itu, waktu terakhir pengguna login sekarang dapat ditampilkan di halaman web dengan mengakses key last_login.
    - Mengubah fungsi logout_user untuk menghapus cookie last_login setelah melakukan logout. Dilakukan penambahan response.delete_cookie('last_login') yang berfungsi untuk menghapus cookie last_login dari daftar cookies di response.
    - Menambahkan potongan kode <h5>Sesi terakhir login: {{ last_login }}</h5> setelah tombol logout pada main.html di direktori main/templates untuk menampilkan data waktu terakhir pengguna login. 

    5. Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
    Ini dia file README.md nya.

## TUGAS 3
-  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Dalam pengimplementasian sebuah platform, kita memerlukan data delivery untuk: 
    1. Menjembatani komunikasi antara sisi client (misalnya browser atau aplikasi mobile) dengan sisi server. Tanpa adanya data delivery, user tidak bisa mengakses atau memanfaatkan data yang disimpan di server.
    2. Data yang disimpan di database dapat dikirimkan dalam format yang lebih user-friendly (HTML, JSON, atau XML) sehingga dapat ditampilkan di antarmuka dengan baik.
    3. Data delivery memastikan setiap perubahan yang terjadi pada database segera tercermin pada tampilan aplikasi. Hal ini membuat informasi yang dilihat user selalu up-to-date dan sinkron dengan data sesungguhnya di server.
    4. Data delivery mengatur bagaimana data dikirimkan, apakah melalui full page rendering, AJAX, REST API, atau GraphQL. Cara ini memengaruhi performa aplikasi dan pengalaman pengguna, seperti kecepatan loading halaman serta penghematan bandwidth.
    5. Dalam proses pengiriman data, data delivery memungkinkan penerapan validasi, autentikasi, dan otorisasi. Hal ini memastikan hanya pengguna yang berhak yang dapat mengakses data tertentu sehingga kerahasiaan dan integritas data tetap terjaga.
    6. Data delivery memungkinkan pertukaran data lintas sistem menggunakan format standar seperti JSON atau XML, sehingga platform bisa saling berkomunikasi dengan lancar.

-  Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya pribadi, JSON lebih baik daripada XML karena penulisannya yang lebih mudah dimengerti. Namun, masing masing format itu memiliki keunggulannya masing-masing, diantaranya:
    JSON:
    1. Lebih ringkas dan mudah dibaca
    2. Ukuran data lebih kecil
    3. Parsing lebih cepat
    4. Sangat cocok untuk web API
    5. Mudah dipahami developer
    XML:
    1. Mendukung metadata dengan atribut
    2. Fleksibel dan ekspresif
    3. Ada dukungan validasi
    4. Cocok untuk sistem besar dan lama (legacy)
    5. Lebih formal dalam struktur data
    JSON lebih populer dibandingkan XML karena strukturnya lebih sederhana, ringkas, dan mudah dibaca. JSON juga langsung sesuai dengan model data di banyak bahasa pemrograman, sehingga tidak membutuhkan proses tambahan seperti data binding atau serialisasi yang rumit pada XML.
    Referensi:
    https://blog.axway.com/learning-center/apis/api-management/why-json-won-over-xml

- Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method is_valid memiliki berbagai fungsi, seperti:
    1. Memeriksa apakah data yang dikirimkan ke form sesuai dengan aturan validasi yang sudah ditentukan pada field form tersebut (panjang minimal, wajib diisi, format email, dll).
    2. Jika semua field valid, maka is_valid() akan mengembalikan nilai True. Selain itu, data yang sudah “dibersihkan” bisa diakses lewat atribut form.cleaned_data.
    3. Jika ada field yang tidak valid, maka is_valid() akan mengembalikan False dan Django otomatis menambahkan pesan error yang bisa ditampilkan di template.
    Kita membutuhkan method is_valid() untuk memastikan data yang masuk ke sistem aman dan sesuai aturan sebelum disimpan ke database, memudahkan developer dalam menangani error input pengguna, dan menjaga konsistensi dan integritas data tanpa harus menulis logika validasi manual di banyak tempat.

-  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    Token csrf_token digunakan untuk memastikan bahwa request yang dikirim memang berasal dari user yang sah (session/browser yang benar), bukan dari sumber luar yang berbahaya. Dengan begitu, csrf_token berfungsi sebagai perlindungan terhadap Cross-Site Request Forgery (CSRF) attacks. 
    Jika kita tidak menambahkan csrf_token, form masih dapat terkirim namun server tidak bisa membedakan mana request asli dari user dan mana yang “dipalsukan” oleh pihak luar. 
    Hal ini daat dimanfaatkan oleh penyerang dengan cara membuat halaman web berbahaya (misalnya dengan form atau script tersembunyi) yang ketika dikunjungi user, otomatis mengirim request ke aplikasi Django tanpa sepengetahuan user karena request ini membawa session/cookie user yang valid sehingga server bisa mengira request itu sah.

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
    Menambahkan 4 fungsi dengan nama show_xml, show_json, show_xml_by_id, show_json_by_id dengan alur:
    - Menambahkan import HttpResponse dan Serializer pada bagian paling atas views.py yang ada pada direktori main.
    - Membuat fungsi baru yang menerima parameter request dengan nama show_xml dan membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada Product.
    - Menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml". 'serializers' di fungsi ini digunakan untuk menerjemahkan objek model menjadi format lain seperti dalam fungsi ini adalah XML.
    - Mengimport fungsi yang sudah dibuat tadi di urls.py yang ada pada direktori main.
    - Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
    - Membuat sebuah fungsi baru yang menerima parameter request dengan nama show_json dengan sebuah variabel di dalamnya yang menyimpan hasil query dari seluruh data yang ada pada Product di views.py yang ada pada direktori main.
    - Menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter content_type="application/json".
    - Mengimport fungsi yang sudah dibuat tadi di urls.py yang ada pada direktori main.
    - Menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.
    - Membuat dua fungsi baru yang menerima parameter request dan product_id dengan nama show_xml_by_id dan show_json_by_id di views.py yang ada pada direktori main.
    - Membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari data dengan id tertentu yang ada pada Product.
    - Menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON).
    - Menambahkan blok try except pada fungsi untuk mengantisipasi kondisi ketika data dengan product_id tertentu tidak ditemukan dalam basis data. Jika data tidak ditemukan, kembalikan HttpResponse dengan status 404 sebagai tanda data tidak ada.
    - Mengimport fungsi yang sudah dibuat tadi di urls.py yang ada pada direktori main.
    - Menambahkan path URL ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.

2. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
    Dilakukan dengan cara mengimport fungsi-fungsi yang sudah dibuat pada poin 1 dan menambahkan path URL ke dalam variabel urlpatterns di urls.py yang ada pada direktori main.

3. Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada setiap data objek model yang akan menampilkan halaman detail objek.
    Dilakukan dengan tahap sebagai berikut:
    - Menambahkan beberapa import dan fungsi-fungsi pada bagian paling atas berkas views.py yang ada pada direktori main seperti:
    a. Fungsi show_main diperbarui dengan menambahkan Product.objects.all() untuk mengambil seluruh objek Product yang tersimpan pada database.
    b. Fungsi create_product digunakan untuk menghasilkan form yang dapat menambahkan data Product secara otomatis ketika data di-submit dari form.
    c. Fungsi show_product menggunakan get_object_or_404(Product, pk=id) untuk mengambil objek Product berdasarkan primary key (id). Jika objek tidak ditemukan, akan mengembalikan halaman 404.
    - Import fungsi-fungsi yang sudah dibuat tadi dan menambahkan path URL ke dalam variabel urlpatterns di urls.py yang ada pada direktori main.
    - Mengupdate kode di dalam blok content untuk menampilkan data product serta tombol "Add Product" yang akan redirect ke halaman form di main.html pada direktori main/templates.
    - Membuat dua berkas HTML baru pada direktori main/templates untuk halaman form input dan detail produk.

4. Membuat halaman form untuk menambahkan objek model pada app sebelumnya.
    Dilakukan dengan cara membuat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form yang dapat menerima data Product baru sekaligus menambahkan beberapa hal:
    a. model = Product untuk menunjukkan model yang akan digunakan untuk form. Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek Product.
    b. fields = ["name", "price", "description", "thumbnail", "category", "is_featured", "brand", "stock"] untuk menunjukkan field dari model Product yang digunakan untuk form.
    Selain itu,  ditambahkan fungsi create_news.html yang dalamnya ada {% csrf_token %},  token yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya, serta {{ form.as_table }}, merupakan template tag yang digunakan untuk menampilkan fields form yang sudah dibuat pada forms.py sebagai table.

5. Membuat halaman yang menampilkan detail dari setiap data objek model.
    Selain pemanfaatan fungsi show_product yang sudah dijabarkan di nomor 3 tadi, dibuat pula file news_detail.html yang berisi apa saja yang perlu ditampilkan nanti, seperti tombol kembali ke menu utama dan produk secara lebih lengkap.

6. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
    Ini dia file README.md nya.

7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
    Screenshot hasil akses URL:
    https://drive.google.com/drive/folders/1GgAkMPNKTmuJLzEyXToGOYZPi6styPFf?usp=sharing

8. Melakukan add-commit-push ke GitHub.
    Ketiga command tersebut sudah dilakukan dan Github sudah terupdate.

- Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Asdos sudah bagus dalam menyampaikan ketentuan maupun step-by-step tutorial dan sangat terbuka terhadap pertanyaan seputar tutorialnya.

## TUGAS 2
- Cara mengimplementasikan checklist secara step-by-step:
1. Membuat sebuah proyek Django baru.
    Melakukan instalasi Django dan inisiasi projek Django dengan nama directory football-shop lengkap dengan penyiapan dependency dan konfigurasi environmentnya.

2. Membuat aplikasi dengan nama main pada proyek tersebut.
    Membentuk aplikasi main di proyek dengan command 'python manage.py startapp main' dan mendaftarkannya di variabel INSTALLED_APPS pada berkas settings.py dalam direktori football_shop.

3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Membuat file urls.py di direktori main. Di dalam file tersebut, dilakukan berbagai hal:
    a. Mengimpor berbagai fungsi yang diperlukan seperti path dari django.urls untuk mendefinisikan pola URL serta show_main dari main.views agar Django bisa memanggil fungsi view tersebut ketika ada request ke URL yang sudah dipetakan.
    b. Menambahkan app_name = 'main', ini berfungsi untuk memberikan namespace unik pada URL dalam aplikasi sehingga mudah untuk dibedakan nantinya saat ada banyak aplikasi dan endpoint dalam proyek Django.
    c. Menambahkan list dengan nama urlpatterns, ini berisi objek URLPattern yang dihasilkan oleh fungsi path(). List tersebut kemudian diisi dengan path('', show_main, name='show_main'), yang artinya hanya ada satu route '' (root), yang akan memanggil view show_main. Argumen tambahan yaitu name='show_main' berguna untuk memudahkan melakukan reverse URL menggunakan nama, bukan hardcoded string path.

    Selain itu, dilakukan pula konfigurasi routing URL untuk proyeknya yang dilakukan di urls.py yang berada di directory proyek football-shop dengan cara:
    a. Mengimpor fungsi include dari django.urls untuk menghubungkan urls.py di proyek ini dengan urls.py yang ada di direktori main.
    b. Menambahkan path('', include('main.urls')) pada list urlpatterns, ini artinya Path URL '' akan diarahkan ke rute yang didefinisikan dalam berkas urls.py aplikasi main. Path URL dibiarkan berupa string kosong agar halaman aplikasi main dapat diakses secara langsung.
    
4. Membuat model pada aplikasi main dengan nama Product
    Mengisi berkas models.py pada direktori aplikasi main dengan:
    a. Mengimport UUID (belum digunakan).
    b. Mengimport models dari django.db agar bisa membuat model di Django.
    c. Mendeklarasikan class dengan nama Product yang memiliki parameter models.Model, yaitu merupakan kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
    d. Membuat tuple dengan nama CATEGORY_CHOICES yang bertujuan untuk mendefinisikan pilihan kategori produk yang tersedia.
    e. Mengisi CATEGORY_CHOICES dengan berbagai produk yang kemungkinan nantinya akan ditambahkan ke daftar produknya.
    f. Menambahkan berbagai atribut pada modelnya, seperti name sebagai nama item dengan tipe CharField, price sebagai harga item dengan tipe IntegerField, description sebagai deskripsi item dengan tipe TextField, thumbnail sebagai gambar item dengan tipe URLField, category sebagai kategori item dengan tipe CharField, is_featured sebagai status unggulan item dengan tipe BooleanField, brand sebagai nama merek dari item dengan tipe TextField, serta stock sebagai penanda berapa stok dari item dengan tipe IntegerField.
    g. Mendeklarasikan method __str__ (belum digunakan).

5.  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    Membuat fungsi show_main di views.py yang mengirimkan data berupa NPM, nama, dan kelas melalui sebuah context. Fungsi ini kemudian me-render file template main.html menggunakan fungsi render. Dengan begitu, data yang ada di context dapat ditampilkan secara dinamis di halaman HTML sehingga halaman web menampilkan nama aplikasi, nama, dan kelas.

6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    Membuat file urls.py di direktori main. Di dalam file tersebut, dilakukan berbagai hal:
    a. Mengimpor fungsi path dari django.urls untuk mendefinisikan pola URL serta show_main dari main.views agar Django bisa memanggil fungsi view tersebut ketika ada request ke URL yang sudah dipetakan.
    b. Menambahkan app_name = 'main', ini berfungsi untuk memberikan namespace unik pada URL dalam aplikasi sehingga mudah untuk dibedakan nantinya saat ada banyak aplikasi dan endpoint dalam proyek Django.
    c. Menambahkan list dengan nama urlpatterns, ini berisi objek URLPattern yang dihasilkan oleh fungsi path(). List tersebut kemudian diisi dengan path('', show_main, name='show_main'), yang artinya hanya ada satu route '' (root), yang akan memanggil view show_main. Argumen tambahan yaitu name='show_main' berguna untuk memudahkan melakukan reverse URL menggunakan nama, bukan hardcoded string path.

7.  Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    Membuat proyek baru dengan menekan tombol Create New Project dan mengisi kolom Project Name dengan footballshop lalu menekan Create New Project di bawahnya. Kemudian mengisi tab Environs dengan apa yang ada di .env.prod di directory FOOTBALL-SHOP. Setelah itu, menambahkan URL deployment PWS di variabel ALLOWED_HOSTS pada settings.py dengan format yang telah ditentukan agar projek Django dapat diakses melalui URL deployment PWS. Terakhir, menjalankan perintah yang terdapat pada informasi Project Command pada halaman PWS. 

8. Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.
    Ini dia file README.md nya.

- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    Link bagan:
    https://drive.google.com/file/d/13j_hKLPA2eG3cwnoeUX-MIUjIw5gMAPW/view?usp=sharing
    
    Penjelasan arah panah:
    1. HTTP request dikirim (misalnya dengan mengetik URL di browser). Request ini pertama kali diterima oleh urls.py untuk dicocokkan dengan pola URL yang ada.
    2. Setelah URL ditemukan kecocokannya, request diarahkan ke fungsi view yang sesuai di views.py.
    3. Jika data dari database dibutuhkan, view akan berinteraksi dengan models.py untuk mengambil atau menyimpan data. models.py kemudian mengembalikan hasil query ke view.
    4. Setelah data siap, view meneruskan data tersebut ke template dengan menggunakan context agar bisa ditampilkan secara dinamis.
    5. Template yang sudah diisi data kemudian dikembalikan dalam bentuk HTML final ke view.
    6. View mengirimkan HTTP response yang berisi HTML final tersebut kembali ke client, sehingga tampil di browser.

- Jelaskan peran settings.py dalam proyek Django!
    Berkas settings.py berfungsi sebagai pusat konfigurasi dari proyek Django. Di dalam file ini dilakukan berbagai hal penting, antara lain:
    a. Mendefinisikan daftar aplikasi yang digunakan pada proyek melalui INSTALLED_APPS, serta middleware yang dibutuhkan untuk memproses request dan response.
    b. Menentukan jenis database (misalnya SQLite, PostgreSQL, atau MySQL) beserta detail koneksi seperti nama database, username, password, host, dan port.
    c. Mengatur lokasi template HTML, file statis (CSS, JavaScript, gambar), dan file media yang diunggah pengguna.
    d. Menyimpan SECRET_KEY, pengaturan DEBUG, ALLOWED_HOSTS, serta konfigurasi keamanan lainnya.
    e. Menentukan zona waktu (TIME_ZONE), bahasa (LANGUAGE_CODE), serta opsi internasionalisasi.
    f. Menyediakan ruang untuk menambahkan pengaturan lain seperti email, logging, cache, atau integrasi API eksternal.

- Bagaimana cara kerja migrasi database di Django?
    Migrasi database di Django adalah proses untuk menyamakan struktur database dengan definisi model yang ada di kode program. Cara kerjanya melibatkan beberapa tahap:
    a. Membuat file migrasi
    Perintah python manage.py makemigrations digunakan untuk membuat file migrasi berdasarkan perubahan yang dilakukan pada models.py. File migrasi ini berisi instruksi bagaimana database perlu diubah.
    b. Menerapkan migrasi ke database
    Perintah python manage.py migrate dijalankan untuk mengeksekusi file migrasi tersebut sehingga perubahan benar-benar diterapkan pada database (misalnya membuat tabel baru, menambah kolom, atau mengubah struktur).
    c. Sinkronisasi model dan database
    Django memastikan bahwa struktur tabel dalam database selalu sesuai dengan model Python yang sudah didefinisikan oleh developer.
    d. Pencatatan migrasi
    Django menyimpan informasi tentang migrasi yang sudah dijalankan di tabel khusus (django_migrations) sehingga tidak ada migrasi yang dijalankan dua kali.

- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    Framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karna Django memiliki beberapa keunggulan, diantaranya adalah:
    a. Django menyediakan banyak fitur bawaan sehingga developer bisa langsung fokus membangun logika aplikasi tanpa harus menulis ulang fungsi dasar.
    b. Hampir semua yang dibutuhkan untuk membangun aplikasi web modern sudah ada di dalamnya, sehingga tidak perlu lagi mencari-cari library tambahan hanya untuk kebutuhan dasar seperti session, keamanan, atau manajemen database.
    c. Django menggunakan pola MTV (Model-Template-View), salah varian dari MVC. Pola ini membantu memisahkan logika bisnis, tampilan, dan data sehingga kode lebih mudah dipahami, dikelola, dan dikembangkan bersama tim.
    d. Dengan adanya fitur admin interface bawaan, Django langsung menyediakan panel untuk mengelola data (CRUD) tanpa perlu membuat dashboard sendiri dari nol.
    e. Django tidak hanya cocok untuk proyek kecil, tetapi juga terbukti bisa menangani aplikasi berskala besar dengan trafik tinggi.

    Referensi:
    https://www.djangoproject.com
    https://www.geeksforgeeks.org/top-10-reasons-to-choose-django-framework-for-your-project

- Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    Tidak ada. Asisten dosen sudah menjalankan tugas mereka dengan baik, bahkan membuka kesempatan untuk bertanya mengenai hal yang kurang dimengerti dan memberikan bantuan apabila mahasiswa memiliki kesulitan dalam bagian tertentu. 