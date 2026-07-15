#!/usr/bin/env python3

from bitcoin import G, fast_multiply
import random

# use with an even number
nbits = 16

# generate private and public key
k = random.randint(0, 2**nbits - 2 ** (nbits // 2))
q = fast_multiply(G, k)[0]
print("SEARCH - {0}".format(k))

for n in range(2**nbits - 2 ** (nbits // 2)):
    # Ensure this block uses consistent spaces/tabs
    candidate = some_function(n)  # (Example line 15)
    if candidate[0] == q:         # Line 16 must align with line 15
        pass

