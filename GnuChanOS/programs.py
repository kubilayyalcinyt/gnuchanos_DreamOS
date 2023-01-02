import PySimpleGUI as sg
import os
from calculatorWarningLib import WarningWindow
from pygame import mixer




sg.LOOK_AND_FEEL_TABLE["gnuchan"] = {
                                    'BACKGROUND': '#240046',
                                    'TEXT': '#9d4edd',
                                    'INPUT': '#9d4edd',
                                    'TEXT_INPUT': '#240046',
                                    'SCROLL': '#3c096c',
                                    'BUTTON': ('#c77dff', '#5a189a'),
                                    'PROGRESS': ('#c77dff', '#5a189a'),
                                    'BORDER': 0, 'SLIDER_DEPTH': 0,'PROGRESS_DEPTH': 0, 
                                    }
sg.theme("gnuchan")


def TextEditor():

    font = "Sans, 11"
    aktifTab = "tab1"
    multiLine = ""

    fileOpen = False

    # tabs
    textEdit1 = [[sg.Multiline(size=(85, 80), key='multitext1', font=font, expand_x=True, expand_y=True)]]
    textEdit2 = [[sg.Multiline(size=(85, 80), key='multitext2', font=font, expand_x=True, expand_y=True)]]
    textEdit3 = [[sg.Multiline(size=(85, 80), key='multitext3', font=font, expand_x=True, expand_y=True)]]
    textEdit4 = [[sg.Multiline(size=(85, 80), key='multitext4', font=font, expand_x=True, expand_y=True)]]
    textEdit5 = [[sg.Multiline(size=(85, 80), key='multitext5', font=font, expand_x=True, expand_y=True)]]


    # tab grub 
    tab = [[
        sg.TabGroup([
            [sg.Tab('Tab 1', textEdit1)],
            [sg.Tab('Tab 2', textEdit2)],
            [sg.Tab('Tab 3', textEdit3)],
            [sg.Tab('Tab 4', textEdit4)],
            [sg.Tab('Tab 5', textEdit5)] ]) 
        ]]


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

        # doc cheat for python can edit and save
        if event == "Open Doc":
            with open('pythonNotes.txt', 'r') as f:
                data = f.read()
            window["pythonNote"].update(data)

        elif event == "Save Doc":
            data = values["pythonNote"]
            with open('pythonNotes.txt', 'w') as f:
                f.write(data)

        # text folder open,save , save as
        if event == 'Open':
            file_name = sg.popup_get_file('Open', save_as=False)
            if file_name:
                with open(file_name, 'r') as f:
                    text = f.read()
                window[multiLine].update(text)
                fileOpen = True

        elif event == "Save":
            if fileOpen == True:
                if file_name:
                    with open(file_name, 'w') as f:
                        f.write(values[multiLine])
            else:
                file_name = sg.popup_get_file('Save As', save_as=True)
                if file_name:
                    with open(file_name, 'w') as f:
                        f.write(values[multiLine])    
                        fileOpen = True
        
        elif event == 'Save As':
            file_name = sg.popup_get_file('Save As', save_as=True)
            if file_name:
                with open(file_name, 'w') as f:
                    f.write(values[multiLine])
                    fileOpen = True
    window.close()


def MusicDownloander():

    filePath = "/home/gnuchanos/"
    youtubeLink = "https://animegirl.youtube.com"
    filepathOkay = False
    downloadNow = ""

    FolderPathNotice = "Copy Your Folder Path Pleas"

    rightWindow = [
        [sg.Push(), sg.Text("GnuChan Music Download", font="sans, 20", justification="center"), sg.Push()],
        [sg.HSeparator()],
        
        [sg.Push(), sg.Input(filePath, font="sans, 20", key="folderPath"), sg.Button("Save Path", font="sans, 20"), sg.Push()],
        [sg.Push(), sg.Text(FolderPathNotice, font="sans, 20", justification="center", key="folderPathOkay"), sg.Push()],

        [sg.HSeparator()],

        [sg.Text("")], [sg.Text("Folder Path: ", key="finish", font="sans, 20", expand_x=True)], [sg.Text("")],

        [sg.HSeparator()],

        [sg.Push(), sg.Input(youtubeLink, font="sans, 20", key="ytLink"), sg.Button("Download", font="sans, 20"), sg.Push()],
        [sg.Push(), sg.Text("Youtube Link - Single video or playlist", font="sans, 20", justification="center"), sg.Push()],

        [sg.HSeparator()],

        [sg.Text("Tutorial: ctrl+C and Ctrl+V good luck \ndon't Forget This is just UI \npowerad by yt-dlp and PySimpleGUI", font="sans, 20")]
    

    ]

    mainWindow = [
        [sg.Column(rightWindow)],
    ]

    Window = sg.Window("GnuChan Default", mainWindow)

    while True:  # Event Loop
        event, values = Window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break



        if event == "Save Path":
            filePath = values["folderPath"]
            Window["finish"].update(f"Folder Path: {filePath}")
            filepathOkay = True



        if event == "Download":
            music_Link = values["ytLink"]
            if "https://www.youtube" in music_Link:
                downloadNow = False
                os.system(f"cd {filePath} && yt-dlp -f 'ba' -x --audio-format mp3 {music_Link}")
                downloadNow = True



        if downloadNow == True:
            Window["finish"].update(f"Folder Path: {filePath} | Music Download is Finish")
        elif downloadNow == False:
            Window["finish"].update(f"Folder Path: {filePath} | Music Download is start")



        if filepathOkay == True:
            FolderPathNotice = "You Can Download Now"
            Window["folderPathOkay"].update(FolderPathNotice)
        elif filepathOkay == False:
            FolderPathNotice = "Copy Your Folder Path Please"
            Window["folderPathOkay"].update(FolderPathNotice)


def Calculator():

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


def Timer():
    
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
        [
            sg.Button("Start", font="Sans, 20", expand_x=True), sg.Button("Stop", font="Sans, 20", expand_x=True),
            sg.Button("Add Log", font="Sans, 20", expand_x=True), sg.Button("Clear", font="Sans, 20", expand_x=True)
        ],
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


# zamanlayıcı nın başladığı yer
    # zamanlayıcıyı başlatma
        if event == "Start":
            timerStart = True
        elif event == "Stop":
            timerStart = False

    # Timer
        if timerStart == True:
            
            if second <= 60:
                window["timerLabel"].update("Saat: " + str(hour) + " | " + " Dakika: " +  str(minute) + " | " + " Saniye: " +  str(int(second)))
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
            ready = str(line) + "| " + "Saat: " + str(hour) + " | " + " Dakika: " +  str(minute) + " | " + " Saniye: " +  str(int(second)) + "\n"

            timerLog += ready
            window["timerLog"].update(timerLog)


    # temizlik bir yerden gelir
        if event == "Clear":
            second = 0
            minute = 0
            hour = 0

            timerStart = False

            line = 0
            timerLog = ""

            window["timerLabel"].update("Saat: " + str(hour) + " | " + " Dakika: " +  str(minute) + " | " + " Saniye: " +  str(int(second)))
            window["timerLog"].update("temizlendi...")
        

# ekstra zamanlayıcı kendime not buradan sonra başlıyor
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
