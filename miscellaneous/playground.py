#!/usr/bin/env python3

import bitcoin
import hashlib
import random

N = bitcoin.N
G = bitcoin.G


def calcul_P(x):
    P = bitcoin.P
    y = pow(int(x * x * x + 7), int((P + 1) // 4), int(P))
    return [(x, y), (x, P - y)]


inv = bitcoin.inv
fast_multiply = bitcoin.fast_multiply
fast_add = bitcoin.fast_add


def fast_substract(a, b):
    x1, y1 = a
    x2, y2 = b
    return fast_add((x1, y1), (x2, -y2))


def get_z(msg):
    hash = hashlib.sha256(msg.encode()).hexdigest()
    return bitcoin.hash_to_int(hash)


def sign(z, k, priv):
    r, y = fast_multiply(G, k)
    s = (inv(k, N) * (z + r * bitcoin.decode_privkey(priv))) % N
    v, r, s = 27 + ((y % 2) ^ (0 if s * 2 < N else 1)), r, s if s * 2 < N else N - s
    return v, r, s


# Generate secret key & the corresponding public key and address
sk = bitcoin.random_key()
pk = bitcoin.privtopub(sk)
print("+ Priv key = {:s}".format(sk))

# Sign 3 messages
d = bitcoin.decode_privkey(sk)
z1 = get_z("my_message_1")
k1 = random.SystemRandom().randrange(1, N)
v1, r1, s1 = sign(z1, k1, sk)
z2 = get_z("my_message_2")
k2 = random.SystemRandom().randrange(1, N)
v2, r2, s2 = sign(z2, k2, sk)
z3 = get_z("my_message_3")
k3 = random.SystemRandom().randrange(1, N)
v3, r3, s3 = sign(z3, k3, sk)

# Express k1 from k2
k1_from_k2 = [
    ((z2 * r1 - z1 * r2) + _k2 * (s2 * r1)) * inv(s1 * r2, N) % N
    for _k2 in [k2, N - k2]
]
assert k1 in k1_from_k2 or N - k1 in k1_from_k2

# Express k1 from k3
k1_from_k3 = [
    ((z3 * r1 - z1 * r3) + _k3 * (s3 * r1)) * inv(s1 * r3, N) % N
    for _k3 in [k3, N - k3]
]
assert k1 in k1_from_k3 or N - k1 in k1_from_k3

# Express k2 from k3
k2_from_k3 = [
    ((z3 * r2 - z2 * r3) + _k3 * (s3 * r2)) * inv(s2 * r3, N) % N
    for _k3 in [k3, N - k3]
]
assert k2 in k2_from_k3 or N - k2 in k2_from_k3

# Express k1, k2 & k3 with d
_a = r1 * inv(s1, N) % N
_b = z1 * inv(s1, N) % N
assert (d * _a + _b) % N == k1 or (d * _a + _b) % N == N - k1
_c = r2 * inv(s2, N) % N
_d = z2 * inv(s2, N) % N
assert (d * _c + _d) % N == k2 or (d * _c + _d) % N == N - k2
_e = r3 * inv(s3, N) % N
_f = z3 * inv(s3, N) % N
assert (d * _e + _f) % N == k3 or (d * _e + _f) % N == N - k3
