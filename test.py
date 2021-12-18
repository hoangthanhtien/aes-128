import aes, os
key = os.urandom(16)
iv = os.urandom(16)

import timeit 

x = input("Nhập chuỗi cần mã hóa: ")
print("Chuỗi cần mã hóa", x)

# start = timeit.default_timer()
# encrypted = aes.AES(key).encrypt_ctr(x.encode('utf-8'), iv)
# end = timeit.default_timer()

print("\n")
print("=====================128bit========================\n")
# encrypted = aes.encrypt(key, b'Hello World')

start = timeit.default_timer()
encrypted = aes.AES(key).encrypt_cbc(x.encode('utf-8'), iv)
end = timeit.default_timer()
print("Ciphertext", encrypted)
print("Thời gian mã hóa", end - start)


start = timeit.default_timer()
string = aes.AES(key).decrypt_cbc(encrypted, iv)
end = timeit.default_timer()

print("Kết quả giải mã", string)
print("Thời gian giải mã", end - start)
print("\n")

print("=====================192bit========================\n")


start = timeit.default_timer()
key = os.urandom(24)
encrypted = aes.AES(key).encrypt_cbc(x.encode('utf-8'), iv)
end = timeit.default_timer()
print("Ciphertext", encrypted)
print("Thời gian mã hóa", end - start)


start = timeit.default_timer()
string = aes.AES(key).decrypt_cbc(encrypted, iv)
end = timeit.default_timer()

print("Kết quả giải mã", string)
print("Thời gian giải mã", end - start)
print("\n")

print("=====================256bit========================\n")


start = timeit.default_timer()
key = os.urandom(32)
encrypted = aes.AES(key).encrypt_cbc(x.encode('utf-8'), iv)
end = timeit.default_timer()
print("Ciphertext", encrypted)
print("Thời gian mã hóa", end - start)


start = timeit.default_timer()
string = aes.AES(key).decrypt_cbc(encrypted, iv)
end = timeit.default_timer()

print("Kết quả giải mã", string)
print("Thời gian giải mã", end - start)
print("\n")
