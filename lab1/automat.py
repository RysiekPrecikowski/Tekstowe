from pprint import pprint
import re

def fa_string_matching(text, pattern):
    q = 0

    delta = transition_table(pattern)

    for s in range(0, len(text)):
        q = delta[q].get(text[s], 0) # jesli nie ma znaku w tablicy przejscia to domyslnie wrzuca nam 0

        if (q == len(delta) - 1):
            print(f"Przesunięcie {s + 1 - q} jest poprawne")
            # s + 1 - ponieważ przeczytaliśmy znak o indeksie s, więc przesunięcie jest po tym znaku


def transition_table(pattern):
    result = []

    alphabet = set(pattern)

    for q in range(0, len(pattern) + 1):
        result.append({})
        for a in alphabet:
            k = min(len(pattern) + 1, q + 2)
            while True:
                k = k - 1
                if re.search(f"{pattern[:k]}$", pattern[:q] + a):
                    break
            result[q][a] = k
    return result





if __name__ == "__main__":
    fa_string_matching("abaabaaaaba", "aba")

    text = open("ustawa", encoding="utf8")
    t = text.read()

    # fa_string_matching(t, transition_table("art"))
