def pattern_count(teks, pattern):
    count = 0
    t_len = len(teks)
    p_len = len(pattern)

    if p_len == 0 or p_len > t_len:
        return 0

    for i in range(t_len - p_len + 1):
        if teks[i:i + p_len] == pattern:
            count += 1
    return count

print("B.a:", pattern_count("palindrom", "ind"))
print("B.b:", pattern_count("abakadabra", "ab"))
print("B.c:", pattern_count("hello", ""))
print("B.d:", pattern_count("ababab", "aba"))
print("B.e:", pattern_count("aaaaaa", "aa"))
print("B.f:", pattern_count("hell", "hello"))