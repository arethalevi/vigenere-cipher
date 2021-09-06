import string
import pandas as pd
import itertools

# inputting the txt data
file_name = str(input("Input the file name: "))
key = str(input("Input the key: "))

# read txt file
file = open("{}.txt".format(file_name), "r")
message = file.read()

# encrypt
def encrypting(key, message):
    # creating the tabula recta
    table = []
    alphabet = string.ascii_lowercase
    for i in range(0, 26):
        shifted = alphabet[i:] + alphabet[:i]
        table.append(list(shifted))
    df_table = pd.DataFrame(table)
    df_table.columns = list(alphabet)
    df_table.index = list(alphabet)

    # creating the keystream
    message = message.lower()
    repeat = itertools.cycle(key)
    keystream = [next(repeat) if letter.isalpha() else letter for letter in message]
   
    ly = list(message)
    lx = keystream

    # starting the looping to translate the text according the keystream and tabula recta
    encrypted = []
    for i in range(len(ly)):
        if ly[i] and lx[i] in alphabet:
            a = df_table._get_value(ly[i], lx[i])
            encrypted.append(a)
        else:
            encrypted.append(ly[i])

    list2string = ''.join(encrypted)
    return list2string.upper()


print(encrypting(key, message))

# save the encrypted message to txt
with open('encrypted {}.txt'.format(file_name), 'w') as f:
    f.write(encrypting(key,message))