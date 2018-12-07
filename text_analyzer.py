import os
import sys
import csv

file = sys.argv[1]
output_file = sys.argv[2]

try:
    f = open(file, "r").read()
except FileNotFoundError:
    print("Wrong file name or file doesn't exist")
    
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

for word in final_word_list:
    word_frequency[word] = 0

for word in final_word_list:
    word_frequency[word] += 1

output_file_extension = output_file.split('.')[1]

if output_file_extension == 'txt': 
    for word in word_frequency:
        w = open(output_file, "a+")
        if word_frequency[word] == 1:    
            w.write("The word \"" + word + "\" was mentioned " + str(word_frequency[word]) + " time.\n\n")
        else:
            w.write("The word \"" + word + "\" was mentioned " + str(word_frequency[word]) + " times.\n\n")
        
    print(str(output_file) + " created")

elif output_file_extension == 'csv':
    csvFile = open(output_file, 'w')
    with csvFile:
        header = ['Word', 'Frequency']
        writer = csv.DictWriter(csvFile, fieldnames=header)
        writer.writeheader()
        
        for word in word_frequency:
            writer.writerow({'Word' : word, 'Frequency' : word_frequency[word]})
        print(str(output_file) + " created")

else:
    print("Unsupported file format was requested")