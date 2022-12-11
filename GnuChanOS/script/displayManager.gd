extends Control

onready var userNameInput = get_node("dm/VBoxContainer/userName/userNameInput")
onready var userPasswordInput = get_node("dm/VBoxContainer/password/passwordInput")
onready var warning = get_node("warning")
var userEnter = ""

var userName = ""
var userPassword = ""

func _process(delta):
	if userEnter == "okay":
		if userName == "user" and userPassword == "user":
			get_tree().change_scene("res://scene/loadingScreen.tscn")
		else:
			warning.text = "böyle bir kullanıcı yok"


func _on_login_pressed():
	userEnter = "okay"
	userName = userNameInput.text
	userPassword = userPasswordInput.text
	print(userName, " | ", userPassword)
