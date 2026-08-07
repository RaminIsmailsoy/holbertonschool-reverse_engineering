import binascii

# Given encrypted flag in hex
encrypted_hex = "9E89846A786585866A977D797C846380"

# Convert Hex back to Bytes
encrypted_bytes = binascii.unhexlify(encrypted_hex)

# Encryption Key (Extracted from Binary)
key = b"mysecretkey"

# Reverse the Encryption
original_flag = bytearray(len(encrypted_bytes))
for i in range(len(encrypted_bytes)):
    original_flag[i] = (encrypted_bytes[i] - key[(i + 1) % len(key)]) ^ key[i % len(key)]

# Print the Recovered Flag
print("Recovered Flag:", original_flag.decode())
