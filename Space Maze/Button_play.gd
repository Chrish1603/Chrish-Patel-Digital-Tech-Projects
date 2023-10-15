extends Button

var speed: float = 0.01

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
	
# play button
func _on_Button_play_pressed():
	Global.level_count = 1
	get_tree().change_scene_to_file("res://level1menu.tscn")
