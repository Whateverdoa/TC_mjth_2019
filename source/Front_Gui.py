import PySimpleGUI as sg

'''
    Example of GUI
'''


def main():
    sg.change_look_and_feel('DarkBlue12')

    columns =[]

    layout = [
        [sg.Text('VDP invul formulier', size=(30, 1), font = ('Arial', 14, 'bold') , text_color="orange")],
        [sg.InputText('202012345', key='ordernummer_1'), sg.Text('Ordernummer', font = ('Arial', 12))],
        [sg.InputText('4', key='mes'), sg.Text('mes', font = ('Arial', 12))],
        [sg.InputText('1', key='vdp_aantal'), sg.Text("VDP's", font = ('Arial', 12))],

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

        [sg.InputText('', key='overlevering_pct'),sg.Text('overlevering %')],
        [sg.InputText('', key='ee'),sg.Text('extra etiketten')],
        [sg.InputText('', key='wikkel'),sg.Text('Wikkel')],



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
            break

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

        print("test")
        print(values['Browse'])
        file_in_frontgui = values['Browse']



    window.close()


if __name__ == '__main__':
    main()


