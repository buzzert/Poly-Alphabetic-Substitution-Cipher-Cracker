import sys
import math
import re
import collections

class PolyCipherCracker:
	global alphabet
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	def __init__(self, ciphertext):
		self.ciphertext = ciphertext

	def _alphabet_at_letter(self, letter):
		index = ord(letter) - 65
		alpha_deque = collections.deque(alphabet)
		alpha_deque.rotate(index)

		return alpha_deque

	def _letter_for_keychar(self, keychar, inputc):
		alpha_deque = self._alphabet_at_letter(keychar)
		return alpha_deque[ord(inputc) - 65]

	def decipher(self, key):
		plaintext = ""

		keypos = 0
		for i in range(0, len(self.ciphertext)):
			keychar = key[keypos % len(key)]
			inputc = self.ciphertext[i]
			plaintext += self._letter_for_keychar(keychar, inputc)
			keypos += 1

		return plaintext

	def bruteforce(self, keylen=3):
		crib = "THERE"

		for i in range(0, pow(len(alphabet), keylen)):
			key = ""
			for c in range(0, keylen):
				upperbound = pow(len(alphabet), c)
				key += chr(((i / upperbound) % len(alphabet)) + 65)

			decipher = self.decipher(key)
			match = re.search(crib, decipher)
			if (match != None):
				print "*** FOUND: ", decipher



if __name__ == "__main__":
	ciphertext = raw_input("Paste ciphertext: \n")

	poly = PolyCipherCracker(ciphertext)
	print poly.bruteforce(3)
