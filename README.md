# AFL3 Bagian Password (Soal 1 sampai 4)

Repositori ini berisi skrip dan bukti untuk tugas bagian password pada AFL-3.  
Skrip dijalankan dengan Python 3. Jika interpreter di Windows adalah `py`, gunakan `py -3` sebagai pengganti `python`.

## Struktur
1. code
   - bruteforce_md5_pin.py
   - bruteforce_md5_salt1.py
   - bruteforce_md5_kdf3.py
   - dictionary_attack_pin.py
2. screenshots
   - task1_output.png
   - task2_output.png
   - task3_output.png
   - task4_output.png
3. report
   - AFL3_Template_filled.docx
4. pinlist.txt

## Penjelasan singkat tiap soal dan cara menjalankan

1) Soal 1 Brute force plain  
Tujuan mencari PIN 6 digit yang menghasilkan MD5(PIN).  
Perintah contoh:

python code/bruteforce_md5_pin.py 0110b96270248f746ecca06f1ce09746

<img width="975" height="539" alt="image" src="https://github.com/user-attachments/assets/6efb18ae-1434-4a72-96c4-e95f8dfcb712" />


2) Soal 2 Brute force dengan salt 1 digit di depan  
Tujuan mencari salt 1 digit dan PIN sehingga MD5(salt||PIN) sama dengan target.  
Perintah contoh:

python code/bruteforce_md5_salt1.py 8d4c531eb4b0f54df72aa6839abbeaec

<img width="975" height="345" alt="image" src="https://github.com/user-attachments/assets/01844511-6792-402c-86d1-0fcbd364240d" />


3) Soal 3 Brute force dengan salt 1 digit dan KDF 3 kali iterasi MD5  
Tujuan mencari salt dan PIN untuk skema h3 = MD5(MD5(MD5(salt||PIN))).  
Perintah contoh:

python code/bruteforce_md5_kdf3.py b20f8b0405b88e2b0b50eb3356d34ba7

<img width="975" height="330" alt="image" src="https://github.com/user-attachments/assets/4761854b-5c71-49cd-8036-3d10aac1a587" />


4) Soal 4 Dictionary attack dengan file pinlist.txt  
Skrip membaca pinlist.txt baris per baris dan memeriksa MD5(PIN) terhadap target.  
Perintah contoh:

python code/dictionary_attack_pin.py 0110b96270248f746ecca06f1ce09746 pinlist.txt

<img width="975" height="305" alt="image" src="https://github.com/user-attachments/assets/cfc0c5e2-55ac-4ca4-baf7-8d49c9c59509" />

# Refleksi AFL-3

Ringkasan hasil eksperimen
PIN 202345 berhasil dipulihkan di soal 1 sampai 3. Tanpa salt pada soal 1 diperlukan 202.346 percobaan. Dengan salt 7 pada soal 2 diperlukan sekitar 7.202.346 percobaan. Dengan salt 3 dan KDF tiga kali pada soal 3 diperlukan sekitar 3.202.346 percobaan. Pada soal 4 serangan dictionary bisa jauh lebih cepat jika PIN ada di wordlist.

Pelajaran utama
Ruang PIN 6 digit hanya satu juta kemungkinan. Ruang sekecil ini membuat brute force praktis dilakukan. MD5 terlalu cepat untuk menyimpan kredensial. Salt satu digit tidak memadai. Iterasi atau KDF memang memperlambat serangan tetapi harus jauh lebih kuat agar efektif.

Rekomendasi singkat
Hentikan penggunaan MD5 untuk penyimpanan kredensial. Gunakan KDF modern seperti Argon2id, bcrypt atau scrypt. Gunakan salt acak per pengguna minimal 16 byte. Atur parameter KDF sehingga hashing memakan waktu sekitar 100 sampai 500 milidetik pada server produksi. Terapkan pembatasan percobaan dan mekanisme penguncian akun. Aktifkan autentikasi multi faktor. Simpan metadata hashing agar proses rehash dan migrasi lebih mudah. Lakukan pemantauan untuk mendeteksi percobaan brute force.

