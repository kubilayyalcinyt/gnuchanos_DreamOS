import PySimpleGUI as sg
import datetime, os
from programs import *




sg.LOOK_AND_FEEL_TABLE["gnuchan"] = {
                                        'BACKGROUND': '#160229',
                                        'TEXT': '#9d4edd',
                                        'INPUT': '#9d4edd',
                                        'TEXT_INPUT': '#240046',
                                        'SCROLL': '#3c096c',
                                        'BUTTON': ('#c77dff', '#5a189a'),
                                        'PROGRESS': ('#c77dff', '#5a189a'),
                                        'BORDER': 0, 'SLIDER_DEPTH': 0,'PROGRESS_DEPTH': 0, 
                                        }
sg.theme("gnuchan")



def main():

    font = "Sans, 15"
    commandList = [" Komut Listesi ", "--| run teditor", "--| run timer", "--| run music", "--| run calculator"]

    mainPanel = [
        [sg.Push()],

        [
            sg.HSeparator(),
            sg.Text(" : ", font="Sans, 20", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            sg.Image("image/ram.png", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),

            sg.Text("must emty space", background_color="#5a189a", expand_x=True, expand_y=True, pad=(0,0), size=(35,None)),

            
            sg.Image("image/gnu.png", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            sg.Text("(-Gnu/Linux'is My Life-)", justification="center", font=font, size=(21, 1), background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            sg.Image("image/gnu.png", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),


            sg.Text("must emty space", background_color="#5a189a", expand_x=True, expand_y=True, pad=(0,0), size=(35,None)),
            
            sg.Text(background_color="#5a2987", key="datetime", font=font, justification="center", expand_x=True, expand_y=True, pad=(0,0)),

            sg.Image("image/rem.png", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            sg.Text(" : ", font="Sans, 20", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            sg.HSeparator()
        ],

        [sg.Text(" ")],
        
        [
        sg.Push(),

        sg.Multiline(autoscroll=True, font=font, disabled=True, no_scrollbar=True, background_color="#240046", text_color="#9d4edd", key="termInput", size=(85,24), expand_y=True, expand_x=True), 
        sg.Text(" "),
        sg.Listbox(commandList, key="cmList", font=font, no_scrollbar=True, background_color="#240046", text_color="#9d4edd", expand_x=True, expand_y=True, size=(20,22),),

        sg.Push()
        ],

        [sg.Text(" ")],

        [
            sg.Push(),
            sg.Text(" ->|", font="Sans, 20", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            sg.Input(font=font, background_color="#240046", text_color="#9d4edd", key="InputTxt", focus=True, expand_x=True, expand_y=True, pad=(0,0), size=(50,1)),
            sg.Text("   ", font=font, expand_x=True),


            sg.Button("test", font=font, expand_x=True),
            sg.Button("test", font=font, expand_x=True),
            sg.Button("test", font=font, expand_x=True),
            sg.Button("test", font=font, expand_x=True),
            sg.Push()
        ],

        [sg.Text("")],

        [
            sg.HSeparator(),
            sg.Text(" : ", font="Sans, 20", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            sg.Image("image/first.png", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),

            sg.Text("must emty space", background_color="#5a189a", expand_x=True, expand_y=True, pad=(0,0), size=(35,None)),

            
            sg.Text("UwU Burası Daha Bitmedi UwU", justification="center", font=font, size=(45, 1), background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            

            sg.Text("must emty space", background_color="#5a189a", expand_x=True, expand_y=True, pad=(0,0), size=(35,None)),
            
            sg.Image("image/last.png", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            sg.Text(" : ", font="Sans, 20", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            sg.HSeparator()
        ],

        [sg.Push()],
    ]



    Window = sg.Window("GnuChan Default", mainPanel, finalize=True, return_keyboard_events=True)
    Window['InputTxt'].bind("<Return>", "_Enter")


    while True:  # Event Loop
        event, values = Window.read(timeout=60)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break


        # time and date
        year = datetime.datetime.today().year
        day = datetime.datetime.today().day
        month = datetime.datetime.today().month

        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second

        dateTimeXtreme = str(year) + "/" + str(day) + "/" + str(month) + " | " + str(hour) + ":" + str(minute) + ":" + str(second)
        Window["datetime"].update(dateTimeXtreme)

        # test input
        test = " ArchKubi: " + values["InputTxt"] + "\n"

        if event == "InputTxt" + "_Enter":
            Window["InputTxt"].update("")

            # programlar
            if values["InputTxt"] == "run teditor":
                Window["termInput"].update("--| Text Editör Açıldı!" + "\n", append=True)
                TextEditor()
            elif values["InputTxt"] == "run timer":
                Window["termInput"].update("--| Timer Açıldı!" + "\n", append=True)
                Timer()
            elif values["InputTxt"] == "run music":
                Window["termInput"].update("--| Youtube Müzik İndirici Açıldı" + "\n", append=True)
                MusicDownloander()
            elif values["InputTxt"] == "run calculator":
                Window["termInput"].update("--| Hesap Makinesi Açıldı" + "\n", append=True)
                Calculator()







            else:
                Window["termInput"].update(test, append=True)
                Window["termInput"].update("--| böyle bir komut bulunamadı!" + "\n", append=True)


if __name__ == "__main__":
    main()