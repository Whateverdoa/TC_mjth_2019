import pandas as pd
from pathlib import Path
import PySimpleGUI as sg

from source.paden_naar_files import cleaner, list_of_files_to_clean, pad_tmp
import source.definitions_fib as csv_builder

'''
    Example of GUI
'''


while True:
    sg.change_look_and_feel('DarkBlue12')

    columns = []

    layout = [
        [sg.Text('VDP invul formulier', size=(30, 1), font=('Arial', 14, 'bold'), text_color="orange")],
        [sg.InputText('202012345', key='ordernummer_1'), sg.Text('Ordernummer', font=('Arial', 12))],
        [sg.InputText('4', key='mes'), sg.Text('mes', font=('Arial', 12))],
        [sg.InputText('1', key='vdp_aantal'), sg.Text("VDP's", font=('Arial', 12))],
        [sg.InputText('1', key='afwijkings_waarde'), sg.Text("afwijking_waarde", font=('Arial', 12))],

        [sg.Text()],

        [sg.InputText('', key='Y_waarde'), sg.Text('Y-waarde')],
        [sg.Text('CSV_file')],
        [sg.Input(), sg.FileBrowse()],

        [sg.Text()],
        # [sg.InputText('', key='totaal'),sg.Text('Totaal')],

        # [sg.InputText('', key='pre'), sg.Text('Pre')],
        # [sg.InputText('', key='begin_1'),sg.Text('Begin nummer')],
        # [sg.InputText('', key='post'), sg.Text('Post')],

        # [sg.InputText('', key='aantal'),sg.Text('Aantal')],
        # [sg.InputText('', key='aantal_per_rol'),sg.Text('Aantal per rol')],

        [sg.InputText('', key='overlevering_pct'), sg.Text('overlevering %')],
        [sg.InputText('', key='ee'), sg.Text('extra etiketten')],
        [sg.InputText('', key='wikkel'), sg.Text('Wikkel')],

        [sg.Button("Ok"), sg.Cancel()],
        # run button

        # this saves the input information
        [sg.Text('_' * 40)],
        [sg.Text('SAVE of LOAD inputform', size=(35, 1))],
        # [sg.Text('Your Folder', size=(15, 1), justification='right'),
        #  sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Exit'),
         sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]

    ]

    window = sg.Window('VDP formulier 2020', layout, default_element_size=(40, 1), grab_anywhere=False)

    while True:
        event, values = window.read()

        if event in ('Exit', None):
            exit(0)

        elif event == 'SaveSettings':
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=False)
            # False in mac OS otherwise it will crash
            window.SaveToDisk(filename)

            # save(values)
        elif event == 'LoadSettings':
            filename = sg.popup_get_file('Load Settings', no_window=False)
            # False in mac OS otherwise it will crash
            window.LoadFromDisk(filename)
            # load(form)

        elif event == "Cancel":
            # todo screen message vraag of er echt gecancelled moet worden:)
            # todo clear  screen  als in een reset
            exit(0)

        elif event == "Ok":

            ordernummer = values['ordernummer_1']
            mes = int(values['mes'])
            aantal_vdps = int(values['vdp_aantal'])
            etikettenY = int(values['Y_waarde'])
            name_file_in = values['Browse']
            afwijkings_waarde = int(values['afwijkings_waarde'])

            overlevering_pct = float(values['overlevering_pct'])
            extra_etiketten = int(values['ee'])
            wikkel = int(values['wikkel'])

            print(ordernummer,
                  mes,
                  aantal_vdps,
                  etikettenY,
                  name_file_in,
                  overlevering_pct,
                  extra_etiketten,
                  wikkel)

            aantal_banen = int(mes * aantal_vdps)

            file_in = pd.read_csv(name_file_in, delimiter=";", dtype="str")  # try except

            totaal = file_in.aantal.astype(int).sum()
            min_waarde = file_in.aantal.astype(int).min()

            row = aantal_rollen = len(file_in)
            opb = ongeveer_per_baan = (totaal // aantal_banen)
            combinaties = aantal_rollen // mes

            print(f'mes = {mes}')
            print(f'aantal rollen= {row}')
            print(f'totaal van lijst is {totaal} en het gemiddelde over {aantal_banen} banen is {opb}')
            print(f'kleinste rol {min_waarde}, de afwijking van het gemiddelde is {afwijkings_waarde}')

            # begin stappenplan stap 0  afwijking berekenaar splitter

            # stap 2 splitter
            print("--.--" * 20)
            print(" door splitter gemaakte csv files")

            csv_builder.splitter(name_file_in,
                                 aantal_banen,
                                 afwijkings_waarde,
                                 totaal,
                                 aantal_rollen,
                                 ongeveer_per_baan,
                                 pad_tmp)

            print("--.--" * 20)

            # stap 3 kijk of aantal in lijsten overeenkomt met gevraagde aantal banen

            map_tmp = sorted(Path(pad_tmp).glob('*.csv'))
            maplengte = len(map_tmp)

            csv_builder.check_map_op_mes(mes, maplengte, name_file_in, aantal_banen, afwijkings_waarde)

            print(csv_builder.lijstmaker_uit_posixpad_csv(pad_tmp))
            print(map_tmp)

            print(csv_builder.lijst_opbreker(map_tmp, mes, 1))

            # laatste regel lost alles op in zoutzuur:)
            for schoon_pad in list_of_files_to_clean:
                cleaner(schoon_pad)

    window.close()



