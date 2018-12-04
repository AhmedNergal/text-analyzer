import os
import sys

file = sys.argv[1]
output_file = sys.argv[2]

f = open(file, "r").read()
w = open(output_file, "a+")
print(f)

f = f.lower()

final_word_list = []
word_frequency = {}

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \n"

modified_text = ""

for c in f:
    if c in alphabet:
        modified_text += c

lines = modified_text.splitlines()

for word in lines:
    temp_word_list = word.split(' ')
    for single_word in temp_word_list:
        if single_word != "":
            final_word_list.append(single_word)

print(final_word_list)

for word in final_word_list:
    word_frequency[word] = 0

for word in final_word_list:
    word_frequency[word] += 1

print(word_frequency)

for word in word_frequency:
    w.write("The word \"" + word + "\" was mentioned " + str(word_frequency[word]) + " times.\n\n")
