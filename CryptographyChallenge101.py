# https://www.khanacademy.org/computing/computer-science/cryptography/cryptochallenge/a/crypto-clue-1

import string
alphabet = list(string.ascii_lowercase)

# Clue 1
def caesarCipherDecryptWithMostFrequentToEAsShift(code):
    letters = list(code)
    counts = {}
    most_frequent = letters[0]
    most_frequent_num = 0
    for letter in letters:
        if letter not in counts.keys():
            counts[letter] = letters.count(letter)
            if counts[letter] > most_frequent_num:
                most_frequent = letter
                most_frequent_num = counts[letter]

    shift = (alphabet.index('e') - alphabet.index(most_frequent)) % len(alphabet)
    message = [alphabet[(alphabet.index(c) + shift) % len(alphabet)] for c in letters]
    return ''.join(message)

text_1 = "gluhtlishjrvbadvyyplkaohavbyjpwolypzavvdlhrvuuleatlzzhnlzdpajoavcpnlulyljpwolyrlfdvykpzaolopkkluzftivsvmklhaoputfmhcvypalovsilpuluk"
text_2 = "vwduwljudeehghyhubwklqjlfrxogilqgsohdvhuhwxuqdqbeoxhsulqwviruydxowdqgdodupghvljqedvhgrqzklfkedqnbrxghflghrqldpvhwwlqjxsvdihkrxvhfr"
ans_1 = caesarCipherDecryptWithMostFrequentToEAsShift(text_1)
ans_2 = caesarCipherDecryptWithMostFrequentToEAsShift(text_2)
print(ans_2+ans_1)

## Holbein is a german painter - could be his name Hans or a painting...
## It is actually the hidden symbol of death in The Ambassadors a Skull

# Clue 2
def vigenereCipher(code, key):
    key_ind = 0
    message = []
    for c in list(code):
        message.append(alphabet[(alphabet.index(c) + (alphabet.index(key[key_ind]))) % len(alphabet)])
        key_ind = key_ind + 1 if (key_ind + 1) < len(key) else 0
    return ''.join(message)

key = "skull"
text_3 = "klkbnqlcytfysryucocphgbdizzfcmjwkuchzyeswfogmmetwwossdchrzyldsbwnydednzwnefydthtddbojicemlucdygicczhoadrzcylwadsxpilpiecskomoltejtkmqqymehpmmjxyolwpeewjckznpccpsvsxauyodhalmriocwpelwbcniyfxmwjcemcyrazdqlsomdbfljwnbijxpddsyoehxpceswtoxwbleecsaxcnuetzywfn"

## Keyword alone does not work...
## Code may start with "start" therefore klkbn = start
## 10 + 18 % 26 = 18
## 11 + 10 % 26 = 19
## 10 + 20 % 26 = 0

ans_3 = vigenereCipher(text_3, key)
print(ans_3)

# Clue 3
text_4 = "44541134541123335344541242 43424432514121231131135315 54425442444243443251415343 54324234411125513553341342 43225343114454345343225134 31421432513412533412155415 34513351444411225144425442 44441534512355154321345111 13112123514254315333214243 51445315341434512542531544 335154325341443 (cut off) 43513544"