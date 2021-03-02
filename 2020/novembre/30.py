#!/usr/bin/env python3

rang = ("\033[91ma", "\033[92mb", "\033[93mc", "\033[94md")
for i in range(1, 21):
    a, b, c, d = rang
    if i % 2 == 1:
        rang = (b, c, a, d)
    else:
        rang = (a, d, b, c)
    print(f"\033[2m{i:2}\033[0m {' '.join(rang)} \033[0m")
