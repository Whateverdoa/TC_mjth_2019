"""before I try classes in this script I will put all the def here"""

def splitter(file_in, aantal_banen):
    pad = "/Users/mike/PycharmProjects/TC_mjth_2019/file_out/tmp/"
    totaal = file_in.aantal.sum()
    row = len(file_in)
    opb = ongeveer_per_baan = (totaal // aantal_banen)
    print(f'aantal rollen= {row}')
    afwijking = -50
    a = 0

    begin_eind_lijst = []
    be_LIJST = []

    for num in range(len(file_in)):
        b = file_in.aantal.iloc[a:num].sum()
        # print(a, num)

        if num == (len(file_in) - 1):
            c = file_in.aantal.iloc[a:num].sum()
            begin_eind_lijst.append([c, a, num + 1])
            be_LIJST.append([a, num + 1])

            csv_naam = f'{pad}{a}.csv'
            print(csv_naam)
            file_in.iloc[a:(num + 1)].to_csv(csv_naam)
            print("splitter klaar")



        elif b >= opb + afwijking:

            csv_naam = f'{pad}{a}.csv'
            print(csv_naam)
            file_in.iloc[a:(num + 1)].to_csv(csv_naam)

            begin_eind_lijst.append([b, a, num])
            be_LIJST.append([a, num + 1])
            be_LIJST.append(f'[{a}:{num}]')
            a = num + 1

        continue

def print_trespa_rolls(colorcode, beeld, aantal, filenaam_uit):
    """
    Take line from list and build csv for that line
    """
    oap = overaantalpercentage = 1  # 1.02 = 2% overlevering
    ee = 4  # = etiketten overlevering handmatig

    with open(filenaam_uit, "a", encoding="utf-8") as fn:
        # open a file to append the strings too
        # print(f".;stans.pdf\n", end='', file=fn)

        print(f"{colorcode}: {aantal} etiketten;leeg.pdf\n", end="", file=fn)

        print(f";{beeld}\n" * int(aantal * oap + ee), end="", file=fn)
        # print(f"{colorcode}, {int(aantal * oap)};leeg.pdf\n", end="", file=fn)

        print(f"{colorcode}: {aantal} etiketten;leeg.pdf\n", end="", file=fn)
        print(f";stans.pdf\n",end="", file=fn)


def read_out_3(lissst, ordernum):
    """builds  and concats 3 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]

        color_1 = f'VDP_{index + 1}'
        color_2 = f'{index}b'

        file_1 = pd.read_csv(f"vdps/{a}", ";")
        file_2 = pd.read_csv(f"vdps/{b}", ";")

        file_3 = pd.read_csv(f"vdps/{c}", ";")

        from turtle import pd
        samengevoeg_3 = pd.concat([file_1, file_2, file_3], axis=1)

        samengevoeg_3.columns = ["omschrijving_1", "pdf_1", "omschrijving_2", "pdf_2", "omschrijving_3", "pdf_3"]

        samengevoeg_3.fillna({'pdf_1': "stans.pdf", 'pdf_2': "stans.pdf", 'pdf_3': "stans.pdf"}, inplace=True)

        samengevoeg_3.to_csv(f"VDP_map/{ordernummer}_{color_1}.csv", ";")

def wikkel_3_baans_tc(input_vdp_lijst):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f'{input_vdp_lijst[index]}'

        with open(f'VDP_map/{file_naam}', "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f'VDP_map/def_{file_naam}', "w", encoding="utf-8") as target:
            target.writelines("id;omschrijving_1;pdf_1;omschrijving_2;pdf_2;omschrijving_3;pdf_3\n")
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:5])

            target.writelines("0;;stans.pdf;;stans.pdf;;stans.pdf\n" * 106)  # inloop

            target.writelines(readline[1:-1])  # bestand

            target.writelines("0;;stans.pdf;;stans.pdf;;stans.pdf\n" * 100)  # uitloop

            target.writelines(readline[1:10])


def read_out_6(lissst, ordernum):
    """builds  and concats 3 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]
        f = lissst[index][5]

        color_1 = f'VDP_{index + 1}'
        color_2 = f'{index}b'

        file_1 = pd.read_csv(f"vdps/{a}", ";")
        file_2 = pd.read_csv(f"vdps/{b}", ";")

        file_3 = pd.read_csv(f"vdps/{c}", ";")
        file_4 = pd.read_csv(f"vdps/{d}", ";")

        file_5 = pd.read_csv(f"vdps/{e}", ";")
        file_6 = pd.read_csv(f"vdps/{f}", ";")

        from turtle import pd
        samengevoeg_6 = pd.concat([file_1, file_2, file_3, file_4, file_5, file_6], axis=1)

        samengevoeg_6.columns = ["omschrijving_1", "pdf_1", "omschrijving_2", "pdf_2", "omschrijving_3", "pdf_3", "omschrijving_4", "pdf_4", "omschrijving_5", "pdf_5", "omschrijving_6", "pdf_6"]

        samengevoeg_6.fillna({'pdf_1': "stans.pdf", 'pdf_2': "stans.pdf", 'pdf_3': "stans.pdf", 'pdf_4': "stans.pdf", 'pdf_5': "stans.pdf",'pdf_6': "stans.pdf"}, inplace=True)

        samengevoeg_6.to_csv(f"VDP_map/{ordernummer}_{color_1}.csv", ";")

def wikkel_6_baans_tc(input_vdp_lijst):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f'{input_vdp_lijst[index]}'

        with open(f'VDP_map/{file_naam}', "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f'VDP_map/def_{file_naam}', "w", encoding="utf-8") as target:
            target.writelines("id;omschrijving_1;pdf_1;omschrijving_2;pdf_2;omschrijving_3;pdf_3\n")
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:5])

            target.writelines("0;;stans.pdf;;stans.pdf;;stans.pdf\n" * 106)  # inloop

            target.writelines(readline[1:-1])  # bestand

            target.writelines("0;;stans.pdf;;stans.pdf;;stans.pdf\n" * 100)  # uitloop

            target.writelines(readline[1:10])


def test():
    print("testing")


