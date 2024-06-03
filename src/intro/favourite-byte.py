import binascii

# Given ciphertext
ciphertext = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

# Convert ciphertext from hex to bytes
ciphertext_bytes = binascii.unhexlify(ciphertext)

# Try all possible byte values (0-255) to find the secret key
broke = False
for key in range(256):
    plaintext_bytes = bytes([b ^ key for b in ciphertext_bytes])
    plaintext = plaintext_bytes.decode()
    if "crypto" in plaintext:
        print(f"The flag is: \n{plaintext}")
        broke = True
        break

if not broke:
    print(f"Could not decode flag: \n{ciphertext}")