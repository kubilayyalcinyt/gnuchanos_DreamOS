extends Control


onready var userInput = get_node("display/fck/VBoxContainer/HBoxContainer/username")
onready var passwordInput = get_node("display/fck/VBoxContainer/HBoxContainer2/userPassword")

func _process(_delta):
	if not userInput:
		pass
	else:
		if GlobalVar.defaulUser == "archkubi" and GlobalVar.defaultPassword == "Kubi":
			get_tree().change_scene("res://loading/loading.tscn")

func _on_login_pressed():

	GlobalVar.defaulUser = userInput.text
	GlobalVar.defaultPassword = passwordInput.text


func _on_login2_pressed():
	get_tree().change_scene("res://WindowManager/windowManager.tscn")
