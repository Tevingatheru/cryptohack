ciphertext = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
# key = "crypto{ASCII_pr1nt4bl3}"
# key = "xor"
key = "exor"
# key = "crypto{z3n_0f_pyth0n}"
# Convert cip
# hertext from hex to bytes
ciphertext_bytes = bytearray.fromhex(ciphertext)

# Decrypt using XOR operation (repeat key to match ciphertext length)
decrypted_bytes = bytes(c ^ ord(k) for c, k in zip(ciphertext_bytes, key * (len(ciphertext_bytes) // len(key) + 1)))

# Convert decrypted bytes to string
decrypted_text = decrypted_bytes.decode()

print(decrypted_text)
