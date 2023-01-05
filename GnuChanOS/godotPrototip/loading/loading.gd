extends Control


onready var progressBar = get_node("ProgressBar")




func _process(delta):
	progressBar.value += delta * 1
	
	if progressBar.value >= 5:
		get_tree().change_scene("res://WindowManager/windowManager.tscn")
