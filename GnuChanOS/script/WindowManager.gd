extends Control

onready var bottomLabel = get_node("system/VBoxContainer/bottom/top3/bottomLabel")
onready var dateLabel = get_node("system/VBoxContainer/top/top6/date")

var clock = OS.get_time()
var dateOS = OS.get_datetime()

var date = ""
var time = ""

func _process(delta):

	date = str(dateOS["year"]) + "/" + str(dateOS["month"]) + "/" + str(dateOS["day"])
	time = str(clock.hour) + ":" + str(clock.minute) + ":" + str(clock.second)

	dateLabel.text = time + " - " + date
	bottomLabel.text = "this is just test"
