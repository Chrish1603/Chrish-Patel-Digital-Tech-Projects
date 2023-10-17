extends CharacterBody3D

# speed of player
const SPEED = 12
const ROTSPEED = 10

func _ready():
	pass

@warning_ignore("unused_parameter")
func _physics_process(delta):
	
	# player moving and rotating right
	if Input.is_action_pressed("ui_right") and Input.is_action_pressed("ui_left"):
		velocity.x = 0
	elif Input.is_action_pressed("ui_right"):
		velocity.x = SPEED
		$MeshInstance3D.rotate_z(deg_to_rad(-ROTSPEED))
		
	# player moving and rotating left
	elif Input. is_action_pressed("ui_left"):
		velocity.x = -SPEED
		$MeshInstance3D.rotate_z(deg_to_rad(ROTSPEED))
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		
	# player moving and rotating forward
	if Input. is_action_pressed( "ui_up") and Input. is_action_pressed("ui_down"):
		velocity.z = 0
	elif Input.is_action_pressed("ui_up"):
		velocity.z = -SPEED
		$MeshInstance3D.rotate_x(deg_to_rad(-ROTSPEED))
		
	# player moving and rotating back
	elif Input. is_action_pressed("ui_down"):
		velocity.z = SPEED
		$MeshInstance3D.rotate_x(deg_to_rad(ROTSPEED))
	else:
		velocity.z = move_toward(velocity.z, 0, SPEED)
	move_and_slide()

# player collidng with enemy
func _on_enemy_1_body_entered(body):
	if body.name == "Player":
		# game over menu
		Global.level_count = 1
		get_tree().change_scene_to_file("res://gameover.tscn")
