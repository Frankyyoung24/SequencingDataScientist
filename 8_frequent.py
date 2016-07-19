"""
Find the most frequently occurring repeat of length 6/7 in all sequences, How many times does it occur in all?
"""

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

#Add the last seq
sequences.append(seq)

sequences = sequences[1:]

def get_all_repeats(sequence):
    repeats = []
    for i in range(len(sequence)):
        repeats.append(sequence[i:i+6])
    return repeats

all_six_repeats = []

for i in sequences:
    repeats_list = get_all_repeats(i)
    for j in repeats_list:
        all_six_repeats.append(j)

def most_common(lst):
    return max(set(lst), key = lst.count)

print(most_common(all_six_repeats))
print(all_six_repeats.count(most_common(all_six_repeats)))
