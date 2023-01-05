extends WindowDialog

onready var input = get_node("pnl/VBoxContainer/HBoxContainer/input")
onready var termSTR = get_node("pnl/VBoxContainer/termSTR")

var newVar = ""

func _on_input_text_entered(new_text):

	newVar = "--|" + GlobalVar.defaulUser + ": " + input.text + "\n" + "---------------------------------------------" + "\n" + "\n"
	termSTR.text += newVar



	if input.text == "hello":
		termSTR.text += "Hellooooo" + "\n"






	else:
		termSTR.text += "Böyle Bir komut yok!" + "\n"
	input.text = ""
