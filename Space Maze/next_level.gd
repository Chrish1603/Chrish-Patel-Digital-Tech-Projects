extends Timer


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
	
# L1 menu to level 1 transition
func _on_L1_timer_timeout():
	get_tree().change_scene_to_file("res://level1.tscn")

# L2 menu to level 2 transition
func _on_L2_timer_timeout():
	get_tree().change_scene_to_file("res://level2.tscn")

# L3 menu to level 3 transition
func _on_L3_timer_timeout():
	get_tree().change_scene_to_file("res://level3.tscn")
	

