"""
What are the length of the longest and shortest sequence in the file?
"""

string = open("dna2.fasta").readlines()

#print(string)

sequences = []
seq = ""

for s in string:
#	print(type(s))
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

lengths = [len(i) for i in sequences]

print(max(lengths), min(lengths))