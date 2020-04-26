""" alleen de code"""


import pandas as pd
import os
import re
from pathlib import Path

import csv_bouwen.functies as deft
import source.defenitions_fib as samenvoegen
from source.paden_naar_files import pad_tmp, pad_vdps, pad_file_in, list_of_files_to_clean, cleaner

pad = Path("/Users/mike/PycharmProjects/TC_mjth_2019/")  # this  should be wd path and then one up
# padtmp = "/Users/mike/PycharmProjects/TC_mjth_2019/file_out/tmp"
# padvdps = "/Users/mike/PycharmProjects/TC_mjth_2019/file_out/vdps"
# print(os.getcwd())
# print(pad)
paden = [pad_tmp, pad_vdps]

for pad_opruim in paden:
    deft.cleaner(pad_opruim)

name_file_in = "202014342_proef.csv"  # input("csv file: ")
ordernummer = "202014342"  # input("ordernumber: ")
aantal_banen = aantal_per_lijst = int(input("aantal_banen / aantal per lijst: >"))  # if else struktuur
mes = 4
aantal_vdp = 1
mes_controle = mes * aantal_vdp

file_in = pd.read_csv(pad_file_in / name_file_in, delimiter=";")  # try except

totaal = file_in.aantal.sum()
min_waarde = file_in.aantal.min()
afwijking = 0
row = len(file_in)
opb = ongeveer_per_baan = (totaal // aantal_banen)

print(f'aantal rollen= {row}')

print(f'totaal van lijst is {totaal} en het gemiddelde over {aantal_banen} banen is {opb}')
print(f'kleinste rol {min_waarde}')


deft.splitter(file_in, aantal_banen, -250)
split_csv = [x for x in os.listdir(pad_tmp) if x.endswith(".csv")]
print(f'split_csv {split_csv}')

lijst_lengte = len(split_csv)

use = lijst_lengte // aantal_per_lijst
print(use)

# deft.check_map_op_mes(mes_controle, lijst_lengte, min_waarde,file_in, aantal_banen, afwijking)
# hier moet programma gaan rekenen totdat er precies genoeg tmpfiles aangemaakt worden.

regex = r"([.])"
subst = ""
links = []

count = 0
for line in split_csv:
    file_Naam_In = f'{pad_tmp / line}'
    print(file_Naam_In)
    a = "".join(line.strip("\n"))
    result = re.sub(regex, subst, a, 0, re.MULTILINE)
    links.append(f'{result}_')

    # file_Naam_In = f"{naam}_inschiet.csv"
    filenaam_uit = f"{pad_vdps}/vdp{count:>{0}{5}}_bewerkt.csv"
    print(file_Naam_In)
    print(filenaam_uit)
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

csv_files_in_tmp = [x for x in os.listdir(pad_tmp) if x.endswith(".csv")]  # pathlib versie of genereerde posix
sorted_files = sorted(csv_files_in_tmp)
print(f'sortedfiles {sorted_files}')
aantal_rollen = len(sorted_files)
combinaties = aantal_rollen // mes

combinatie_binnen_mes = []

print(combinaties)

begin = 0
eind = mes

for combinatie in range(combinaties):
    combinatie_binnen_mes.append(sorted_files[begin:eind])
    begin += mes
    eind += mes

print(combinatie_binnen_mes)

print(len(combinatie_binnen_mes) * mes)

if mes == 10:
    print("gekozen mes == 10")

# ultimate cleaner

for schoon_pad in list_of_files_to_clean:
    cleaner(schoon_pad)