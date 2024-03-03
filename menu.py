import PySimpleGUI as sg

class Menu:
    def openMenu(taskList):
        layout = [
            [sg.Text("Select an option:"), sg.Combo(taskList, key='-OPTION-')],
            [sg.Button("Continue")]
        ]

        window = sg.Window("Select Option", layout)

        option = None

        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break
            elif event == "Continue":
                option = values['-OPTION-']
                break

        window.close()

        print("Selected Option:", option)
        return option
