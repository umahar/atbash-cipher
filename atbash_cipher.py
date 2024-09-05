def encode(plain_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    cipher_text = ""
    for i in plain_text.lower():
        if not i.isalpha():
            if i in [",", "."]:
                continue
            cipher_text = cipher_text + i
        else:
            cipher_text = cipher_text + cipher[plain.index(i)]
    cipher_text = cipher_text.replace(" ", "")
    grouped_chars = []
    for i in range(0, len(cipher_text), 5):
        grouped_chars.append(cipher_text[i : i + 5])
    result = " ".join(grouped_chars)
    return result


def decode(ciphered_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"

    plain_text = ""
    for i in ciphered_text:
        if not i.isalpha():
            plain_text = plain_text + i
        else:
            plain_text = plain_text + plain[cipher.index(i)]
    return plain_text.replace(" ", "")


print(encode("Testing,1 2 3, testing."))
print(decode("gvhg "))
