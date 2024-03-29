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

CON = {1: [17],
       2: [5],
       3: [22],
       4: [10],
       5: [0],
       6: [0, 13],
       7: [0, 13],
       8: [0, 13]}

def caesar(text, key, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    c = ""
    for i in text.upper():
        if i in alphabet:
            c += alphabet[(alphabet.index(i) + key) % len(alphabet)]
    return c

def commutation(pairs):
    stop = False
    pairs = pairs.upper().split()
    p = {i[0]: i[1] for i in pairs}
    pairs_2 = [ii for ii in pairs if ii[::-1] in pairs]
    pairs_3 = []
    for iii in pairs:
        if (iii[1] in p.keys() and iii not in pairs_2) or (len(pairs) != len(p)):
            stop = True
        else:
            pairs_3.append(iii[::-1])
    pairs.extend(pairs_3)
    p_2 = {i[0]: i[1] for i in pairs}
    return [p_2, stop]
    
def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    com = commutation(pairs)
    p = com[0]
    if not com[1]:
        cipher = ""
        flag2, flag3 = 0, 0
        for i in text.upper():
            if i in ROTORS[0]:
                if i in p.keys():
                    i = p[i]
                if shift3 < 25:
                    shift3 += 1
                    if (shift3 in CON[rot3]) or ((shift2 + 1) in CON[rot2]):
                        shift2 += 1
                    if (shift2 in CON[rot2]) and flag2 == 0:
                        flag2 = 1
                        shift1 += 1
                    if shift1 in CON[rot1] and flag3 == 0:
                        shift2 += 1
                        flag3 = 1
                else:
                    shift3 = 0            
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
                if sr_3 in p:
                    sr_3 = p[sr_3]
                cipher += sr_3
        return cipher
    else:
        return "Извините, невозможно произвести коммутацию"
