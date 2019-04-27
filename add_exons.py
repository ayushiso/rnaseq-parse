# adds exon features inferred from CDS features (same coordinates)

import sys

in_gtf = sys.argv[1]
out_gtf = sys.argv[2]

with open(in_gtf, 'r') as ingtf:
    with open(out_gtf, 'w') as outgtf:
        for line in ingtf:
            elems = line.split('\t')
            if elems[2] != "CDS":
                outgtf.write(line)
            else:
                elems[2] = "exon"
                ex_line = '\t'.join(elems)
                outgtf.write(ex_line)
                outgtf.write(line)
