from Crypto.Cipher import AES

plaintext = bytearray.fromhex('255044462d312e350a25d0d4c5d80a34')
ciphertext = bytearray.fromhex('d06bf9d0dab8e8ef880660d2af65aa82')
iv = bytearray.fromhex('09080706050403020100A2B2C2D2E2F2')

with open('possible_keys.txt') as possible:
    keys = possible.readlines()

for k in keys:
    k = k.rstrip('\n')
    key = bytearray.fromhex(k)
    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    generated_ciphertext = cipher.encrypt(plaintext)
    if generated_ciphertext == ciphertext:
        print("correct key:", k)
        exit(0)
