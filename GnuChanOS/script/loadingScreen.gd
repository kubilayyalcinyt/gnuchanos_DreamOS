extends Control

onready var progressbar = get_node("ProgressBar")
var progressNum = 5

func _ready():
	progressbar.value = progressNum

func _process(delta):

	if progressbar.value != 0:
		progressbar.value -= delta
	else:
		get_tree().change_scene("res://scene/WindowManager.tscn")
		print("okay")

	progressbar.value = clamp(progressbar.value, 0, 5)
