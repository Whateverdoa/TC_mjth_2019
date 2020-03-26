import pandas as pd
import csv_bouwen.functies as deft
import os
from pathlib import Path
from source.paden import pad_tmp, pad_vdps, pad_file_in

# pad = Path("/Users/mike/PycharmProjects/TC_mjth_2019/")  # this  should be wd path and then one up
# padtmp = Path("/Users/mike/PycharmProjects/TC_mjth_2019/file_out/tmp")
# padvdps = Path("/Users/mike/PycharmProjects/TC_mjth_2019/file_out/vdps")
# print(os.getcwd())
# print(pad)
paden = [pad_tmp, pad_vdps]
print(paden)

for pad_opruim in paden:
    deft.cleaner(pad_opruim)

name_file_in = "202009810 15 18 20_inschiet.csv"  # input("csv file: ")
ordernummer = "202009810"  # input("ordernumber: ")
mes = int(input("mes: >"))  # if else struktuur
aantal_vdp = int(input("aantal_vdp's: >"))  # if else struktuur
aantal_banen = mes * aantal_vdp
file_in = pd.read_csv(f'{pad_file_in}/{name_file_in}', delimiter=";")  # try except
print(file_in.head(2))
som = file_in.aantal.sum()
print(f'aantal etiketten = {som}')
aantal_rollen = len(file_in)
print(f'aantal rollen = {aantal_rollen}')
min_waarde = file_in.aantal.min()
print(f'min_waarde ={min_waarde}')
gemiddelde_baan = som // aantal_banen
print(gemiddelde_baan)
# print(int(round(gemiddelde_baan,-1)))
# gemiddelde_baan = int(round(gemiddelde_baan,-1))

# opb = gemiddelde_baan
afwijking = -1500


def afwijking_berekenen(opb, afwijking):
    a = 0
    begin_eind_lijst_som = []
    begin_eind_lijst = []
    be_LIJST = []

    for num in range(len(file_in)):
        b = file_in.aantal.iloc[a:(num + 1)].sum()
        # print(a, num)
        #     print(b)

        if num == (len(file_in) - 1):
            c = file_in.aantal.iloc[a:num].sum()
            begin_eind_lijst.append([c, a, num + 1])
            begin_eind_lijst_som.append(b)
            be_LIJST.append([a, num + 1])

            #         csv_naam = f'tmp/tmp{a:>{0}{4}}.csv'
            #         print(csv_naam)
            #         file_in.iloc[a:(num + 1)].to_csv(csv_naam)
            print("........")



        elif b >= opb + afwijking:

            #         csv_naam = f'tmp/tmp{a:>{0}{4}}.csv'
            #         print(csv_naam)
            #         file_in.iloc[a:(num + 1)].to_csv(csv_naam)

            begin_eind_lijst.append([b, a, num])
            begin_eind_lijst_som.append(b)
            be_LIJST.append([a, num + 1])
            be_LIJST.append(f'[{a}:{num}]')
            a = num + 1

        continue

    be_LIJST = []
    print(begin_eind_lijst_som)

    sum(begin_eind_lijst_som)

    aantal_aangemaakte_files = len(begin_eind_lijst_som)

    count = 0
    for aantal in begin_eind_lijst_som:
        count += aantal
    print(count)

    if aantal_aangemaakte_files == aantal_banen:
        print(f'OK {aantal_aangemaakte_files} == {mes}*{aantal_vdp}')
        return begin_eind_lijst_som
    else:
        print(f'{aantal_aangemaakte_files} != {mes}*{aantal_vdp}')
        return [0]


afwijking_berekenen(gemiddelde_baan, afwijking)

test = []
for stap in range(afwijking, -1400, 25):
    print(stap)

    test.append(afwijking_berekenen(gemiddelde_baan, stap))

s = pd.Series(test)
print(s)
# count=0
# de=[]
# for i in s:
#     count+=1
#     if i != [0]:
#
#         print(i)
#         print(count)
#         de.append(i)
#
#
# print(set(de))
