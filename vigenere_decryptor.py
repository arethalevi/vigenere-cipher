import pandas as pd
import string
import itertools

# inputting the txt data
file_name = str(input("nama file: "))
key = str(input("Masukkan key: "))

# read the data
file = open("{}.txt".format(file_name), "r")
message = file.read()

def decrypting(message, key):
    # creating the tabula recta
    table = []
    alphabet = string.ascii_lowercase

    for i in range(0, 26):
        shifted = alphabet[i:] + alphabet[:i]
        table.append(list(shifted))

    df_table = pd.DataFrame(table)
    df_table.columns = list(alphabet)
    df_table.index = list(alphabet)

    #creating the keystream
    message = message.lower()
    repeat = itertools.cycle(key)
    keystream = [next(repeat) if letter.isalpha() else letter for letter in message]

    lv = list(message)
    lb = keystream

    #looping to translate the text
    decrypted = []
    for i in range(len(lv)):
        if lv[i] and lb[i] in alphabet:
            j = df_table.loc[df_table[lb[i]] == lv[i]]
            decrypted.append(j.index[0])
        else:
            decrypted.append(lv[i])
    stl = ''.join([str(elem) for elem in decrypted])
    return stl

print(decrypting(message, key))

# save to txt
with open('decrypted {}.txt'.format(file_name), 'w') as f:
    f.write(decrypting(message, key))

