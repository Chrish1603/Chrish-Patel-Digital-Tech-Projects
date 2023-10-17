extends Area3D

signal coinCollected

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
# coin floating animation
@warning_ignore("unused_parameter")
func _physics_process(delta):
	rotate_y(deg_to_rad(3))

# coin collection animation
func _on_coin_body_entered(body):
	if body.name == "Player":
		$AnimationPlayer.play("coin_bouce")
		$Timer.start()

# when timer completes
func _on_timer_timeout():
	emit_signal("coinCollected")
	queue_free()
