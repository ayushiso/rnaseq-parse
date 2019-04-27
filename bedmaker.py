# converts fasta with coordinates (from sORF finder) to BED file

import sys

in_fasta = sys.argv[1]
out_bed = sys.argv[2]

try:
    with open(in_fasta, 'r') as in_fq, open(out_bed, 'w') as out_bd:
        for header in in_fq:
            sequence = next(in_fq).rstrip()
            feats = header.split(":")

            chr, coords = feats[0], feats[1].split("#")
            out_bd.write("{}\t".format(chr[1:]))

            st_on_chr = coords[0].split("-")

            # check strand polarity
            if coords[2] == "+":
                start = int(st_on_chr[0]) + int(coords[1])
                stop = start + len(sequence)

            elif coords[2] == "-":
                stop = int(st_on_chr[0]) + int(coords[1])
                start = stop - len(sequence)

            else:
                print("Incorrect strand polarity feature detected")
                break

            # write start and stop features
            out_bd.write("{}\t".format(start))
            out_bd.write("{}\t".format(stop))
            out_bd.write("{}\n".format(coords[2]))

except StopIteration:
    print("End") # shouldn't happen if the fasta file is in proper format
