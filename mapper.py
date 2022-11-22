#!/usr/bin/env python3
import sys

DATE_COL = 0
ZIP_CODE_COL = 2
ON_STREET_COL = 6
CROSS_STREET_COL = 7
OFF_STREET_COL = 8
PEDE_INJ_COL = 11
PEDE_KILL_COL = 12
CYC_INJ_COL = 13
CYC_KILL_COL = 14
MOT_INJ_COL = 15
MOT_KILL_COL = 16


for line in sys.stdin:
    values = line.split(',')

    date = values[DATE_COL]
    if '/' not in date:
        continue
    zip_code = values[ZIP_CODE_COL]
    if zip_code == "": 
        continue

    street_on = values[ON_STREET_COL]
    street_cross = values[CROSS_STREET_COL]
    street_off = values[OFF_STREET_COL]

    pedestrians_injured = values[PEDE_INJ_COL]
    pedestrians_killed = values[PEDE_KILL_COL]

    cyclists_injured = values[CYC_INJ_COL]
    cyclists_killed = values[CYC_KILL_COL]

    motorists_injured = values[MOT_INJ_COL]
    motorists_killed = values[MOT_KILL_COL]
    year = int(date.split('/')[2])
    if year <= 2012: 
        continue

    if street_on != '':
        print(f"{street_on}\t{zip_code}\tpedestrians\tinjured\t{pedestrians_injured}")
        print(f"{street_on}\t{zip_code}\tpedestrians\tkilled\t{pedestrians_killed}")
        print(f"{street_on}\t{zip_code}\tcyclists\tinjured\t{cyclists_injured}")
        print(f"{street_on}\t{zip_code}\tcyclists\tkilled\t{cyclists_killed}")
        print(f"{street_on}\t{zip_code}\tmotorists\tinjured\t{motorists_injured}")
        print(f"{street_on}\t{zip_code}\tmotorists\tkilled\t{motorists_killed}")
    if street_cross != '':
        print(f"{street_cross}\t{zip_code}\tpedestrians\tinjured\t{pedestrians_injured}")
        print(f"{street_cross}\t{zip_code}\tpedestrians\tkilled\t{pedestrians_killed}")
        print(f"{street_cross}\t{zip_code}\tcyclists\tinjured\t{cyclists_injured}")
        print(f"{street_cross}\t{zip_code}\tcyclists\tkilled\t{cyclists_killed}")
        print(f"{street_cross}\t{zip_code}\tmotorists\tinjured\t{motorists_injured}")
        print(f"{street_cross}\t{zip_code}\tmotorists\tkilled\t{motorists_killed}")
    if street_off != '':
        print(f"{street_off}\t{zip_code}\tpedestrians\tinjured\t{pedestrians_injured}")
        print(f"{street_off}\t{zip_code}\tpedestrians\tkilled\t{pedestrians_killed}")
        print(f"{street_off}\t{zip_code}\tcyclists\tinjured\t{cyclists_injured}")
        print(f"{street_off}\t{zip_code}\tcyclists\tkilled\t{cyclists_killed}")
        print(f"{street_off}\t{zip_code}\tmotorists\tinjured\t{motorists_injured}")
        print(f"{street_off}\t{zip_code}\tmotorists\tkilled\t{motorists_killed}")
