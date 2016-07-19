"""
Find all repeats of length 12 in the input file. Use Max to specify the number of copies of the most frequent repeat.
How many different 12-base sequences occur Max times?
"""
from collections import Counter

string = open("dna2.fasta").readlines()

sequences = []
seq = ""

for s in string:
    if not s.startswith('>'):
        s = s.replace(" ", "")
        s = s.replace("\n", "")
        seq = seq + s
    else:
        sequences.append(seq)
        seq = ""

# Add the last seq
sequences.append(seq)

sequences = sequences[1:]

def get_all_repeats(sequence):
    repeats = []
    for i in range(len(sequence)):
        repeats.append(sequence[i:i+12])
    return repeats

all_twelve_repeats = []

for s in sequences:
    repeats_list = get_all_repeats(s)
    for r in repeats_list:
        if len(r) == 12:
            all_twelve_repeats.append(r)

print(Counter(all_twelve_repeats))
