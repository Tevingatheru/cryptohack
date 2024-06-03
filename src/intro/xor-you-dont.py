ciphertext = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ciphertext_bytes = bytearray.fromhex(ciphertext)

flag_format = 'crypto{1'

key_bytes = bytes([c1 ^ ord(c2) for c1, c2 in zip(ciphertext_bytes, flag_format)])
key = key_bytes.decode()

plaintext_bytes = bytes([c ^ ord(k) for c, k in zip(ciphertext_bytes, key * (len(ciphertext_bytes) // len(key) + 1))])
plaintext = plaintext_bytes.decode()

print(f"The flag is: {plaintext}")