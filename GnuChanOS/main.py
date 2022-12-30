import PySimpleGUI as sg
import datetime

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

def main():

    font = "Sans, 15"
    commandList = []

    topPanel = [
        [
            sg.Text(" : ", font=font, background_color="#240046", expand_y=True, expand_x=True, pad=(0,0)),
            sg.Image("", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0), ),

            sg.Text("must emty space", background_color="#5a189a", expand_x=True, pad=(0,0), expand_y=True, size=(47, None)),

            
            sg.Image("", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0), ),
            sg.Text("(-Gnu/Linux'is My Life-)", justification="center", font=font, background_color="#240046", expand_x=True, expand_y=True, pad=(0,0) ),
            sg.Image("", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0), ),


            sg.Text("must emty space", background_color="#5a189a", expand_x=True, expand_y=True, pad=(0,0), size=(41, None)),
            
            sg.Text(size=(21, None), background_color="#5a2987", key="datetime", font=font, justification="center", expand_x=True, expand_y=True, pad=(0,0)),

            sg.Image("", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0)),
            sg.Text(" : ", font=font, background_color="#240046", expand_y=True, expand_x=True, pad=(0,0)),
        ]
    ]


    rightWindow = [
        [sg.Text("Command List", font=font, text_color="#9d4edd", background_color="#361d4f", expand_y=True, size=(85,2), justification="center")],

        [
            sg.Push(),
            sg.Listbox(commandList, font=font, expand_x=True, expand_y=True, size=(20,23), no_scrollbar=True, background_color="#240046", text_color="#9d4edd", key="cmList"),
            sg.Push(),
        ]
    ]


    multilinePanel = [
        [
            sg.Push(),
            sg.Multiline(autoscroll=True, font=font, disabled=True, no_scrollbar=True, background_color="#240046", text_color="#9d4edd", key="termInput", size=(85,26.4), expand_y=True, expand_x=True), 
            sg.Push()
        ],

    ]


    inputPanel = [

        [
            sg.Push(),
            sg.Text(":> ", font="Sans, 20", background_color="#240046", expand_y=True, expand_x=True, pad=(0,0)), 
            sg.Input(font=font, background_color="#240046", text_color="#9d4edd", key="InputTxt", expand_y=True, expand_x=True, pad=(0,0), size=(50,1)),
            sg.Text("   ", font=font, expand_x=True, expand_y=True),
            sg.Button("test", font=font, expand_x=True, expand_y=True),
            sg.Button("test", font=font, expand_x=True, expand_y=True),
            sg.Button("test", font=font, expand_x=True, expand_y=True),
            sg.Button("test", font=font, expand_x=True, expand_y=True),
            sg.Push()
        ],

    ]


    bottomPanel = [
        [
            sg.Text(" : ", font=font, background_color="#240046", expand_x=True, pad=(0,0), size=(None,2)),
            

            sg.Text("must emty space", background_color="#5a189a", expand_x=True, expand_y=True, pad=(0,0)),
            sg.Text("this is example", font=font, justification="center", background_color="#240046", expand_x=True, expand_y=True, pad=(0,0), size=(38, 2)),
            sg.Text("must emty space", background_color="#5a189a", expand_x=True, expand_y=True, pad=(0,0)),


            sg.Text(" : ", font=font, background_color="#240046", expand_x=True, expand_y=True, pad=(0,0), size=(None,2)),

        ]

    ]


    mainPanel = [
        [sg.Push()],
        [sg.Push(), sg.Column(topPanel), sg.Push()],
        [sg.Push(), sg.Column(multilinePanel), sg.Column(rightWindow), sg.Push()],
        [sg.Push(), sg.Column(inputPanel), sg.Push()],
        [sg.Push(), sg.Column(bottomPanel), sg.Push()],
        [sg.Push()],
    ]



    Window = sg.Window("GnuChan Default", mainPanel, finalize=True, size=(1280,900))
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
            Window["termInput"].update(test, append=True)
            Window["InputTxt"].update("")


if __name__ == "__main__":
    main()