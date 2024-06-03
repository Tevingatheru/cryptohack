import base64

# hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
hex_string = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

bytes_data = bytes.fromhex(hex_string)

# Encode the bytes into Base64
base64_encoded = base64.b64encode(bytes_data)

# Print the Base64-encoded string
print(base64_encoded.decode())
