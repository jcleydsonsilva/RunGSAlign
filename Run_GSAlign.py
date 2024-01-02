import os
import sys
import subprocess
from Bio import SeqIO
from collections import defaultdict


def Renome_seq(key,aux):
    aux.pop(key, None)
    return aux
    
##############################################################################
fasta = {}
with open(sys.argv[1], "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        fasta[record.id] = record.seq
##############################################################################
fastah = {}
with open(sys.argv[2], "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        fastah[record.id] = record.seq
###############################################################################

for key in sorted(fasta):
    print ('*************************** --- *************************** --- *************************** --- ***************************')
    print ('Query: '+ key+'\n') 
    seq = fasta[key]
    aux_fasta = Renome_seq(key,fastah)

    db = open('ref.fa','w') 
    for acc in aux_fasta:
        db.write('>' + acc + '\n')
        db.write(str(aux_fasta[acc]) + '\n')
    db.close()
    
    query = open('query.fa','w')
    query.write('>'+key+'\n')
    query.write(str(seq) + '\n')
    query.close()


    cmd = 'GSAlign -t 110 -r ref.fa -q query.fa -o '+ key +' -dp\n'
    cmd += 'rm *.vcf *.maf *.gp'
    process = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()

    #########################################################################