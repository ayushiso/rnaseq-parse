# adds start and stop codon features to gtf file inferred from the CDS coordinates.

#NOTE: try doing it from original once.

import sys
import copy

gtf_wo_fts = sys.argv[1]
gtf_out = sys.argv[2]

# infer using CDS features in file
with open(gtf_wo_fts, 'r') as ingtf:
    with open(gtf_out, 'w') as outgtf:
        for line in ingtf:
            elems = line.split('\t')
            if elems[2] != "CDS":
                outgtf.write(line)
            else:
                start_elems = copy.deepcopy(elems)
                stop_elems = copy.deepcopy(elems)

                if elems[6] == "+":
                    #print start codon feature
                    start_elems[2] = "start_codon"
                    start_elems[4] = str(int(elems[3])+2)

                    start_line = '\t'.join(start_elems)
                    outgtf.write(start_line)

                    #print the CDS feature
                    outgtf.write(line)

                    #print stop codon feature
                    stop_elems[2] = "stop_codon"
                    stop_elems[3] = str(int(elems[4])+1)
                    stop_elems[4] = str(int(elems[4])+3)

                    stop_line = '\t'.join(stop_elems)
                    outgtf.write(stop_line)

                elif elems[6] == "-":
                    #print stop codon feature
                    stop_elems[2] = "stop_codon"
                    stop_elems[3] = str(int(elems[3])-3)
                    stop_elems[4] = str(int(elems[3])-1)

                    stop_line = '\t'.join(stop_elems)
                    outgtf.write(stop_line)

                    #print the CDS feature
                    outgtf.write(line)

                    #print start codon feature
                    start_elems[2] = "start_codon"
                    start_elems[3] = str(int(elems[4])-2)

                    start_line = '\t'.join(start_elems)
                    outgtf.write(start_line)
                else:
                    print("impossible!")



# add from existing file?
