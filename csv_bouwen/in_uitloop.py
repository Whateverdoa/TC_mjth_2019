



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

            target.writelines(readline[1:])  # bestand

            target.writelines("0;;stans.pdf;;stans.pdf;;stans.pdf\n" * 100)  # uitloop

            target.writelines(readline[1:10])