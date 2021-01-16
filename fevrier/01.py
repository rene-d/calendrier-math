#!/usr/bin/env python3

# tous les diviseurs qui sont inférieurs à 100
m = max(d for d in range(1, 1260 // 2 + 1) if 1260 % d == 0 and d < 100)

print("réponse:", m)
