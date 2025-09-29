
# Membaca pinlist.txt (1 PIN per baris) dan mencari PIN yang MD5(PIN) == target

import hashlib
import time
import sys
import os

def md5_hex(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

def cari_dengan_wordlist(target_hash: str, wordlist_path: str):
    target = target_hash.lower()
    if not os.path.isfile(wordlist_path):
        print(f"File wordlist tidak ditemukan: {wordlist_path}")
        return None, 0, 0.0

    mulai = time.time()
    checked = 0
    found = None
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            pin = line.strip()
            if not pin:
                continue
            checked += 1
            h = md5_hex(pin)
            if h == target:
                selesai = time.time()
                found = pin
                return found, checked, selesai - mulai
    selesai = time.time()
    return None, checked, selesai - mulai

def usage():
    print("Penggunaan: python dictionary_attack_pin.py <md5-hash> [wordlist_file]")
    print("Contoh:  python dictionary_attack_pin.py 0110b96270248f746ecca06f1ce09746 pinlist.txt")
    print("Jika file wordlist tidak diberikan, skrip akan mencari 'pinlist.txt' di folder saat ini.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    target = sys.argv[1]
    wordlist = sys.argv[2] if len(sys.argv) >= 3 else "pinlist.txt"

    print(f"Mencari hash target: {target}")
    result, checked, elapsed = cari_dengan_wordlist(target, wordlist)
    if result:
        print("=========================================")
        print(f"Hasil: DITEMUKAN PIN = {result}")
        print(f"Jumlah kandidat yang diperiksa: {checked}")
        print(f"Waktu eksekusi: {elapsed:.3f} detik")
        print("=========================================")
    else:
        print("=========================================")
        print("Hasil: PIN tidak ditemukan di wordlist.")
        print(f"Jumlah kandidat yang diperiksa: {checked}")
        print(f"Waktu eksekusi: {elapsed:.3f} detik")
        print("=========================================")
