# generates gene and transcript features using bruno file for CDS features present in GTF
# which are also there in bruno file

import sys
import csv

in_gtf = sys.argv[1]
in_bruno = sys.argv[2]
out_gtf = sys.argv[3]

gtf_dict = {}
bruno_dict = {}

with open(in_gtf, 'r') as ingtf:
    for line in ingtf:
        line_list = line.split('\t')
        features = line_list[-1].split(';')
        orfid = features[0].split(' ')[1][1:-1]
        gtf_dict[orfid] = line

with open(in_bruno, 'r') as inbruno:
    creader = csv.reader(inbruno, delimiter=',')
    attr = next(creader)
    for row in creader:
        bruno_dict[row[0]] = [row[5], row[6]]

with open(out_gtf, 'w') as outgtf:
    for orfid in gtf_dict:
        if orfid in bruno_dict:
            gene_elems = gtf_dict[orfid].split('\t')
            coords = bruno_dict[orfid]
            tab = '\t'
            outgtf.write(tab.join(gene_elems[:2]) + "\tgene\t" + tab.join(coords) + tab + tab.join(gene_elems[5:]))
            outgtf.write(tab.join(gene_elems[:2]) + "\ttranscript\t" + tab.join(coords) + tab + tab.join(gene_elems[5:]))
        outgtf.write(gtf_dict[orfid])
