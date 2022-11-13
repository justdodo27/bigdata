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
    street_cross = values[ON_STREET_COL]
    street_off = values[ON_STREET_COL]

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
        if pedestrians_injured != '0':
            print(f"{street_on}:{zip_code}:pedestrians:injured\t{pedestrians_injured}")
        if pedestrians_killed != '0':
            print(f"{street_on}:{zip_code}:pedestrians:killed\t{pedestrians_killed}")
        if cyclists_injured != '0':
            print(f"{street_on}:{zip_code}:cyclists:injured\t{cyclists_injured}")
        if cyclists_killed != '0':
            print(f"{street_on}:{zip_code}:cyclists:killed\t{cyclists_killed}")
        if motorists_injured != '0':
            print(f"{street_on}:{zip_code}:motorists:injured\t{motorists_injured}")
        if motorists_killed != '0':
            print(f"{street_on}:{zip_code}:motorists:killed\t{motorists_killed}")
    if street_cross != '':
        if pedestrians_injured != '0':
            print(f"{street_cross}:{zip_code}:pedestrians:injured\t{pedestrians_injured}")
        if pedestrians_killed != '0':
            print(f"{street_cross}:{zip_code}:pedestrians:killed\t{pedestrians_killed}")
        if cyclists_injured != '0':
            print(f"{street_cross}:{zip_code}:cyclists:injured\t{cyclists_injured}")
        if cyclists_killed != '0':
            print(f"{street_cross}:{zip_code}:cyclists:killed\t{cyclists_killed}")
        if motorists_injured != '0':
            print(f"{street_cross}:{zip_code}:motorists:injured\t{motorists_injured}")
        if motorists_killed != '0':
            print(f"{street_cross}:{zip_code}:motorists:killed\t{motorists_killed}")
    if street_off != '':
        if pedestrians_injured != '0':
            print(f"{street_off}:{zip_code}:pedestrians:injured\t{pedestrians_injured}")
        if pedestrians_killed != '0':
            print(f"{street_off}:{zip_code}:pedestrians:killed\t{pedestrians_killed}")
        if cyclists_injured != '0':
            print(f"{street_off}:{zip_code}:cyclists:injured\t{cyclists_injured}")
        if cyclists_killed != '0':
            print(f"{street_off}:{zip_code}:cyclists:killed\t{cyclists_killed}")
        if motorists_injured != '0':
            print(f"{street_off}:{zip_code}:motorists:injured\t{motorists_injured}")
        if motorists_killed != '0':
            print(f"{street_off}:{zip_code}:motorists:killed\t{motorists_killed}")
