from Bio import SeqIO
import os
import random
import time

def spoolgen(obj):
    for i in obj:
        yield i

def jumblelib(file, outputfile):
    start = time.perf_counter()
    count = int(0)
    print("Starting Jumble")
    with open(file) as f:
        for line in f:
            if line.startswith(">"):
                count += 1
    gen = list(SeqIO.parse(file, "fasta"))
    with open(outputfile, "w") as f:
        manifest = list(range(count))
        random.shuffle(manifest)
        for i in manifest:
            entry = gen[int(i)]
            entry = entry.format("fasta")
            f.write(entry)
    end = time.perf_counter()
    elapsed = end - start
    print(f"Jumbling Complete - Elapsed time:{elapsed:.6f}")
#    os.replace("temp.txt", file)
            
jumblelib("SRR36025408.fasta", "SRR36025408.fasta")
            
