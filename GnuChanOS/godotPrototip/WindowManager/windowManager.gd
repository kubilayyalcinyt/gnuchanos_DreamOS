extends Control

onready var term = get_node("programs/terminalWindow")

func _ready():
	pass

func _process(delta):
	if Input.is_action_just_pressed("terminal"):
		term.popup_centered()
