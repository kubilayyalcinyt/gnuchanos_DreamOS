extends Control

onready var userNameInput = get_node("dm/VBoxContainer/userName/userNameInput")
onready var userPasswordInput = get_node("dm/VBoxContainer/password/passwordInput")

var userName = ""
var userPassword = ""

func _process(delta):
	if userName == "user" and userPassword == "user":
		get_tree().change_scene("res://scene/loadingScreen.tscn")



func _on_login_pressed():
	userName = userNameInput.text
	userPassword = userPasswordInput.text
	print(userName, " | ", userPassword)
