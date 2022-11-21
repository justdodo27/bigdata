#!/usr/bin/env python3
import sys

current_key = None
damage_sum = 0


for line in sys.stdin:
    *key, damage_count = line.split('\t')
    damage_count = int(damage_count)

    key = '\t'.join(key)

    if current_key == key:
        damage_sum += damage_count
    else:
        if current_key:
            print(f"{current_key}\t{damage_sum}")
            
        damage_sum = 0
        current_key = key

        damage_sum += damage_count

if current_key:
    print(f"{current_key}\t{damage_sum}")
