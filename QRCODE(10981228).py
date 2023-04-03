# SENG 207 - PROGRAMMING FOR ENGINEERS
# NAME : ISSABELLA MENSAH
# ID : 10981228
# PROJECT 2 - PART 2
# BMEN DEPARTMENT



import PySimpleGUI as sg
import qrcode

sg.theme('TealMono')
font = ('Comic Sans MS',11)

layout = [
    [sg.Text('Text or Link: ', font=font)],
    [sg.Input(key='mylink')],
    [sg.Text('Select a color:',font=font), sg.Combo(values=['blue','red','orange','green', ], key='myColor', default_value='black')],
    [sg.Slider(range=(1, 20), orientation='h', default_value=10, key='mySize')],
    [sg.Button('Create',font=font), sg.Button('Save As',font=font)],
    [sg.Image(key='image')]
]

win = sg.Window('Bella Qr Code Generator', layout)

while True:
    event, values = win.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Create':
        input = values['mylink']
        color = values['myColor']
        size = values['mySize']
        if input.strip() == "":
            sg.popup_error("Empty input not accepted!")
            continue

        try:
            qr = qrcode.QRCode(version=1,box_size=size, border=3, error_correction=qrcode.constants.ERROR_CORRECT_L)
            qr.add_data(input)
            qr.make(fit=True)
            img = qr.make_image(fill_color=color, back_color='white')
            img.save('qr-code.png')
        except:
            sg.popup_error('Invalid input, Try Again!')
            continue
        
        win['image'].update('qr-code.png')
    
    if event == 'Save As':
        userFile = sg.popup_get_file('QR Code SAVE', save_as=True, default_extension='.png')
        if userFile:
            img.save(userFile)
    
        

win.close()