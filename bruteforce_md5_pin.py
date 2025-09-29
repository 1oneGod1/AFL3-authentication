import hashlib
import time
import sys

def cari_pin(target_hash):
    target = target_hash.lower()
    mulai = time.time()
    for i in range(1000000):
        pin = f"{i:06d}"               # format 6 digit dengan nol di depan
        h = hashlib.md5(pin.encode()).hexdigest()
        if h == target:
            selesai = time.time()
            return pin, i+1, selesai - mulai
    selesai = time.time()
    return None, 1000000, selesai - mulai

def penggunaan():
    print("Penggunaan: python bruteforce_md5_pin.py <md5-hash>")
    print("Contoh:  python bruteforce_md5_pin.py 0110b96270248f746ecca06f1ce09746")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Argumen tidak lengkap.")
        penggunaan()
        sys.exit(1)

    hash_target = sys.argv[1]
    print(f"Mencari PIN 6-digit untuk hash: {hash_target}")
    pin, jumlah_cek, waktu = cari_pin(hash_target)

    if pin:
        print("=========================================")
        print(f"Hasil: DITEMUKAN PIN = {pin}")
        print(f"Jumlah kandidat yang diperiksa: {jumlah_cek}")
        print(f"Waktu eksekusi: {waktu:.3f} detik")
        print("=========================================")
    else:
        print("=========================================")
        print("Hasil: PIN tidak ditemukan dalam rentang 000000-999999")
        print(f"Jumlah kandidat yang diperiksa: {jumlah_cek}")
        print(f"Waktu eksekusi: {waktu:.3f} detik")
        print("=========================================")
