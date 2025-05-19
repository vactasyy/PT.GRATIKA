def hitung_huruf(s):
    from collections import defaultdict

    s = s.replace(" ", "")  # Hilangkan spasi
    huruf_dict = defaultdict(int)

    for char in s:
        if char.isalpha():  # Hanya huruf
            huruf_dict[char] += 1

    hasil = dict(sorted(huruf_dict.items()))
    print("C:", hasil)

# Contoh penggunaan:
hitung_huruf("Hello World")
hitung_huruf("Bismillah")
hitung_huruf("MasyaAllah")