import PySimpleGUI as sg
from pygame import mixer
from ursina import *


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

    mixer.init()

    second = 0
    minute = 0
    hour = 0

    line = 0

    limiMinute = 0
    limitSecond = 60

    
    timerStart = False
    limitedTimerStart = False

    defaulMusic = "music/music1.mp3"
    timerLog = ""
    ready = ""



    timerLogLy = [
        [sg.Text("Timer Log", font="Sans, 20", expand_x=True, expand_y=True, justification="center")],
        [sg.Multiline(font="Sans, 20", key="timerLog", size=(30,10), expand_x=True, expand_y=True, no_scrollbar=True, autoscroll=True, disabled=True)]
    ]

    timer = [
        [sg.Text(font="Sans, 20", key="timerLabel", expand_x=True, justification="center", background_color="black")],
        [sg.Button("Start", font="Sans, 20", expand_x=True), sg.Button("Stop", font="Sans, 20", expand_x=True)],
        [sg.Button("Add Log", font="Sans, 20", expand_x=True), sg.Button("Clear", font="Sans, 20", expand_x=True)]
    ]

    LimitedTimer = [
        [sg.Text("Zamanlayıcı Ayarla", font="Sans, 20", expand_x=True)],
        [sg.Button("Zaman Sınırı Başlat", font="Sans, 20", expand_x=True), sg.Button("Durdur", font="Sans, 20", expand_x=True)],
        [sg.Text(key="uyarı", font="Sans, 20", expand_x=True)],
        [sg.Input(key="dakika", expand_x=True, font="Sans, 20"), sg.Text("Dakika", font="Sans, 20", expand_x=True)],
    ]

    default = [
        [sg.Column(timer, expand_x=True)],
        [sg.Column(timerLogLy, expand_x=True)],
        [sg.Column(LimitedTimer, expand_x=True)]

    ]


    window = sg.Window("GnuChan Timer", default, finalize=True)

    while True:
        event, values = window.read(timeout=60)
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break

    # zamanlayıcıyı başlatma
        if event == "Start":
            timerStart = True
        elif event == "Stop":
            timerStart = False



    # Timer
        if timerStart == True:
            
            if second <= 60:
                window["timerLabel"].update("Saat:" + str(hour) + ":" + " Dakika:" +  str(minute) + ":" + " Saniye:" +  str(int(second)))
                second += 0.05
            else:
                minute += 1
                second = 0
            
            if minute >= 60:
                hour = 1
        else:
            pass



    # add log ile kaydetme
        if event == "Add Log" and timerStart == True:
            
            line += 1
            ready = str(line) + "| " +"Saat:" + str(hour) + " Dakika:" +  str(minute) + " : " + " Saniye:" +  str(int(second)) + "\n"

            timerLog += ready
            window["timerLog"].update(timerLog)


    # temizlik bir yerden gelir
        if event == "Clear":
            second = 0
            minute = 0
            hour = 0
            timerStart = False
            window["timerLabel"].update(str(hour) + ":" + str(minute) + ":" + str(int(second)))
            window["timerLog"].update("")
        





    # sınırlı zamanlayıcı
        if event == "Zaman Sınırı Başlat":
            limitedTimerStart = True
            second = 60
            window["dakika"].update("")

            if not values["dakika"]:
                window["uyarı"].update("dakika boş bırakılamaz")
            else:
                limiMinute = int(values["dakika"])

    # zamanlayıcıyı durdurma
        if event == "Durdur":
            limitedTimerStart = False
            mixer.music.stop()

    # zamanlayıcı başlıyor yada sıfırlanıyor
        if limitedTimerStart == True:
            if limiMinute < 0:
                limiMinute = 0
                window["uyarı"].update("en az 1 dakika ver")

            # eğer zamanlayıcı boş değilse
            window["uyarı"].update("başladı: Kalan Süre -> " + str(limiMinute) + " : " + str(int(limitSecond)))  

            if limitSecond >= 0:
                limitSecond -= 0.05
            else:
                if limiMinute == 0:
                    window["uyarı"].update("bitti")
                    limitedTimerStart = False
                    
                    mixer.music.load(defaulMusic)
                    mixer.music.play()
                else:
                    limitSecond = 60
                    limiMinute -= 1
        else:
            limiMinute = 0
            limitSecond = 0
            window["uyarı"].update("Zamanlayıcı Durdu")
            


if __name__ == "__main__":
    main()