# removes transcript_id tag from gene features (fixing "no start/stop codon" error)

import sys

in_gtf = sys.argv[1]
out_gtf = sys.argv[2]

with open(in_gtf, 'r') as ingtf:
    with open(out_gtf, 'w') as outgtf:
        for line in ingtf:
            elems = line.split('\t')
            if elems[2] != "gene":
                outgtf.write(line)
            else:
                tags = elems.pop()
                gene_id = tags.split('; ')[0]
                elems.append(gene_id)
                new_line = '\t'.join(elems) + ";\n"
                outgtf.write(new_line)
