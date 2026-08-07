from struct import unpack

# Given values from analysis
exponent = 0x0000FFFFFFFFFFFF
modulus = 0x0FFFFFFFFFFFFFFB
encrypted_flag_hex = (
    "8e82d972b66c836fa896da60a7779a69"
    "bc84db77a0729877a582d1758c778461"
    "a883da69ba70905fa498c14fba6da861"
    "9980c063a763f700"
)

# Convert the encrypted flag from hex to bytes
encrypted_flag = bytes.fromhex(encrypted_flag_hex)

# Modular exponentiation to compute decryption key (naive method)
def naive_modular_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

# Compute the decryption key
decryption_key = naive_modular_exponentiation(2, exponent, modulus)

# Function to decrypt the flag
def decrypt_flag(encrypted_flag, decryption_key):
    decrypted_flag = []
    
    # Process each 8-byte chunk
    for i in range(0, len(encrypted_flag), 8):
        block = encrypted_flag[i:i+8]
        # Convert to integer
        block_int = int.from_bytes(block, byteorder='little')
        
        # XOR the block with the decryption key
        decrypted_block = block_int ^ decryption_key
        
        # Convert the decrypted block back to bytes and then to a string
        decrypted_flag.append(decrypted_block.to_bytes(8, byteorder='little').decode(errors='ignore'))
    
    return ''.join(decrypted_flag)

# Decrypt the flag
decrypted_flag = decrypt_flag(encrypted_flag, decryption_key)

# Print the decrypted flag
print("Decrypted Flag:", decrypted_flag)
