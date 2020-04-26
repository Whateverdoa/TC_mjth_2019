import pandas as pd
from pathlib import Path

from source.paden_naar_files import file_tmp_2, VDP_Def, pad_tmp


def splitter(file_in,
             aantal_banen,
             afwijkings_waarde,
             totaal,
             aantal_rollen,
             ongeveer_per_baan,
             outgoing_posix_pad):
    """"alle variabelen  als argument  try *arg"""
    # afwijkings_waarde = 0 deze komt nu uit def

    file_in = pd.read_csv(file_in, ";")
    a = 0

    begin_eind_lijst = []
    be_LIJST = []

    for num in range(aantal_rollen):
        b = file_in.aantal.iloc[a:num].sum()
        # print(a, num)

        if num == (len(file_in) - 1):
            c = file_in.aantal.iloc[a:num].sum()
            begin_eind_lijst.append([c, a, num + 1])
            be_LIJST.append([a, num + 1])

            csv_naam = Path(f"{outgoing_posix_pad}/{a:>{0}{5}}.csv")
            print(csv_naam)
            file_in.iloc[a : (num + 1)].to_csv(csv_naam)
            print("splitter klaar")

        elif b >= ongeveer_per_baan + afwijkings_waarde:

            csv_naam = Path(f"{outgoing_posix_pad}/{a:>{0}{5}}.csv")
            print(csv_naam)
            file_in.iloc[a : (num + 1)].to_csv(csv_naam)

            begin_eind_lijst.append([b, a, num])
            be_LIJST.append([a, num + 1])
            be_LIJST.append(f"[{a}:{num}]")
            a = num + 1

        continue

    return print(begin_eind_lijst), print(be_LIJST)

def check_map_op_mes(
    mes_controle, maplengte, min_waarde_rol, file_in, aantal_banen, afwijkings_waarde=0
):
    # for loop of while true loop
    if mes_controle == maplengte:
        print("ok")
        print(afwijkings_waarde, maplengte)

    elif mes_controle < maplengte:
        print("te veel")
        # afwijkings_waarde += min_waarde_rol
        print(afwijkings_waarde, maplengte)
        # mappen opschonen
        # nieuwe waardes toepassen in splitter()

    else :
        print("te weinig")
        print(afwijkings_waarde, maplengte)


def print_trespa_rolls(colorcode, beeld, aantal, filenaam_uit, ee = 10):
    """
    Take line from list and build csv for that line
    """
    oap = overaantalpercentage = 1  # 1.02 = 2% overlevering
    # ee = 4  # = etiketten overlevering handmatig

    with open(filenaam_uit, "a", encoding="utf-8") as fn:
        # open a file to append the strings too
        # print(f".;stans.pdf\n", end='', file=fn)

        print(f"{colorcode}: {aantal} etiketten;leeg.pdf\n", end="", file=fn)

        print(f";{beeld}\n" * int(aantal * oap + ee), end="", file=fn)
        # print(f"{colorcode}, {int(aantal * oap)};leeg.pdf\n", end="", file=fn)

        print(f"{colorcode}: {aantal} etiketten;leeg.pdf\n", end="", file=fn)
        print(f";stans.pdf\n", end="", file=fn)


def wikkel_aan_file_zetten(posixlijst, aantal_per_rol, wikkel, rolnummer):
    """neem de csv file en zet er een sluitetiket en een wikkel aan inclusief rolnummer"""
    rol = pd.read_csv(posixlijst, dtype="str")
    # print(rol.head(1))

    df_rol = pd.DataFrame(rol, columns=["kolom1", "pdf", "omschrijving"])

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol) - 1
    eind = df_rol.iat[eind_positie_rol, 0]

    twee_extra = pd.DataFrame(
        [(".", "stans.pdf", "") for x in range(2)],
        columns=["kolom1", "pdf", "omschrijving"],
    )

    wikkel_df = pd.DataFrame(
        [(".", "stans.pdf", "") for x in range(wikkel)],
        columns=["kolom1", "pdf", "omschrijving"],
    )

    sluitstuk = pd.DataFrame(
        [[".", "stans.pdf", f"{rolnummer} {begin} t/m {eind} {aantal_per_rol} etiketten"]],
        # f"{rolnummer} {begin} t/m {eind}", "stans.pdf"
        columns=["kolom1", "pdf", "omschrijving"],
    )

    naam = f"df_{posixlijst.name:>{0}{4}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

    return naam


def files_maken_met_wikkel_en_sluit(posix_rollen_lijst, aantal_per_rol, wikkel, aantalrollen, begin_nummer_rol=0):
    """de totale wikkel functie met de wikkel functie erin"""
    for i in range(aantalrollen):
        csv_naam = f'wikkel_sluit_{i:>{0}{5}}.csv'
        pad = Path(file_tmp_2 / csv_naam)
        # print(csv_naam)
        rol = f'rol_{begin_nummer_rol + i + 1:>{0}{3}}'
        wikkel_aan_file_zetten(posix_rollen_lijst[i], aantal_per_rol, wikkel, rol).to_csv(pad, index=0)
    return csv_naam


def lijstmaker_uit_posixpad_csv(padnaam):
    rollen_posix_lijst = [rol for rol in padnaam.glob("*.csv") if rol.is_file()]
    return rollen_posix_lijst


def html_sum_form_writer(titel="summary", **kwargs):
    """"build a html file for summary purposes with  *kwargv
    search jinja and flask
    css link toevoegen
    """
    for key, value in kwargs.items():
        print(key, value)

    naam_html_file = f'summary/{titel}_.html'
    with open(naam_html_file, "w") as f_html:

        #         for key, value in kwargs.items():
        #             print(key, value)

        print("<!DOCTYPE html>\n", file=f_html)
        print('<html lang = "en">\n', file=f_html)
        print("     <head>\n", file=f_html)
        print("<meta charset='UTF-8>'\n", file=f_html)
        print(f"<title>{titel.capitalize()}</title>\n", file=f_html)
        print("     </head>", file=f_html)
        print("         <body>", file=f_html)
        for key, value in kwargs.items():
            print(f' <p><b>{key}</b> : {value}<p/>', file=f_html)

        print("         </body>", file=f_html)
        print(" </html>", file=f_html)


def lijst_opbreker(lijst_in, mes, combinaties):
    start = 0
    end = mes
    combinatie_binnen_mes = []

    for combinatie in range(combinaties):
        # print(combinatie)
        combinatie_binnen_mes.append(lijst_in[start:end])
        start += mes
        end += mes
    return combinatie_binnen_mes


def kol_naam_lijst_builder(mes=1):
    kollomnaamlijst = []

    for count in range(1, mes + 1):
        # 5 = len (list) of mes
        num = f"num_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        # kollomnaamlijst.append(num)
        kollomnaamlijst.append(omschrijving)
        kollomnaamlijst.append(pdf)

    # return ["id"] + kollomnaamlijst
    return kollomnaamlijst


def lees_per_lijst(lijst_met_posix_paden):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count = 1
    concatlist = []
    for posix_pad_naar_file in lijst_met_posix_paden:
        print(posix_pad_naar_file)
        naam = f'file{count:>{0}{4}}'
        print(naam)
        naam = pd.read_csv(posix_pad_naar_file)
        concatlist.append(naam)
        count += 1
    kolomnamen = kol_naam_lijst_builder(5)
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    lijst_over_axis_1.columns = [kolomnamen]

    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1


def df_rol_builder(posixlijst_naam, aantal_per_rol, wikkel, begin_nummer_uit_lijst=1, vlg=0, posities=1):
    rol = pd.DataFrame(posixlijst_naam)

    df_rol = pd.DataFrame(rol, columns=["omschrijving", "pdf"])

    begin = df_rol.iat[0, 0]
    eind_positie_rol = (aantal_per_rol) - 1
    eind = df_rol.iat[eind_positie_rol, 0]

    twee_extra = pd.DataFrame(
        [("", "stans.pdf") for x in range(2)],
        columns=["omschrijving", "pdf"],
    )

    wikkel_df = pd.DataFrame(
        [("", "stans.pdf") for x in range(wikkel)],
        columns=["omschrijving", "pdf"],
    )

    sluitstuk = pd.DataFrame(
        [[f"{begin} t/m {eind}", "stans.pdf"]],
        columns=["omschrijving", "pdf"],
    )

    naam = f"df_{begin_nummer_uit_lijst:>{vlg}{posities}}"
    # print(f'{naam} ____when its used to append the dataFrame in a list or dict<-----')
    naam = pd.concat([twee_extra, sluitstuk, wikkel_df, df_rol])

    return naam


def horizontaal_samenvoegen(opgebroken_posix_lijst, map_uit, meswaarde):
    count = 1
    for lijst_met_posix in opgebroken_posix_lijst:
        vdp_hor_stap = f'vdp_hor_stap_{count:>{0}{4}}.csv'
        vdp_hor_stap = map_uit / vdp_hor_stap
        # print(vdp_hor_stap)
        df = lees_per_lijst(lijst_met_posix, meswaarde)
        # print(df.tail(5))

        lees_per_lijst(lijst_met_posix, meswaarde).to_csv(vdp_hor_stap, index=0)

        count += 1
    return print("hor")


def stapel_df_baan(naam, lijstin, ordernummer, map_uit):
    stapel_df = []
    for lijst_naam in lijstin:
        # print(lijst_naam)
        to_append_df = pd.read_csv(
            f"{lijst_naam}", ",", dtype="str", index_col=0)
        stapel_df.append(to_append_df)
    pd.concat(stapel_df, axis=0).to_csv(f"{map_uit}/{naam}_{ordernummer}.csv", ",")
    return pd.DataFrame(stapel_df)


def kolom_naam_gever_num_pdf_omschrijving(mes=1):
    """supplies a specific string  met de oplopende kolom namen num_1, pdf_1, omschrijving_1 etc"""

    def list_to_string(functie):
        kolom_namen = ""
        for kolomnamen in functie:
            kolom_namen += kolomnamen + ","
        return kolom_namen[:-1] + "\n"

    kollomnaamlijst = []

    for count in range(1, mes + 1):
        # 5 = len (list) of mes
        num = f"num_{count}"
        omschrijving = f"omschrijving_{count}"
        pdf = f"pdf_{count}"
        kollomnaamlijst.append(num)
        kollomnaamlijst.append(pdf)
        kollomnaamlijst.append(omschrijving)

    namen = list_to_string(kollomnaamlijst)

    return namen


def wikkel_n_baans_tc(input_vdp_posix_lijst, etiketten_Y, in_loop, mes):
    """last step voor VDP adding in en uitloop"""

    inlooplijst = (".,stans.pdf,," * mes)
    inlooplijst = inlooplijst[:-1] + "\n"  # -1 removes empty column in final file

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