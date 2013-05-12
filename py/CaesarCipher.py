#!/usr/bin/env python2

import sys
import os
import CORBA
import Caesar
import Caesar__POA

alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


class CaesarCipher (Caesar__POA.CaesarCipher):
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

    def decrypt(self, text):
        encrypted = list(text)
        decrypted = "Decrypted text: "
        for i in range(len(encrypted)):
            for j in range(len(alph)):
                # print i, j
                if encrypted[i] == alph[j]:
                    if j < len(alph)-3:
                        todec = alph[j-3]
                    elif j == 2:
                        todec = alph[len(alph)-3]
                    elif j == 1:
                        todec = alph[len(alph)-2]
                    elif j == 0:
                        todec = alph[len(alph)]
                    else:
                        print "DEBUG: nichts true"
                    decrypted += todec
            if encrypted[i] == " ":
                decrypted += " "
        return decrypted

x = CaesarCipher()
print x.encrypt("ABCXYZabcxyz")
print x.decrypt("DEFabcdefABC")
print x.encrypt("Hallo das ist ein Test.")
print x.decrypt("Kdoor gdv lvw hlq Whvw")

orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = CaesarCipher()
poa.activate_object(servant)

print orb.object_to_string(servant._this())

poa._get_the_POAManager().activate()
orb.run()
