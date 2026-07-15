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
    # 1. You must define candidate here. For example:
    candidate = k + n  # (Replace this with your actual math logic)
    
    # 2. Now you can safely check it:
    if candidate == q:
         
        pass



