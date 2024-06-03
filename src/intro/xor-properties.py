import binascii

# Given values
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_XOR_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_XOR_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

# Convert hex strings to bytes
KEY1_bytes = binascii.unhexlify(KEY1)
KEY2_XOR_KEY1_bytes = binascii.unhexlify(KEY2_XOR_KEY1)
KEY2_XOR_KEY3_bytes = binascii.unhexlify(KEY2_XOR_KEY3)
FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2_bytes = binascii.unhexlify(FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2)

# Use XOR properties to recover KEY3
KEY3_bytes = bytes([a ^ b for a, b in zip(KEY2_XOR_KEY1_bytes, KEY2_XOR_KEY3_bytes)])

# Use XOR properties to recover the flag
flag_bytes = bytes([a ^ b ^ c ^ d for a, b, c, d in zip(FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2_bytes, KEY1_bytes, KEY3_bytes, KEY2_XOR_KEY1_bytes)])
flag = flag_bytes.decode()

print(f"The flag is:\n{flag}")