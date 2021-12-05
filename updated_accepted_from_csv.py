# must be run as sudo
import sys
import csv

conf_file = "/etc/bandersnatch.conf"
accept_list_file = "./accept_list.csv"
accept_list = []

with open(accept_list_file, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        accept_list.append('    '+row[0])


# get line number
line_no = None
with open(conf_file, 'r') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

    for index, l in enumerate(lines):
        if l == '[allowlist]':
            line_no = index+2
            break

if line_no is None:
    print("Could not find [allowlist] in file")
    sys.exit(1)




new_lines = lines[:line_no] + accept_list

with open(conf_file, 'w') as f:
    f.write('\n'.join(new_lines))




