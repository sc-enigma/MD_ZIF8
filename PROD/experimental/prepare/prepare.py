# Read .itp file
lines = []
itp_lines = []
with open('ZIF8_MXL.gro', 'r') as gro_file:
    lines = [line for line in gro_file]
    for idx in range(2, len(lines) - 1):
        itp_lines.append(lines[idx])
data = []
for string in itp_lines:
    split = [string[0:5], string[5:12], string[12:15], string[15:23], string[23:31], string[31:39], string[39:]]
    for idx in range(len(split)):
        split[idx] = split[idx].replace(' ', '')
    data.append(split)

def remove(data, mol_idx):
    idx = 0   
    while idx  < len(data):
        if int(data[idx][0]) == mol_idx:
            del data[idx]
            idx -= 1
        if int(data[idx][0])  > mol_idx:
            data[idx][0] = str(int(data[idx][0]) - 1)
        idx += 1
    return data

def get_z_coords(data, mol_idx):
    z_coords = []
    for rec in data:
        if rec[1] == 'ZIF':
            continue
        if int(rec[0]) == mol_idx:
            z_coords.append(float(rec[-1]))
    return z_coords

min_lim = 3.5090000
max_lim = 6.8
mol_idx = 0
while True:
    z_coords = get_z_coords(data, mol_idx)
    if len(z_coords) != 0:
        if min(z_coords) < min_lim or max(z_coords) > max_lim:
            data = remove(data, mol_idx)
            continue
    mol_idx += 1
    if len(z_coords) == 0 and mol_idx > 1000:
        break

print(int(data[-1][0]) - 288)

# Write .itp file
for idx in range(len(data)):
    data[idx][3] = idx + 1
itp_lines_out = []
for split in data:
    itp_lines_out.append(f'{split[0]:>5}{split[1]:>3}{split[2]:>7}{split[3]:>5}{split[4]:>8}{split[5]:>8}{split[6]:>9}')
with open('ZIF8_MXL_fixed.gro', 'w') as gro_file_out:
    gro_file_out.write(lines[0])
    gro_file_out.write(f'{len(itp_lines_out):>5}\n')
    for string in itp_lines_out:
        gro_file_out.write(string)
    gro_file_out.write(lines[-1])