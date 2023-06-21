extends CharacterBody2D

var target_position = Vector2()  # The target position the ghost is moving towards
var movement_speed = 600  # Adjust this value to control the ghost's movement speed

# Called when the node enters the scene tree for the first time.
func ready (delta):
	# Calculate the direction vector towards the target position
	var direction = (target_position - position).normalized()

	# Move the ghost towards the target position
	var velocity = direction * movement_speed * delta
	move_and_slide(velocity)

	
func chase(target_position):
	self.target_position = target_position

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _on_satellite_body_entered(body):
	if body.name == "rocket":
		# Handle collision with Pac-Man (e.g., reduce score, trigger game over, etc.)
		# Example: get_tree().reload_current_scene() to restart the game
