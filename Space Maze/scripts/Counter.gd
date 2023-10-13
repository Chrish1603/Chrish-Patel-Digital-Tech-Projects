extends Label

var coins = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	text = str(coins)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if Global.level_count == 1 and coins == 10:
		Global.level_count += 1
		get_tree().change_scene_to_file("res://level2menu.tscn")
		
	elif Global.level_count == 2 and coins == 20:
		Global.level_count += 1
		get_tree().change_scene_to_file("res://level3menu.tscn")
		
	elif Global.level_count == 3 and coins == 30:
		get_tree().change_scene_to_file("res://youwon.tscn")
		
	else:
		pass

#coin counter increase
func _on_coin_collected():
	coins = coins + 1
	_ready()
	
