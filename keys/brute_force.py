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
    # Delete the "some_function(n)" line if it isn't yours
    if candidate[0] == q:  # Make sure "candidate" is defined before this line
        pass


