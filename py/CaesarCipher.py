#!/usr/bin/env python2

import CORBA

alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


class CaesarCipher:
    def encrypt(self, text):
        plain = list(text)
        encrypted = "Encryped text: "
        for i in range(len(plain)):
            for j in range(len(alph)):
                # print i, j
                if plain[i] == alph[j]:
                    if j < len(alph)-3:
                        toenc = alph[j+3]
                    elif j == len(alph)-3:
                        toenc = alph[0]
                    elif j == len(alph)-2:
                        toenc = alph[1]
                    elif j == len(alph)-1:
                        toenc = alph[2]
                    else:
                        print "DEBUG: nichts true"
                    encrypted += toenc
            if plain[i] == " ":
                encrypted += " "
        return encrypted

x = CaesarCipher()
# print x.encrypt("ABCXYZabcxyz")
print x.encrypt("Hallo das ist ein Test.")
# orb = CORBA.ORB_init(sys.argv)
