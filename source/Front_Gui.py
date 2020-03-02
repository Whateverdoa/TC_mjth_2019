import PySimpleGUI as sg

# Very basic window.  Return values as a list
sg.change_look_and_feel('Dark')

layout = [
            # [sg.Text("VDP"), sg.Checkbox('nummers', default=True), sg.Checkbox('beelden')],



            [sg.Text('csv builder for VDP 2.0', text_color="Yellow")],
            [sg.Text('Ordernummer', size=(15, 1)), sg.InputText(key="order_number")],
            [sg.Text()],
            [sg.CalendarButton("Datum")],
            [sg.Text()],
            #
            # [sg.Text('Totaal aantal', size=(15, 1)), sg.Input(key="totaal_aantal")],
            # [sg.Text('Beginnummer', size=(15, 1)), sg.InputText(key="begin_nummer")],
            # [sg.Text('posities', size=(15, 1)), sg.InputText(key="posities")],
            # [sg.Text('Aantal_per_rol', size=(15, 1)), sg.InputText(key='aantal_per_rol')],
            #
            # [sg.Text('Y_waarde', size=(15, 1)), sg.InputText(key="Y_waarde")],
            # [sg.Text('Wikkel', size=(15, 1)), sg.InputText(key="wikkel")],
            # [sg.Text('n * nummer', size=(15, 1)), sg.InputText(key="veelvoud")],

            [sg.Text('Choose A Folder', size=(35, 1))],
            [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Default Folder'), sg.FolderBrowse()],
            [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()],

            [sg.Button("Ok"), sg.Cancel()]
            ]

window = sg.Window('csv builder for VDP test form').Layout(layout)
button, values = window.Read()

print(button, values["order_number"])

print(type(int(values["order_number"])))
# aantallen = int(values[0])
# print(aantallen)
