def naive_string_matching(text, pattern):
    for s in range(0, len(text) - len(pattern) + 1):
        if pattern == text[s:s + len(pattern)]:
            print(f"Przesunięcie {s} jest poprawne")


from time import time

if __name__ == "__main__":
    # naive_string_matching("abaabaaaaba", "aba")

    text = open("ustawa", encoding="utf8").read()

    t = time()
    naive_string_matching(text, "art")
    print(time() - t)





