"""
What is the starting position of the longest ORF in reading frame 3 in any of the sequnces?
"""

string = open("dna2.fasta").readlines()

sequences = []
seq = ""

for s in  string:
    if not s.startswith('>'):
        s = s.replace(" ", "")
        s = s.replace("\n", "")
        seq = seq + s
    else:
        sequences.append(seq)
        seq = ""

# add the last seq
sequences.append(seq)

sequences = sequences[1:]

# Find the ORF 3
def find_orf_3(sequence):
    # find all ATG indexs
    start_position = 2
    start_indexs = []
    stop_indexs = []

    for i in range(2, len(sequence), 3):
        if sequence[i:i+3] == "ATG":
            start_indexs.append(i)

    # find all stop indexs
    for i in range(2, len(sequence), 3):
        stops = ["TAA", "TAG", "TGA"]
        if sequence[i:i+3] in stops:
            stop_indexs.append(i)

    orf = []
    mark = 0
    start_position = {}

    for i in range(0, len(start_indexs)):
        for j in range(0, len(stop_indexs)):
            if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
                orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
                start_position[len(sequence[start_indexs[i]:stop_indexs[j]+3])] = start_indexs[i]
                mark = stop_indexs[j] + 3
                break

    return start_position

n = 1
lengths = []
for i in sequences:
    print("["+str(n)+"]")
    orfs = find_orf_3(i)
    print(orfs)
    n += 1
