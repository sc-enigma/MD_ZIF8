gro_lines = []
with open("ZIF8_i.gro", 'r') as gro_file:
    gro_lines = [line for line in gro_file]
gro_sections = { 'atoms': [] }
for idx, line in enumerate(gro_lines):
    if len(line) <= 1 or ';' in line:
        continue
    gro_sections['atoms'].append(line.split())

itp_lines = []
with open("ZIF8_i.itp", 'r') as itp_file:
    itp_lines = [line for line in itp_file]
itp_sections = {}
current_section = ''
for idx, line in enumerate(itp_lines):
    if len(line) <= 1 or ';' in line:
        continue
    line = line.replace('\n', '')
    if '[' in line:
        current_section = line
        itp_sections[current_section] = []
    else:
        itp_sections[current_section].append(line)

def format_from_gro_line(line):
    arr = [line[0:5], line[5:8], line[8:15], line[15:20], line[20:28]]
    print(arr)
    arr[0] = int(arr[0])
    arr[2] = int(arr[2])
    arr[4] = int(arr[4])
    arr[5] = int(arr[5])
    arr[6] = int(arr[6])
    
def format_to_gro_line(arr):
    return f"{arr[0]:>5}{arr[1]:>3}{arr[2]:>7}{arr[3]:>5}{arr[4]:8.3f}{arr[5]:8.3f}{arr[6]:8.3f}"

print(format_from_gro_line('    1ZIF     C1    1   0.858   0.207   0.426'))









