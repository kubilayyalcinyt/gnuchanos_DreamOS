import PySimpleGUI as sg
from calculatorWarningLib import WarningWindow


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
    font = "Sans, 20"


    number1 = ""
    number2 = ""
    Info = ""
    mathSybol = ""
    mathSonucLabel = 0


    Math = ["+", "-", "*", "/"]
    number = ["0","1","2","3","4","5","6","7","8","9"]


    activeMath = {
        "+":"toplamaMath",
        "-":"cikarmaMath",
        "*":"carpmaMath",
        "/":"bolmeMath"
    }

    number1Enter = True
    mathEnd = False

    default = [

        [sg.Text(font=font, size=(30,1), key="mathLabel", background_color="black", expand_x=True, justification="center")],
        
        [sg.HSeparator()],
        [sg.Text(font=font, size=(30,1), key="num1Enter", expand_x=True, justification="center")],


        [sg.HSeparator()],
        [sg.Text("Sayılar1 + sayılar2 = Sonuç Sayısı", font="Sans, 20", justification="center", expand_x=True)],
        [sg.Button("1", font=font, expand_x=True), sg.Button("2", font=font, expand_x=True), sg.Button("3", font=font, expand_x=True), sg.Button("4", font=font, expand_x=True)],
        [sg.Button("5", font=font, expand_x=True), sg.Button("6", font=font, expand_x=True), sg.Button("7", font=font, expand_x=True), sg.Button("8", font=font, expand_x=True)],
        [sg.Button("9", font=font, expand_x=True), sg.Button("0", font=font, expand_x=True), sg.Button("=", font=font, expand_x=True)],
        [sg.Button("Devam Et", font=font, expand_x=True)],


        [sg.HSeparator()],
        [sg.Text("Matematik İşlemleri", font="Sans, 20", justification="center", expand_x=True)],
        [sg.Button("+", font=font, expand_x=True), sg.Button("-", font=font, expand_x=True), sg.Button("*", font=font, expand_x=True), sg.Button("/", font=font, expand_x=True)],


        [sg.HSeparator()],
        [sg.Button("Temizle", font=font, expand_x=True)],
        [sg.Button("Yardım", font=font, expand_x=True)]

    ]


    window = sg.Window("GnuChan Hesaplıyor", default, finalize=True, size=(484, 629))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break


        if event in number:
            if number1Enter == True:
                number1 += event
                window["mathLabel"].update(number1)
            else:
                number2 += event
                window["mathLabel"].update(number2)
        

        if event in Math:
            number1Enter = False
            mathSybol = activeMath[event]


        if event == "=" and number1Enter == False:
            
            if mathSybol == "toplamaMath":
                mathSonucLabel = int(number1) + int(number2)
                window["mathLabel"].update(mathSonucLabel)

                number1Enter = True
                mathEnd = True

            if mathSybol == "cikarmaMath":
                mathSonucLabel = int(number1) - int(number2)
                window["mathLabel"].update(mathSonucLabel)

                number1Enter = True
                mathEnd = True

            if mathSybol == "carpmaMath":
                mathSonucLabel = int(number1) * int(number2)
                window["mathLabel"].update(mathSonucLabel)

                number1Enter = True
                mathEnd = True

            if mathSybol == "bolmeMath":
                mathSonucLabel = int(number1) / int(number2)
                window["mathLabel"].update(mathSonucLabel)

                number1Enter = True
                mathEnd = True


        if event == "Temizle":
            number1 = ""
            number2 = ""

            mathSonucLabel = 0
            
            number1Enter = True
            mathEnd = False
            
            window["mathLabel"].update("")


        if event == "Devam Et":
            number1 = str(mathSonucLabel)
            number2 = ""
            mathSonucLabel = 0
            
            number1Enter = True
            mathEnd = False
            window["mathLabel"].update(number1)

        if event == "Yardım":
            WarningWindow()

        if number1Enter == True and mathEnd == False:
            window["num1Enter"].update("ilk sayı giriliyor...")
        elif number1Enter == False and mathEnd == False:
            window["num1Enter"].update("ikinci sayı giriliyor...")
        elif number1Enter == True and mathEnd == True:
            window["num1Enter"].update("işlem bitti")

    window.close()



if __name__ == "__main__":
    main()