""" alleen de code"""

import defenities as deft
import pandas as pd
import os
import re
import pathlib

name_file_in = input("Paste name file: ")
ordernummer = input("ordernumber: ")
aantal_banen =int(input("aantal_banen: >")) # if else struktuur
mes = 3

pad = "/Users/mike/PycharmProjects/TC_mjth_2019/" # this  should be wd path and then one up
# print(os.getcwd())
# print(pad)

file_in = pd.read_csv(f'{pad}file_in/{name_file_in}', delimiter=";") # try except

totaal = file_in.aantal.sum()
row = len(file_in)
opb = ongeveer_per_baan = (totaal // aantal_banen)
print(f'aantal rollen= {row}')
afwijking = -50

print(f'totaal van lijst is {totaal} en het gemiddelde over {aantal_banen} banen is {opb}')


deft.splitter(file_in, aantal_banen)

split_csv = [x for x in os.listdir(f'{pad}file_out/tmp') if x.endswith(".csv")]
print(f'split_csv {split_csv}')
lijst_lengte = len(split_csv)
aantal_per_lijst = 3
use = lijst_lengte // aantal_per_lijst
print(use)

regex = r"([.])"
subst = ""
links = []

count = 0
for line in split_csv:
    file_Naam_In = f"{pad}file_out/tmp/{line}"

    a = "".join(line.strip("\n"))
    result = re.sub(regex, subst, a, 0, re.MULTILINE)
    links.append(f'{result}_')

    # file_Naam_In = f"{naam}_inschiet.csv"
    filenaam_uit = f"{pad}file_out/vdps/vdp{count}_bewerkt.csv"
    # print(file_Naam_In)
    # print(filenaam_uit)
    count += 1

    trespa_lijst = pd.read_csv(file_Naam_In, ",", encoding="utf-8")
    # print(trespa_lijst[0:1])

    oap = overaantalpercentage = 1  # 1.02 = 2% overlevering
    ee = 4  # = etiketten overlevering handmatig

    df = trespa_lijst[["Colorcode", "beeld", "aantal"]]
    df.to_csv("lijst_in.csv", index=0)

    new_input_list = []

    with open("lijst_in.csv") as input:
        num = 0
        for line in input:
            line_split = line.split(",")

            new_input_list.append(line_split)
            num += 1

    list_length = len(new_input_list)

    beg = 1
    eind = 2

    with open(filenaam_uit, "w", encoding="utf-8") as fn:

        print("beeld1;pdf1", file=fn)

    with open(filenaam_uit, "a", encoding="utf-8") as fn:
        for _ in range(list_length - 1):
            a = str(new_input_list[beg:eind][0][0])
            b = str(new_input_list[beg:eind][0][1])
            c = int(new_input_list[beg:eind][0][2])
            deft.print_trespa_rolls(a, b, c, filenaam_uit)

            beg += 1
            eind += 1

os.remove("lijst_in.csv")

