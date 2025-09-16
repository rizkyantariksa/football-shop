tautan aplikasi: https://muhammad-rizky413-footballshop.pbp.cs.ui.ac.id

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