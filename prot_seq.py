import urllib.request
from Bio import PDB

# Create a PDB parser
parser = PDB.PDBParser()

# Specify the PDB ID of the protein of interest
pdb_id = '4HHB'

# Download the PDB file using urllib
url = f'https://files.rcsb.org/download/{pdb_id}.pdb'
filename = f'{pdb_id}.pdb'
urllib.request.urlretrieve(url, filename)


# Parse the downloaded PDB file
structure = parser.get_structure(pdb_id, filename)

# Extract the protein sequence
ppb = PDB.PPBuilder()
sequences = []
for pp in ppb.build_peptides(structure):
    sequence = pp.get_sequence()
    sequences.append(sequence)

# Print the sequences
for sequence in sequences:
    print(sequence)
