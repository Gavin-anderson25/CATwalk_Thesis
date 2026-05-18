import tkinter as tk
from tkinter import ttk
from Bio import SeqIO
import random
import lib.seeder as sd
import lib.CATwalk as ct
import lib.validator as vd

def getseedbutton():
    fasta = genfastaentry.get()
    length = int(seedsize_entry.get())
    generator_output.delete("1.0", "end")
    generator_output.insert("end", sd.randomseq(fasta, length))

def performcatwalk():
    library = libraryentry.get()
    seedsequence = seed_entry.get()
    productlength = int(length_entry.get())
    barb_size = int(barb_entry.get())
    errorvariable = float(error_entry.get())
    cutoffvariable = float(cutoff_entry.get())
    catwalk_output.delete("1.0", "end")
    catwalk_output.insert("end", ct.CATwalk(center_sequence=seedsequence, fasta=library, product_length=productlength, barbsize=barb_size, error_variable=errorvariable, cutoff_variable=cutoffvariable))

def performvalidation():
    file = validatorfastaentry.get()
    subject = validatorinput.get("1.0", "end-1c")
    validoutputlabel.config(text=f"Percent Similarity between Extended Product and Reference: {vd.validatesequence(file, subject):.5f}")
    #validoutput_entry.delete("1.0", "end")
    #validoutput_entry.insert("end", vd.validatesequence(file, subject))

root = tk.Tk()
root.geometry("1300x600")
root.title("CATwalk")

catwalk_label = ttk.Label(root, text="CATwalk", font=("TkMenuFont", 15))
catwalk_label.pack(side=tk.TOP, padx=5, pady=0)

generator_zone = ttk.Frame(root)
generator_zone.pack(side=tk.LEFT, fill="both", padx=10, pady=10)

generator_label = ttk.Label(generator_zone, text="Seed Generator", font=("TkMenuFont", 12))
generator_label.pack(side=tk.TOP, padx=5, pady=15)

genfastalabel = ttk.Label(generator_zone, text="Genome File Name (.fasta):")
genfastalabel.pack(side=tk.TOP, padx=5, pady=0)
genfastaentry = ttk.Entry(generator_zone, width=30)
genfastaentry.pack(side=tk.TOP, padx=5, pady=5)
genfastaentry.insert("end", "s.enterica_ref.fna")

generator_zone_param = ttk.Frame(generator_zone)
generator_zone_param.pack(side=tk.TOP, padx=0, pady=0)
seedsizelabel = ttk.Label(generator_zone_param, text="Seed Length (nt):")
seedsizelabel.pack(side=tk.LEFT, padx=5, pady=5)
seedsize_entry = ttk.Entry(generator_zone_param, width=10)
seedsize_entry.pack(side=tk.LEFT, padx=0, pady=5)
seedsize_entry.insert("end", "250")

sequence_generator = ttk.Button(generator_zone, text="Generate Random Sequence", command=getseedbutton)
sequence_generator.pack(side=tk.TOP, padx=5, pady=5)

generator_output = tk.Text(generator_zone, width=50, height=10)
generator_output.pack()

divider1 = ttk.Separator(root, orient="vertical")
divider1.pack(side= tk.LEFT, fill="y", padx=5, pady=5)

catwalk_zone = ttk.Frame(root)
catwalk_zone.pack(side=tk.LEFT, fill="both", padx=10, pady=10)

catwalk_sublabel = ttk.Label(catwalk_zone, text="Seed Extender", font=("TkMenuFont", 12))
catwalk_sublabel.pack(side=tk.TOP, padx=5, pady=15)

librarylabel = ttk.Label(catwalk_zone, text="Library Name (.fasta):")
librarylabel.pack(side=tk.TOP, padx=5, pady=0)
libraryentry = ttk.Entry(catwalk_zone, width=30)
libraryentry.pack(side=tk.TOP, padx=5, pady=5)
libraryentry.insert("end", "SRR38513909.fasta")

seedlabel = ttk.Label(catwalk_zone, text="Seed Sequence:")
seedlabel.pack(side=tk.TOP, padx=5, pady=0)
seed_entry = ttk.Entry(catwalk_zone, width=30)
seed_entry.pack(side=tk.TOP, padx=5, pady=5)

param_zone1 = ttk.Frame(catwalk_zone)
param_zone1.pack(side=tk.TOP, fill="both", padx=0, pady=0)

param_zone2 = ttk.Frame(catwalk_zone)
param_zone2.pack(side=tk.TOP, fill="both", padx=0, pady=0)

lengthlabel = ttk.Label(param_zone1, text="Product Size (nt):")
lengthlabel.pack(side=tk.LEFT, padx=5, pady=5)
length_entry = ttk.Entry(param_zone1, width=10)
length_entry.pack(side=tk.LEFT, padx=0, pady=5)
length_entry.insert("end", "2000")

barblabel = ttk.Label(param_zone1, text="Barb Length (nt):")
barblabel.pack(side=tk.LEFT, padx=5, pady=5)
barb_entry = ttk.Entry(param_zone1, width=10)
barb_entry.pack(side=tk.LEFT, padx=0, pady=5)
barb_entry.insert("end", "15")

errorlabel = ttk.Label(param_zone2, text="Error Rate (%): ")
errorlabel.pack(side=tk.LEFT, padx=5, pady=5)
error_entry = ttk.Entry(param_zone2, width=10)
error_entry.pack(side=tk.LEFT, padx=0, pady=5)
error_entry.insert("end", "0.001")

cutofflabel = ttk.Label(param_zone2, text="Error Cutoff:")
cutofflabel.pack(side=tk.LEFT, padx=5, pady=5)
cutoff_entry = ttk.Entry(param_zone2, width=10)
cutoff_entry.pack(side=tk.LEFT, padx=0, pady=5)
cutoff_entry.insert("end", "1.05")

extendbutton = ttk.Button(catwalk_zone, text="Extend Seed", command=performcatwalk)
extendbutton.pack(padx=5, pady=5)

catwalk_output = tk.Text(catwalk_zone, width=50, height=10)
catwalk_output.pack()

divider2 = ttk.Separator(root, orient="vertical")
divider2.pack(side= tk.LEFT, fill="y", padx=5, pady=5)

validator_zone = ttk.Frame(root)
validator_zone.pack(side=tk.LEFT, fill="both", padx=10, pady=10)

validator_sublabel = ttk.Label(validator_zone, text="Product Validator", font=("TkMenuFont", 12))
validator_sublabel.pack(side=tk.TOP, padx=5, pady=15)

validatorfastalabel = ttk.Label(validator_zone, text="Reference File Name (.fasta):")
validatorfastalabel.pack(side=tk.TOP, padx=5, pady=0)
validatorfastaentry = ttk.Entry(validator_zone, width=30)
validatorfastaentry.pack(side=tk.TOP, padx=5, pady=5)
validatorfastaentry.insert("end", "s.enterica_ref.fna")

validatorinputlabel = ttk.Label(validator_zone, text="Extended Product:")
validatorinputlabel.pack(side=tk.TOP, padx=5, pady=0)
validatorinput = tk.Text(validator_zone, width=50, height=10)
validatorinput.pack(side=tk.TOP, padx=5, pady=0)

validatebutton = ttk.Button(validator_zone, text="Validate Extended Product", command=performvalidation)
validatebutton.pack(side=tk.TOP, padx=5, pady=5)

param_zone3 = ttk.Frame(validator_zone)
param_zone3.pack(side=tk.TOP, fill="both", padx=0, pady=0)
validoutputlabel = ttk.Label(validator_zone, text="Percent Similarity between Extended Product and Reference (%): ###")
validoutputlabel.pack(side=tk.TOP, padx=5, pady=5)
#validoutput_entry = ttk.Entry(validator_zone, width=10)
#validoutput_entry.pack(side=tk.TOP, padx=0, pady=5)

root.mainloop()
