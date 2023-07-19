extends CharacterBody3D

const SPEED = 10
const ROTSPEED = 8

func _ready():
	pass

@warning_ignore("unused_parameter")
func _physics_process(delta):
	
	if Input.is_action_pressed( "ui_right") and Input.is_action_pressed("ui_left"):
		velocity.x = 0
	elif Input.is_action_pressed("ui_right"):
		velocity.x = SPEED
		$MeshInstance3D.rotate_z(deg_to_rad(-ROTSPEED))
	elif Input. is_action_pressed("ui_left"):
		velocity.x = -SPEED
		$MeshInstance3D.rotate_z(deg_to_rad(ROTSPEED))
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
		
	if Input. is_action_pressed( "ui_up") and Input. is_action_pressed("ui_down"):
		velocity.z = 0
	elif Input.is_action_pressed("ui_up"):
		velocity.z = -SPEED
		$MeshInstance3D.rotate_x(deg_to_rad(-ROTSPEED))
	elif Input. is_action_pressed("ui_down"):
		velocity.z = SPEED
		$MeshInstance3D.rotate_x(deg_to_rad(ROTSPEED))
	else:
		velocity.z = move_toward(velocity.z, 0, SPEED)
	
	move_and_slide()
	
	# Add the gravity.
	#if not is_on_floor():
		#velocity.y -= gravity * delta

	# Handle Jump.
	#if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		#velocity.y = JUMP_VELOCITY

	# Get the input direction and handle the movement/deceleration.
	#var input_dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	#var direction = (transform.basis * Vector3(input_dir.x, 0, input_dir.y)).normalized()
	#if direction:
		#velocity.x = direction.x * SPEED
		#velocity.z = direction.z * SPEED
	#else:
		#velocity.x = move_toward(velocity.x, 0, SPEED)
		#velocity.z = move_toward(velocity.z, 0, SPEED)
	
