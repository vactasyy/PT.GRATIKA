def hitung_huruf(s):
    from collections import defaultdict

    s = s.replace(" ", "")
    huruf_dict = defaultdict(int)

    for char in s:
        if char.isalpha():
            huruf_dict[char] += 1

    hasil = dict(sorted(huruf_dict.items()))
    print("C:", hasil)

hitung_huruf("Hello World")
hitung_huruf("Bismillah")
hitung_huruf("MasyaAllah")
