import math

# Read atoms
atom_lines = []
with open('ZIF8_i.gro', 'r') as af:
    atom_lines = [line for line in af]
atoms = [[float(line.split()[3]), float(line.split()[4]), float(line.split()[5])] for line in atom_lines]

shift = 0.0
for atom in atoms:
    shift = max(shift, -1.0 * atom[2])
shift += 0.2

# Write atoms
with open('ZIF8_o.gro', 'w') as oaf:
    line_idx = 0
    for line_idx in range(len(atom_lines)):
        line = atom_lines[line_idx]
        oaf.write(f'{line[0:38]} ' + f'{(atoms[line_idx][2] + shift):.3f}' + '\n')