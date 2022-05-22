import PySimpleGUI as sg
import pyautogui as py
import winsound

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 300  # Set Duration To 1000 ms == 1 second

password_file =  open("C:\pword.txt", "a")
password_list = [password_file]
password_file.close()


#------- GUI definition & setup --------#
def btn(name):  # a PySimpleGUI "User Defined Element" (see docs)
    return sg.Button(name, size=(6, 1), pad=(2, 1))


layout = [[sg.Text('Input The Passwords And Press Add To Add It To The List')],
          [sg.Input(default_text='', size=(50, 1), key='INPUT'), btn('Add')],
          [btn('Run')],

          [sg.Text('')],
          [sg.Text('', key='-MESSAGE_AREA-')]]


window = sg.Window('Foxx Password Manager', layout, element_justification='center', finalize=True, resizable=True)

text = window['-MESSAGE_AREA-']

#------------ The Event Loop ------------#

while True:


    event, values = window.read(timeout=1000)       # run timeout so that current location can be updated
    if event == sg.WIN_CLOSED:
        break

    if event == 'Run':
        p = open("pword.txt", "r")

        py.sleep(1)
        winsound.Beep(500, duration)
        py.sleep(1)
        winsound.Beep(1000, duration)
        py.sleep(1)
        winsound.Beep(1500, duration)
        py.sleep(1)
        winsound.Beep(2000, duration)
        py.sleep(1)
        winsound.Beep(2500, duration)

        for line in p:
            py.write(line)
            py.press('enter')
            py.sleep(3)
        p.close()




    if event == 'Add':
        password_file = open("pword.txt", "a")
        input = values['INPUT'] #turns value of text box asigned as INPUT to the variable input
        password_list.append(password_file)
        password_file.writelines(input + "\n")
        password_file.close()
        text.update(text.get() + input + " ")
        window['INPUT'].update('')  # only add a legit submit


window.close()