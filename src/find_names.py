#!/usr/bin/env python3

import csv

def get_name(bytes, index):
    name = ""
    while bytes[index] != 0xfe:
        name = name + chr(bytes[index])
        index += 1
    return name

result = []
with open('games.csv', newline='') as csvfile:
    with open('output/uni-bios_r.rom', 'rb') as bios:
        ba = bytearray(bios.read())
        spamreader = csv.reader(csvfile, delimiter=',')
        for i, row in enumerate(spamreader):
            if len(row) > 2:
                game_name = row[2]
            else:
                game_name = get_name(ba, int(row[1], 16))
            result.append([i, int(row[1], 16) - 4, row[0], game_name])
            #print(", ".join(result[-1]))

result.sort(key=lambda r: r[-1])

with open('output/games.bin', 'wb') as output:
    for i, row in enumerate(result):
        print(str(i) + ', ' + hex(row[1]) +': ' + str(row))
        output.write(row[0].to_bytes(1, 'big'))
    for row in result:
        output.write(row[1].to_bytes(2, 'big'))

    output.write(b'\x0a\x20')
    # ab4a
    output.write('SUPER SIDEKICKS 4 '.encode('utf8')) # 18
    output.write(b'\xfe\x00')

    output.write(b'\x0a\x20')
    # ab60
    output.write('METAL SLUG 2 TURBO'.encode('utf8')) # 18
    output.write(b'\xfe\x00')

    output.write(b'\x0f\x20')
    # ab76
    output.write('XEVIOUS '.encode('utf8')) # 8
    output.write(b'\xfe\x00')

    output.write(b'\x0a\x20')
    # ab82
    output.write('THE EYE OF TYPHOON'.encode('utf8')) # 18
    output.write(b'\xfe\x00')

    output.write(b'\x0d\x20')
    # ab98
    output.write('XENO CRISIS '.encode('utf8')) # 12
    output.write(b'\xfe\x00')

# Padding of titles
#(26-l)/2+6
#2  12
#4  11
#6  10
#8  0f
#10 0e
#12 0d
#14 0c
#16 0b
#18 0a
#20 09
#22 08
#24 07
#26 06
