import PySimpleGUI as sg
import os

def main():

    sg.LOOK_AND_FEEL_TABLE["gnuchan"] = {
                                            'BACKGROUND': '#160229',
                                            'TEXT': '#9d4edd',
                                            'INPUT': '#9d4edd',
                                            'TEXT_INPUT': '#240046',
                                            'SCROLL': '#3c096c',
                                            'BUTTON': ('#c77dff', '#5a189a'),
                                            'PROGRESS': ('#c77dff', '#5a189a'),
                                            'BORDER': 1, 'SLIDER_DEPTH': 0,'PROGRESS_DEPTH': 0, 
                                            }
    sg.theme("gnuchan")
    font = "Sans, 11"

    aktifTab = "tab1"
    multiLine = ""



    # tabs
    textEdit1 = [
        [sg.Multiline(size=(85, 80), key='multitext1', font=font, expand_x=True, expand_y=True)],
        ]
    textEdit2 = [
        [sg.Multiline(size=(85, 80), key='multitext2', font=font, expand_x=True, expand_y=True)],
        ]
    textEdit3 = [
        [sg.Multiline(size=(85, 80), key='multitext3', font=font, expand_x=True, expand_y=True)],
        ]
    textEdit4 = [
        [sg.Multiline(size=(85, 80), key='multitext4', font=font, expand_x=True, expand_y=True)],
        ]
    textEdit5 = [
        [sg.Multiline(size=(85, 80), key='multitext5', font=font, expand_x=True, expand_y=True)],
        ]


    # tab grub 
    tab = [
        [sg.TabGroup([
            [sg.Tab('Tab 1', textEdit1)],
            [sg.Tab('Tab 2', textEdit2)],
            [sg.Tab('Tab 3', textEdit3)],
            [sg.Tab('Tab 4', textEdit4)],
            [sg.Tab('Tab 5', textEdit5)],
        ],
        )]
    ]


    rightWindow = [
        [sg.Multiline(size=(100, 10), key="pythonNote", font=font, expand_y=True)],
        [sg.Button("Open Doc", font=font), sg.Button("Save Doc", font=font)]
    ]


    mainWindow = [

            #   top bottom
                [
                    sg.Text("Aktif Tab: ", font="Sans, 20"), sg.Text(aktifTab, font="Sans, 20", key="aktifTabWin"), 
                    
                    sg.Button("tab1", font=font),
                    sg.Button("tab2", font=font),
                    sg.Button("tab3", font=font),
                    sg.Button("tab4", font=font),
                    sg.Button("tab5", font=font),

                    sg.Text("", expand_x=True), sg.Text(" İşlemler ", font="Sans, 20"),

                    sg.Button("Open", font=font),
                    sg.Button("Save", font=font),
                    sg.Button("Save As", font=font),
                    sg.Button("Clear", font=font),
                ],

            #   window bar

                [
                    sg.Column(tab, expand_x=True, expand_y=True), 
                    sg.VSeparator(), 
                    sg.Column(rightWindow, expand_x=True, expand_y=True),
                ],
            ]



    window = sg.Window('Pencere Başlığı', mainWindow, size=(1180,900), resizable=True, finalize=True)






    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        # tıkladığımız button ismi event listede var ise aktifTab ismi ile eşitlendi
        if event in ["tab1","tab2","tab3","tab4","tab5"]:
            aktifTab = event
            window["aktifTabWin"].update(aktifTab)

        # aktif tab ismini sözlük olarak atadık
        aktif_Tab_MultiLine = { 
            "tab1": "multitext1", "tab2": "multitext2", 
            "tab3": "multitext3", "tab4": "multitext4", "tab5": "multitext5",
        }
        # böylece multiline için aktif olan anahtarı alıyor
        # bolca if yapmamız gerekmedi | örnek if aktifTab == "tab1" ---> multiLine = multitext1 
        multiLine = aktif_Tab_MultiLine[aktifTab]

        if event == 'Clear':
            if multiLine in ["multitext1","multitext2","multitext3","multitext4","multitext5"]:
                window[multiLine].update('')






        # doc file
        if event == "Open Doc":
            with open('pythonNotes.txt', 'r') as f:
                data = f.read()
            window["pythonNote"].update(data)

        elif event == "Save Doc":
            data = values["pythonNote"]
            with open('pythonNotes.txt', 'w') as f:
                f.write(data)
            

        # open text files
        if event == 'Open':
            file_name = sg.popup_get_file('Open', save_as=False)
            if file_name:
                with open(file_name, 'r') as f:
                    text = f.read()
                window[multiLine].update(text)

        elif event == "Save":
            if file_name:
                with open(file_name, 'w') as f:
                    f.write(values[multiLine])

        elif event == 'Save As':
            file_name = sg.popup_get_file('Save As', save_as=True)
            if file_name:
                with open(file_name, 'w') as f:
                    f.write(values[multiLine])

    window.close()

if __name__ == "__main__":
    main()