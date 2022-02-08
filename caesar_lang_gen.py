# -*- coding: utf-8 -*-
"""

@author: Robert Dosa
"""

from string import ascii_lowercase

consonants = list(ascii_lowercase)

vowels = ["a", "e", "o", "u", "i"]

for i in range(len(vowels)):
    consonants.remove(vowels[i])

# Consonant mapping

cons_mapping = {}
cons_num = enumerate(consonants)
for a, b in cons_num:
    cons_mapping.update({a: b})

# Vowel mapping

vowels_mapping = {}
vow_num = enumerate(vowels)
for a, b in vow_num:
    vowels_mapping.update({a: b})


def letter_pos(letter, mapping):
    """Returns the key of a specified letter in the mapping dictionary"""
    for key in mapping.keys():
        if mapping.get(key) == letter:
            return key


def encrypt(st, pkey):
    """Encrypting function that implements the Caesar cipher formula such that E(x)=(x+p) mod l, where
    E(x) is the encrypted letter for x, p is the key and l, in this case, is the length of the mapping"""
    en_ls = []
    for c in st:
        if c in cons_mapping.values():
            en_ls.append(cons_mapping.get((letter_pos(c, cons_mapping) + pkey) % 21))
        elif c in vowels_mapping.values():
            en_ls.append(vowels_mapping.get((letter_pos(c, vowels_mapping) + pkey) % 5))
        else:
            en_ls.append(c)
    return "".join(en_ls)


def decrypt(encrypted, pkey):
    """Decrypting function that implements the Caesar cipher formula such that D(x)=(x-p) mod l, where
    D(x) is the decrypted letter for x, p is the key and l, in this case, is the length of the mapping"""
    dc_ls = []
    for c in encrypted:
        if c in cons_mapping.values():
            dc_ls.append(cons_mapping.get((letter_pos(c, cons_mapping) - pkey) % 21))
        elif c in vowels_mapping.values():
            dc_ls.append(vowels_mapping.get((letter_pos(c, vowels_mapping) - pkey) % 5))
        else:
            dc_ls.append(c)
    return "".join(dc_ls)


def manual_text():
    user_input = input("Enter text: ").lower()
    while True:
        input_key = input("Enter the key (1 - 9): ")
        if input_key not in [str(i) for i in range(1, 10)]:
            continue
        else:
            input_key = int(input_key)
            break
    print(encrypt(user_input, input_key))


def encrypt_file():
    while True:
        input_key = input("Enter the key (1 - 9): ")
        if input_key not in [str(i) for i in range(1, 10)]:
            continue
        else:
            input_key = int(input_key)
            break
    file_name = input("Enter the new file name: ")
    new_file = open(file_name + ".txt", "w+")
    new_file.write(encrypt(open_txt(), input_key))
    new_file.close()
    print("encrypted.txt has been created!")
