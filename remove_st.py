#removes start and stop codon features in GTF, only returns CDS features.

import sys

infile = sys.argv[1]
outfile = sys.argv[2]


with open(infile, 'r') as in_file:
    with open(outfile, 'w') as out_file:
        for line in in_file:
            attrs = line.split('\t')
            if attrs[2] == "CDS":
                out_file.write(line)
