tautan aplikasi: https://muhammad-rizky413-footballshop.pbp.cs.ui.ac.id

- Cara mengimplementasikan checklist secara step-by-step:
1. Membuat sebuah proyek Django baru.
    Melakukan instalasi Django dan inisiasi projek Django dengan nama directory football-shop lengkap dengan penyiapan dependency dan konfigurasi environmentnya.

2. Membuat aplikasi dengan nama main pada proyek tersebut.
    Membentuk aplikasi main di proyek dengan command 'python manage.py startapp main' dan mendaftarkannya di variabel INSTALLED_APPS pada berkas settings.py dalam direktori football_news.

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