import math
import matplotlib.pyplot as plt

# Read atoms
atom_lines = []
with open('__atoms.txt', 'r') as af:
    atom_lines = [line for line in af]
atoms = [[float(line.split()[1]), float(line.split()[2]), float(line.split()[3])] for line in atom_lines]

# Read .itp file
itp_lines = []
with open('ZIF8_i.itp', 'r') as itpf:
    itp_lines = [line for line in itpf]

# Distibute text into sections
sections = []
sections.append(itp_lines[0:2222])      # 0
sections.append(itp_lines[2222:4718])   # 1 bonds
sections.append(itp_lines[4718:11063])  # 2
sections.append(itp_lines[11063:15671]) # 3 angles
sections.append(itp_lines[15671:15676]) # 4
sections.append(itp_lines[15676:22972]) # 5 dihedrals
sections.append(itp_lines[22972:22977]) # 6
sections.append(itp_lines[22977:])      # 7 dihedrals

def distancez(atom1, atom2):
    return math.sqrt((atom1[2] - atom2[2])**2)

# Correct bonds
line_idx = 0
while line_idx < len(sections[1]):
    bond_line = sections[1][line_idx]
    bond = [int(bond_line.split()[0]), int(bond_line.split()[1])]
    d12 = distancez(atoms[bond[0] - 1], atoms[bond[1] - 1])
    if d12 > 2.0:
        del sections[1][line_idx]
    else:
        line_idx += 1

# Correct angles
line_idx = 0
while line_idx < len(sections[3]):
    angle_line = sections[3][line_idx]
    angle = [int(angle_line.split()[0]), int(angle_line.split()[1]), int(angle_line.split()[2])]
    d01 = distancez(atoms[angle[0] - 1], atoms[angle[1] - 1])
    d12 = distancez(atoms[angle[1] - 1], atoms[angle[2] - 1])
    if d01 > 2.0 or d12 > 2.0:
        del sections[3][line_idx]
    else:
        line_idx += 1

# Correct dihedrals
line_idx = 0
while line_idx < len(sections[5]):
    dihedral_line = sections[5][line_idx]
    dihedral = [int(dihedral_line.split()[0]), int(dihedral_line.split()[1]), int(dihedral_line.split()[2]), int(dihedral_line.split()[3])]
    d01 = distancez(atoms[dihedral[0] - 1], atoms[dihedral[1] - 1])
    d12 = distancez(atoms[dihedral[1] - 1], atoms[dihedral[2] - 1])
    d23 = distancez(atoms[dihedral[2] - 1], atoms[dihedral[3] - 1])
    if d01 > 2.0 or d12 > 2.0 or d23 > 2.0:
        del sections[5][line_idx]
    else:
        line_idx += 1

# Correct dihedrals
line_idx = 0
while line_idx < len(sections[7]):
    dihedral_line = sections[7][line_idx]
    dihedral = [int(dihedral_line.split()[0]), int(dihedral_line.split()[1]), int(dihedral_line.split()[2]), int(dihedral_line.split()[3])]
    d01 = distancez(atoms[dihedral[0] - 1], atoms[dihedral[1] - 1])
    d12 = distancez(atoms[dihedral[1] - 1], atoms[dihedral[2] - 1])
    d23 = distancez(atoms[dihedral[2] - 1], atoms[dihedral[3] - 1])
    if d01 > 2.0 or d12 > 2.0 or d23 > 2.0:
        del sections[7][line_idx]
    else:
        line_idx += 1

# Write .itp file
with open('ZIF8.itp', 'w') as oitpf:
    for section in sections:
        for line in section:
            oitpf.write(line)

# Visualize
line_idx = 0
while line_idx < len(sections[1]):
    bond_line = sections[1][line_idx]
    bond = [int(bond_line.split()[0]), int(bond_line.split()[1])]
    a1 = atoms[bond[0] - 1]
    a2 = atoms[bond[1] - 1]
    plt.plot([a1[0], a2[0]], [a1[2], a2[2]])
    line_idx += 1
plt.show()


