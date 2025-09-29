#!/usr/bin/env python3
# bruteforce_md5_salt1_id.py
# Mencari salt 1 digit (0-9) + PIN 6-digit sehingga MD5(salt||PIN) = target

import hashlib, time, sys

def cari_salt_pin(target_hash):
    target = target_hash.lower()
    mulai = time.time()
    tries = 0
    for salt_digit in range(10):
        salt = str(salt_digit)
        for i in range(1000000):
            pin = f"{i:06d}"
            combo = salt + pin
            h = hashlib.md5(combo.encode()).hexdigest()
            tries += 1
            if h == target:
                selesai = time.time()
                return salt, pin, tries, selesai-mulai
    selesai = time.time()
    return None, None, tries, selesai-mulai

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Penggunaan: python bruteforce_md5_salt1.py <md5-hash>")
        sys.exit(1)
    target_hash = sys.argv[1]
    salt, pin, tries, waktu = cari_salt_pin(target_hash)
    if salt is not None:
        print("=========================================")
        print(f"Hasil: DITEMUKAN salt = '{salt}', PIN = '{pin}'")
        print(f"Jumlah kandidat yang diperiksa: {tries}")
        print(f"Waktu eksekusi: {waktu:.3f} detik")
        print("=========================================")
    else:
        print("Tidak ditemukan kombinasi salt(0-9) + 6-digit PIN")
        print(f"Jumlah kandidat yang diperiksa: {tries}")
        print(f"Waktu eksekusi: {waktu:.3f} detik")
