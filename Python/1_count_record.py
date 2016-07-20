“”“
How many records are in the multi-FASTA file?
”””

fasta_filr = open("dna2.fasta").read()
fasta_file = list(fasta_filr).count('>')
print(fasta_file)
