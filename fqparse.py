# fixes mixed @ features in fastq files

import sys

infile = sys.argv[1]
outfile = sys.argv[2]
trfile = sys.argv[3]

with open(infile, 'r') as infq:
    with open(outfile, 'w') as outfq:
        with open(trfile, 'w') as trf:
            i = 1
            for line in infq:
                if i % 4 == 1 and line[0] != "@":
                    trf.write("i" + "@mis " + line)
                    outfq.write("@" + line)
                elif i % 4 == 3 and line[0] != "+":
                    trf.write("i"+ " +mis " + line)
                    outfq.write("+" + line)
                else:
                    outfq.write(line)
                i += 1
