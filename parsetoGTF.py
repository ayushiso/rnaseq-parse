import csv
import sys

infile = sys.argv[1]
outfile = sys.argv[2]

data = []

with open(infile, 'r') as incsv:
    creader = csv.reader(incsv, delimiter=',')
    attr = next(creader)
    for row in creader:
        data.append(row)

with open(outfile, 'w') as out_gtf:
    for attr_list in data:

        #writing first three columns
        out_gtf.write("{}_C_albicans_SC5314\tBRN\tCDS\t".format(attr_list[1]))

        #writing ORF start and end , dots and strand value in between
        out_gtf.write("{}\t{}\t.\t{}\t.\t".format(attr_list[3], attr_list[4], attr_list[2]))

        #writing gene_id and transcript_id (basically same as exon name)
        out_gtf.write("gene_id \"{}\"; transcript_id \"{}-T\";".format(attr_list[0], attr_list[0]))

        out_gtf.write("\n")
