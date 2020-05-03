"""before I try classes in this script I will put all the functions here"""
import pandas as pd
import os
from pathlib import Path
from source.paden import pad_tmp, pad_vdps, pad_file_in


Y_WAARDE = Y_waarde = 12 #import from GUI Front
INLOOP = inloop = (Y_waarde * 10) -Y_waarde

def check_map_op_mes(
    mes_controle, maplengte, min_waarde_rol, file_in, aantal_banen, afwijkings_waarde=0
):
    # for loop of while true loop

    if mes_controle == maplengte:
        print("ok")
        print(afwijkings_waarde)

    elif mes_controle < maplengte:
        print("te weinig")
        afwijkings_waarde += min_waarde_rol
        print(afwijkings_waarde)
        # mappen opschonen
        # nieuwe waardes toepassen in splitter()

    elif mes_controle > maplengte:
        print("te veel")
        afwijkings_waarde -= min_waarde_rol
        print(afwijkings_waarde)
        # mappen opschonen
        # nieuwe waardes toepassen in splitter()


def cleaner(pad):
    split_csv = [x for x in os.listdir(pad) if x.endswith(".csv")]
    for file in split_csv:
        naam = f"{pad}/{file}"
        if os.path.exists(naam):
            os.remove(naam)


def splitter(file_in, aantal_banen, afwijkings_waarde):
    pad = pad_tmp
    totaal = file_in.aantal.sum()
    row = len(file_in)
    opb = ongeveer_per_baan = totaal // aantal_banen
    print(f"aantal rollen= {row}")
    # afwijkings_waarde = 0 deze komt nu uit def
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

            csv_naam = Path(f"{pad}/{a:>{0}{5}}.csv")
            print(csv_naam)
            file_in.iloc[a : (num + 1)].to_csv(csv_naam)
            print("splitter klaar")

        elif b >= opb + afwijkings_waarde:

            csv_naam = Path(f"{pad}/{a:>{0}{5}}.csv")
            print(csv_naam)
            file_in.iloc[a : (num + 1)].to_csv(csv_naam)

            begin_eind_lijst.append([b, a, num])
            be_LIJST.append([a, num + 1])
            be_LIJST.append(f"[{a}:{num}]")
            a = num + 1

        continue

    return begin_eind_lijst, be_LIJST


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
        print(f";stans.pdf\n", end="", file=fn)


def wikkel_1_baan_tc(input_vdp_lijst):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"VDP_map/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"VDP_map/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines("id;omschrijving_1;pdf_1;omschrijving_2;pdf_2\n")
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:5])

            target.writelines("0;;stans.pdf\n" * 106)  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines("0;;stans.pdf\n" * 100)  # uitloop

            target.writelines(readline[1:10])


def read_out_2(lissst, ordernum):
    """builds  and concats 3 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]

        color_1 = f"VDP_{index + 1}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"vdps/{a}", ";")
        file_2 = pd.read_csv(f"vdps/{b}", ";")

        samengevoeg_2 = pd.concat([file_1, file_2], axis=1)

        samengevoeg_2.columns = ["omschrijving_1", "pdf_1", "omschrijving_2", "pdf_2"]

        samengevoeg_2.fillna({"pdf_1": "stans.pdf", "pdf_2": "stans.pdf"}, inplace=True)

        samengevoeg_2.to_csv(f"VDP_map/{ordernum}_{color_1}.csv", ";")


def wikkel_2_baans_tc(input_vdp_lijst):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"VDP_map/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"VDP_map/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines("id;omschrijving_1;pdf_1;omschrijving_2;pdf_2\n")
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:5])

            target.writelines("0;;stans.pdf;;stans.pdf\n" * 106)  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines("0;;stans.pdf;;stans.pdf\n" * 100)  # uitloop

            target.writelines(readline[1:10])


def read_out_3(lissst, ordernum):
    """builds  and concats 3 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]

        color_1 = f"VDP_{index + 1}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"vdps/{a}", ";")
        file_2 = pd.read_csv(f"vdps/{b}", ";")

        file_3 = pd.read_csv(f"vdps/{c}", ";")

        samengevoeg_3 = pd.concat([file_1, file_2, file_3], axis=1)

        samengevoeg_3.columns = [
            "omschrijving_1",
            "pdf_1",
            "omschrijving_2",
            "pdf_2",
            "omschrijving_3",
            "pdf_3",
        ]

        samengevoeg_3.fillna(
            {"pdf_1": "stans.pdf", "pdf_2": "stans.pdf", "pdf_3": "stans.pdf"},
            inplace=True,
        )

        samengevoeg_3.to_csv(f"VDP_map/{ordernum}_{color_1}.csv", ";")


def wikkel_3_baans_tc(input_vdp_lijst):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"VDP_map/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"VDP_map/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;omschrijving_1;pdf_1;omschrijving_2;pdf_2;omschrijving_3;pdf_3\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:5])

            target.writelines("0;;stans.pdf;;stans.pdf;;stans.pdf\n" * 106)  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines("0;;stans.pdf;;stans.pdf;;stans.pdf\n" * 100)  # uitloop

            target.writelines(readline[1:10])


def read_out_4(lissst, ordernum):
    """builds  and concats 4files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]

        color_1 = f"VDP_{index + 1}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"vdps/{a}", ";")
        file_2 = pd.read_csv(f"vdps/{b}", ";")

        file_3 = pd.read_csv(f"vdps/{c}", ";")
        file_4 = pd.read_csv(f"vdps/{d}", ";")

        samengevoeg_4 = pd.concat([file_1, file_2, file_3, file_4], axis=1)

        samengevoeg_4.columns = [
            "omschrijving_1",
            "pdf_1",
            "omschrijving_2",
            "pdf_2",
            "omschrijving_3",
            "pdf_3",
            "omschrijving_4",
            "pdf_4",
        ]

        samengevoeg_4.fillna(
            {
                "pdf_1": "stans.pdf",
                "pdf_2": "stans.pdf",
                "pdf_3": "stans.pdf",
                "pdf_4": "stans.pdf",
            },
            inplace=True,
        )

        samengevoeg_4.to_csv(f"VDP_map/{ordernum}_{color_1}.csv", ";")


def wikkel_4_baans_tc(input_vdp_lijst, data_uit_vdp=5):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"VDP_map/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"VDP_map/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;omschrijving_1;pdf_1;omschrijving_2;pdf_2;omschrijving_3;pdf_3;omschrijving_4;pdf_4\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:data_uit_vdp])

            target.writelines(
                "0;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf\n"
                * (inloop - data_uit_vdp)
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf\n" * (inloop - 10)
            )  # uitloop

            target.writelines(readline[1:10])


def read_out_5(lissst, ordernum):
    """builds  and concats 4files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]

        color_1 = f"VDP_{index + 1}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"vdps/{a}", ";")
        file_2 = pd.read_csv(f"vdps/{b}", ";")

        file_3 = pd.read_csv(f"vdps/{c}", ";")
        file_4 = pd.read_csv(f"vdps/{d}", ";")

        file_5 = pd.read_csv(f"vdps/{e}", ";")

        samengevoeg_5 = pd.concat([file_1, file_2, file_3, file_4, file_5], axis=1)

        samengevoeg_5.columns = [
            "omschrijving_1",
            "pdf_1",
            "omschrijving_2",
            "pdf_2",
            "omschrijving_3",
            "pdf_3",
            "omschrijving_4",
            "pdf_4",
            "omschrijving_5",
            "pdf_5",
        ]

        samengevoeg_5.fillna(
            {
                "pdf_1": "stans.pdf",
                "pdf_2": "stans.pdf",
                "pdf_3": "stans.pdf",
                "pdf_4": "stans.pdf",
                "pdf_5": "stans.pdf",
            },
            inplace=True,
        )

        samengevoeg_5.to_csv(f"VDP_map/{ordernum}_{color_1}.csv", ";")


def wikkel_5_baans_tc(input_vdp_lijst):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"VDP_map/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"VDP_map/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;omschrijving_1;pdf_1;omschrijving_2;pdf_2;omschrijving_3;pdf_3;omschrijving_4;pdf_4;omschrijving_5;pdf_5\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:8])

            target.writelines(
                "0;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf\n" * 18
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf\n" * 18
            )  # uitloop

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

        color_1 = f"VDP_{index + 1}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"vdps/{a}", ";")
        file_2 = pd.read_csv(f"vdps/{b}", ";")

        file_3 = pd.read_csv(f"vdps/{c}", ";")
        file_4 = pd.read_csv(f"vdps/{d}", ";")

        file_5 = pd.read_csv(f"vdps/{e}", ";")
        file_6 = pd.read_csv(f"vdps/{f}", ";")

        samengevoeg_6 = pd.concat(
            [file_1, file_2, file_3, file_4, file_5, file_6], axis=1
        )

        samengevoeg_6.columns = [
            "omschrijving_1",
            "pdf_1",
            "omschrijving_2",
            "pdf_2",
            "omschrijving_3",
            "pdf_3",
            "omschrijving_4",
            "pdf_4",
            "omschrijving_5",
            "pdf_5",
            "omschrijving_6",
            "pdf_6",
        ]

        samengevoeg_6.fillna(
            {
                "pdf_1": "stans.pdf",
                "pdf_2": "stans.pdf",
                "pdf_3": "stans.pdf",
                "pdf_4": "stans.pdf",
                "pdf_5": "stans.pdf",
                "pdf_6": "stans.pdf",
            },
            inplace=True,
        )

        samengevoeg_6.to_csv(f"VDP_map/{ordernum}_{color_1}.csv", ";")


def wikkel_6_baans_tc(input_vdp_lijst):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"VDP_map/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"VDP_map/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;omschrijving_1;pdf_1;omschrijving_2;pdf_2;omschrijving_3;pdf_3\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:5])

            target.writelines("0;;stans.pdf;;stans.pdf;;stans.pdf\n" * 106)  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines("0;;stans.pdf;;stans.pdf;;stans.pdf\n" * 100)  # uitloop

            target.writelines(readline[1:10])


def read_out_7(lissst, ordernum):
    """builds  and concats 7 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]
        f = lissst[index][5]
        g = lissst[index][6]

        color_1 = f"VDP_{index + 1}"
        # color_2 = f"{index}b"

        file_1 = pd.read_csv(f"vdps/{a}", ";")
        file_2 = pd.read_csv(f"vdps/{b}", ";")

        file_3 = pd.read_csv(f"vdps/{c}", ";")
        file_4 = pd.read_csv(f"vdps/{d}", ";")

        file_5 = pd.read_csv(f"vdps/{e}", ";")
        file_6 = pd.read_csv(f"vdps/{f}", ";")

        file_7 = pd.read_csv(f"vdps/{g}", ";")

        samengevoeg_7 = pd.concat(
            [file_1, file_2, file_3, file_4, file_5, file_6, file_7], axis=1
        )

        samengevoeg_7.columns = [
            "omschrijving_1",
            "pdf_1",
            "omschrijving_2",
            "pdf_2",
            "omschrijving_3",
            "pdf_3",
            "omschrijving_4",
            "pdf_4",
            "omschrijving_5",
            "pdf_5",
            "omschrijving_6",
            "pdf_6",
            "omschrijving_7",
            "pdf_7",
        ]

        samengevoeg_7.fillna(
            {
                "pdf_1": "stans.pdf",
                "pdf_2": "stans.pdf",
                "pdf_3": "stans.pdf",
                "pdf_4": "stans.pdf",
                "pdf_5": "stans.pdf",
                "pdf_6": "stans.pdf",
                "pdf_7": "stans.pdf",
            },
            inplace=True,
        )

        samengevoeg_7.to_csv(f"VDP_map/{ordernum}_{color_1}.csv", ";")


def wikkel_7_baans_tc(input_vdp_lijst):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"VDP_map/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"VDP_map/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;omschrijving_1;pdf_1;omschrijving_2;pdf_2;omschrijving_3;pdf_3;omschrijving_4;pdf_4;omschrijving_5;pdf_5;omschrijving_6;pdf_6;omschrijving_7;pdf_7\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:10])

            target.writelines(
                "0;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf\n"
                * 211
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf\n"
                * 210
            )  # uitloop

            target.writelines(readline[1:10])


def read_out_10(lissst, ordernum):
    """builds  and concats 7 files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]
        f = lissst[index][5]
        g = lissst[index][6]
        h = lissst[index][7]
        i = lissst[index][8]
        j = lissst[index][9]

        color_1 = f"VDP_{index + 1}"
        # color_2 = f"{index}b"

        file_1 = pd.read_csv(f"vdps/{a}", ";")
        file_2 = pd.read_csv(f"vdps/{b}", ";")

        file_3 = pd.read_csv(f"vdps/{c}", ";")
        file_4 = pd.read_csv(f"vdps/{d}", ";")

        file_5 = pd.read_csv(f"vdps/{e}", ";")
        file_6 = pd.read_csv(f"vdps/{f}", ";")

        file_7 = pd.read_csv(f"vdps/{g}", ";")
        file_8 = pd.read_csv(f"vdps/{h}", ";")

        file_9 = pd.read_csv(f"vdps/{i}", ";")
        file_10 = pd.read_csv(f"vdps/{j}", ";")

        samengevoeg_10 = pd.concat(
            [
                file_1,
                file_2,
                file_3,
                file_4,
                file_5,
                file_6,
                file_7,
                file_8,
                file_9,
                file_10,
            ],
            axis=1,
        )

        samengevoeg_10.columns = [
            "omschrijving_1",
            "pdf_1",
            "omschrijving_2",
            "pdf_2",
            "omschrijving_3",
            "pdf_3",
            "omschrijving_4",
            "pdf_4",
            "omschrijving_5",
            "pdf_5",
            "omschrijving_6",
            "pdf_6",
            "omschrijving_7",
            "pdf_7",
            "omschrijving_8",
            "pdf_8",
            "omschrijving_9",
            "pdf_9",
            "omschrijving_10",
            "pdf_10",
        ]

        samengevoeg_10.fillna(
            {
                "pdf_1": "stans.pdf",
                "pdf_2": "stans.pdf",
                "pdf_3": "stans.pdf",
                "pdf_4": "stans.pdf",
                "pdf_5": "stans.pdf",
                "pdf_6": "stans.pdf",
                "pdf_7": "stans.pdf",
                "pdf_8": "stans.pdf",
                "pdf_9": "stans.pdf",
                "pdf_10": "stans.pdf",
            },
            inplace=True,
        )

        samengevoeg_10.to_csv(f"VDP_map/{ordernum}_{color_1}.csv", ";")


def wikkel_10_baans_tc(input_vdp_lijst, Y_waarde, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"VDP_map/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"VDP_map/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;omschrijving_1;pdf_1;omschrijving_2;pdf_2;omschrijving_3;pdf_3;omschrijving_4;pdf_4;omschrijving_5;pdf_5;omschrijving_6;pdf_6;omschrijving_7;pdf_7;omschrijving_8;pdf_8;omschrijving_9;pdf_9;omschrijving_10;pdf_10\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:Y_WAARDE])

            target.writelines(
                "0;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf\n"
                * inloop
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf;;stans.pdf\n"
                * inloop
            )  # uitloop

            target.writelines(readline[-Y_WAARDE:]) # check of dit laatste uit file is


def test():
    print("testing")

def kol_naam_lijst_builder(mes_waarde=1):
    kollomnaamlijst = []

    for count in range(1, mes_waarde + 1):
        # 5 = len (list) of mes
        num = f"kolom_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kollomnaamlijst.append(num)
        kollomnaamlijst.append(pdf)
        kollomnaamlijst.append(omschrijving)

    # return ["id"] + kollomnaamlijst
    return kollomnaamlijst


def lees_per_lijst(lijst_met_posix_paden, mes_waarde):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count = 1
    concatlist = []
    for posix_pad_naar_file in lijst_met_posix_paden:
        # print(posix_pad_naar_file)
        naam = f'file{count:>{0}{4}}'
        # print(naam)
        naam = pd.read_csv(posix_pad_naar_file)
        concatlist.append(naam)
        count += 1
    kolomnamen = kol_naam_lijst_builder(mes_waarde)
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    lijst_over_axis_1.columns = [kolomnamen]

    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1


def horizontaal_samenvoegen(opgebroken_posix_lijst, map_uit, meswaarde):
    count = 1
    for lijst_met_posix in opgebroken_posix_lijst:
        vdp_hor_stap = f'vdp_hor_stap_{count:>{0}{4}}.csv'
        vdp_hor_stap = map_uit/ vdp_hor_stap
        # print(vdp_hor_stap)
        df = lees_per_lijst(lijst_met_posix, meswaarde)
        # print(df.tail(5))

        lees_per_lijst(lijst_met_posix, meswaarde).to_csv(vdp_hor_stap, index=0)

        count += 1
    return print("hor")


def stapel_df_baan(naam,lijstin, ordernummer, map_uit):
    stapel_df = []
    for lijst_naam in lijstin:
        # print(lijst_naam)
        to_append_df = pd.read_csv(
            f"{lijst_naam}", ",", dtype="str", index_col=0)
        stapel_df.append(to_append_df)
    pd.concat(stapel_df, axis=0).to_csv(f"{map_uit}/{naam}_{ordernummer}.csv", ",")
    return pd.DataFrame(stapel_df)






def wikkel_n_baans_tc(input_vdp_posix_lijst, etiketten_Y, in_loop, mes):
    """last step voor VDP adding in en uitloop"""

    inlooplijst = (".,stans.pdf,," * mes)
    inlooplijst = inlooplijst[:-1] + "\n" # -1 removes empty column in final file

    for file_naam in input_vdp_posix_lijst:
        with open(f"{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        nieuwe_vdp_naam = VDP_Def / file_naam.name
        with open(nieuwe_vdp_naam, "w", encoding="utf-8") as target:
            target.writelines(kolom_naam_gever_num_pdf_omschrijving(mes))

            target.writelines(readline[1:etiketten_Y + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                (inlooplijst) * in_loop)  # inloop
            print("inloop maken")
            target.writelines(readline[1:])  # bestand

            target.writelines(
                (inlooplijst) * in_loop)  # inloop  # uitloop
            print("uitloop maken")
            target.writelines(readline[-etiketten_Y:])