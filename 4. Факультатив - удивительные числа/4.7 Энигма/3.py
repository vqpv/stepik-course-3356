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

def enigma(text, ref, rot1, rot2, rot3):
    cipher = ""
    for i in text.upper():
        if i in ROTORS[0]:
            r_3 = ROTORS[rot3][ROTORS[0].index(i)]
            r_2 = ROTORS[rot2][ROTORS[0].index(r_3)]
            r_1 = ROTORS[rot1][ROTORS[0].index(r_2)]
            r = REFLECTORS[ref][REFLECTORS[0].index(r_1)]
            rr_1 = ROTORS[0][ROTORS[rot1].index(r)]
            rr_2 = ROTORS[0][ROTORS[rot2].index(rr_1)]
            rr_3 = ROTORS[0][ROTORS[rot3].index(rr_2)]
            cipher += rr_3
    return cipher
