import aes, os
key = os.urandom(16)
iv = os.urandom(16)

import timeit 

def aesEncrypt(key_length, key):
    print(f"====================={key_length}bit========================\n")

    start = timeit.default_timer()
    key = bytes(key, 'utf-8')
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

x = input("Nhập chuỗi cần mã hóa: ")
print("Chuỗi cần mã hóa", x)
input_key = input("Tự động tạo khóa? ")

if input_key == "yes" or input_key == "y":

    print("\n")
    print("=====================128bit========================\n")
# encrypted = aes.encrypt(key, b'Hello World')

    start = timeit.default_timer()
    encrypted = aes.AES(key).encrypt_cbc(x.encode('utf-8'), iv)
    end = timeit.default_timer()
    print("Ciphertext", encrypted)
    print("Khóa được tự động tạo", key)
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
    print("Khóa được tự động tạo", key)
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
    print("Khóa được tự động tạo", key)
    print("Thời gian mã hóa", end - start)


    start = timeit.default_timer()
    string = aes.AES(key).decrypt_cbc(encrypted, iv)
    end = timeit.default_timer()

    print("Kết quả giải mã", string)
    print("Thời gian giải mã", end - start)
    print("\n")
else:
    rounds_by_key_size = {128: 10, 192: 12, 256: 14}
    bit_to_bytes = { 128 : 16, 192: 24, 256 : 32}
    key_length = input("Chọn độ dài khóa (bit): ")
    key = input("Nhập khóa: ")
    if not rounds_by_key_size.get(int(key_length)) or not len(key) == bit_to_bytes.get(int(key_length)):
        raise Exception("Độ dài khóa không hợp lệ")
    else:
        aesEncrypt(key_length, key)
