#!/usr/local/bin/python
import csv
import json
import os

jsondir = '../../app/data/planets'
csvfile = open('data.csv', 'rb')

fieldnames = [
    "dec",
    "hd_name",
    "hip_name",
    "pl_astflag",
    "pl_cbflag",
    "pl_dens",
    "pl_disc",
    "pl_discmethod",
    "pl_eqt",
    "pl_facility",
    "pl_hostname",
    "pl_imgflag",
    "pl_masse",
    "pl_massj",
    "pl_name",
    "pl_omflag",
    "pl_orbeccen",
    "pl_orbper",
    "pl_pnum",
    "pl_rade",
    "pl_radj",
    "pl_ratdor",
    "pl_rvflag",
    "pl_telescope",
    "pl_tranflag",
    "ra",
    "rowupdate",
    "st_age",
    "st_dist",
    "st_mass",
    "st_optmag",
    "st_rad",
    "st_teff",
    "pl_pelink",
    "pl_edelink"
]
reader = csv.DictReader(csvfile, fieldnames)

keys_to_delete = []

for row in reader:
    if reader.line_num == 1:
        continue
    jsonfile = open(jsondir + '/' + row['pl_name'].replace(' ', '') + '.json', 'w+')
    output = json.dumps(row, separators=(',',':'))
    
    all_data = json.loads(output)
    
    for key in row:
        if not row[key]:
            keys_to_delete.append(key)
    for i in keys_to_delete:
        all_data.pop(i, None)

    keys_to_delete = []

    out = json.dumps(all_data, separators=(',',':'))

    jsonfile.write(out)