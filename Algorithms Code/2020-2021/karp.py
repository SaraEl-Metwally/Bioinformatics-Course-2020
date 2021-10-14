d = 256


def karp(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    for i in range(m):
        # 256^0*ascii+s56^1*ascii.........
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == m:
                print("pattern is founded at index " + str(i))
        if i < n - m:
            t = (d * (t - pow(d, m - 1) * ord(text[i])) + ord(text[i + m])) % q

            if t < 0:
                t = t + q


text = "THERE WOULD HAVE BEEN A TIME FOR SUCH A WORLD"
pattern = "WORLD"
q = 101
karp(pattern, text,q)
