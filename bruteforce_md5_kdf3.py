# Mencari salt 1-digit + PIN 6-digit dengan KDF 3x (iterated MD5)
import hashlib, time, sys

def cari_salt_pin_kdf3(target_hash):
    target = target_hash.lower()
    mulai = time.time()
    tries = 0
    for salt_digit in range(10):
        salt = str(salt_digit)
        for i in range(1000000):
            pin = f"{i:06d}"
            # iterated MD5
            h = (salt + pin).encode()
            h = hashlib.md5(h).hexdigest().encode()
            h = hashlib.md5(h).hexdigest().encode()
            h = hashlib.md5(h).hexdigest()
            tries += 1
            if h == target:
                selesai = time.time()
                return salt, pin, tries, selesai-mulai
    selesai = time.time()
    return None, None, tries, selesai-mulai

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Penggunaan: python bruteforce_md5_kdf3.py <md5-hash>")
        sys.exit(1)
    target = sys.argv[1]
    salt, pin, tries, waktu = cari_salt_pin_kdf3(target)
    if salt is not None:
        print("=========================================")
        print(f"Hasil: DITEMUKAN salt = '{salt}', PIN = '{pin}'")
        print(f"Jumlah kandidat yang diperiksa: {tries}")
        print(f"Waktu eksekusi: {waktu:.3f} detik")
        print("=========================================")
    else:
        print("Tidak ditemukan kombinasi dalam ruang pencarian.")
        print(f"Jumlah kandidat yang diperiksa: {tries}")
        print(f"Waktu eksekusi: {waktu:.3f} detik")
