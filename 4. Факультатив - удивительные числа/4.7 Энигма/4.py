REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
              2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
              3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
              4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
              }

ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
          2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
          3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
          4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
          5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
          6: 'JPGVOUMFYQBENHZRDKASXLICTW',
          7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT', 
          8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
          'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
          'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
          }

def caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    c = ""
    for i in text.upper():
        if i in alphabet:
            c += alphabet[(alphabet.index(i) + key) % len(alphabet)]
    return c

def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    cipher = ""
    for i in text.upper():
        if i in ROTORS[0]:
            s_3 = caesar(i, shift3, ROTORS[0])
            r_3 = ROTORS[rot3][ROTORS[0].index(s_3)]
            s_2 = caesar(r_3, shift2 - shift3, ROTORS[0])
            r_2 = ROTORS[rot2][ROTORS[0].index(s_2)]
            s_1 = caesar(r_2, shift1 - shift2, ROTORS[0])
            r_1 = ROTORS[rot1][ROTORS[0].index(s_1)]
            s_0 = caesar(r_1, shift1 * (-1), ROTORS[0])
            r = REFLECTORS[ref][REFLECTORS[0].index(s_0)]
            sr_0 = caesar(r, shift1, ROTORS[0])
            rr_1 = ROTORS[0][ROTORS[rot1].index(sr_0)]
            sr_1 = caesar(rr_1, shift2 - shift1, ROTORS[0])
            rr_2 = ROTORS[0][ROTORS[rot2].index(sr_1)]
            sr_2 = caesar(rr_2, shift3 - shift2, ROTORS[0])
            rr_3 = ROTORS[0][ROTORS[rot3].index(sr_2)]
            sr_3 = caesar(rr_3, shift3 * (-1), ROTORS[0])
            cipher += sr_3
    return cipher
