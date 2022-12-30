import PySimpleGUI as sg

def WarningWindow():
    multiLineText = """ Temel Yardım
    klasik sayı 1 giriliyor ["+","-","*","/"] listedeki matematik işlemi seçiliyor = basınca bitiyor
    ------------------------------------------------------------------------------------------------
    devam et işlemi sayı1 harici her şey sıfırlanıyor sayı kaldığı yerden devam ediyor
    
    """
    defaul = [
        [sg.Multiline(multiLineText, font="Sans, 20", disabled=True, size=(60,8), no_scrollbar=True)]
    ]
    window = sg.Window('Window Title', defaul)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': 
            break
    window.close()