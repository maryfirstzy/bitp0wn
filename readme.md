# Bitp0wn

```
This repo is a showcase of algorithms to get some fun with bitcoin cryptography.
The scripts are not optimised and are only proof-of-concepts (not suited for production).
```

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

### keys

+ __[keys/brute_force.py](https://github.com/marcvincenti/bitp0wn/blob/master/keys/brute_force.py)__ : You will find a simple bruteforce algorithm wich test every possibilities to retrieve a private key from the public key.

+ __[keys/bsgs.py](https://github.com/marcvincenti/bitp0wn/blob/master/keys/bsgs.py)__ : The Baby-step Giant-step algorithm, it has order of 2^(n/2) time complexity and space complexity.

+ __[keys/pollard_rho.py](https://github.com/marcvincenti/bitp0wn/blob/master/keys/pollard_rho.py)__ : The Pollard Rho algorithm, it has order of 2^(n/2) time complexity but is slower than bsgs in practice. However, this algorithm has a constant space complexity.

### signatures

+ __[signatures/fake_sig.py](https://github.com/marcvincenti/bitp0wn/blob/master/signatures/fake_sig.py)__ : In this script, we show why hashing the message in ecdsa is important. Because without it, you can generate plenty of signatures that can be verified with the public key of your choice.

+ __[signatures/r_exploit_ecdsa.py](https://github.com/marcvincenti/bitp0wn/blob/master/signatures/r_exploit_ecdsa.py)__ : This algorithm exploit a failure in signatures generation. If the same address use the same k in 2 differents signatures (_i.e_ same r-value), then you can recalculate the private key instantly.

+ __[signatures/r_exploit_schnorr.py](https://github.com/marcvincenti/bitp0wn/blob/master/signatures/r_exploit_schnorr.py)__ : Same as precedent exploit but for schnorr signatures instead of ecdsa signatures.

### miscellaneous

+ __[miscellaneous/playground.py](https://github.com/marcvincenti/bitp0wn/blob/master/miscellaneous/playground.py)__ : This file contains relations between values of differents signatures for an identical address.

+ __[miscellaneous/shamir-shared-secret.py](https://github.com/marcvincenti/bitp0wn/blob/master/miscellaneous/shamir-shared-secret.py)__ : Shamir Shared Secret Scheme to distribute a secret to n entities wich can be recovered with k < n shares.

+ __[miscellaneous/tiny-curve.py](https://github.com/marcvincenti/bitp0wn/blob/master/miscellaneous/tiny-curve.py)__ : This script let you generate your own elliptic curves (not secure, never use the curves in production). This will be useful to test some of our algorithms on smaller curves.
