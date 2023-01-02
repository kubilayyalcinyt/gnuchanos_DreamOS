import PySimpleGUI as sg
defaul = [

    # this example left have size not have expand
    # right have expand_y works but expamd x not work
    [
        sg.Text("left", size=(50,50), background_color="red"), 
        sg.Text("right", expand_y=True, expand_x=True, background_color="black"),
    ],

    # bottom have expand_x work but expand_y not and ı give size 10
    # expand only work size or window size
    [
        sg.Text("bottom", expand_x=True, expand_y=True, size=(None, 10), background_color="white")
    ]

]
window = sg.Window('Window Title', defaul, finalize=True)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
window.close()