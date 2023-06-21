extends Area2D

@export var speed = 600
var screen_size
signal star

# Called when the node enters the scene tree for the first time.
func _ready():
	#$AnimatedSprite2D.play("moving")
	screen_size = get_viewport_rect().size


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var velocity = Vector2.ZERO
	if Input.is_action_pressed ("ui_up"):
		velocity.y -= 1
		rotation_degrees = 315
	if Input.is_action_pressed("ui_down"):
		velocity.y += 1
		rotation_degrees = 135
	if Input.is_action_pressed("ui_left"):
		velocity.x -= 1
		rotation_degrees = 225
	if Input.is_action_pressed ("ui_right"):
		velocity.x += 1
		rotation_degrees = 45

	if velocity. length() > 0:
		velocity = velocity.normalized() * speed
		
	position += velocity * delta
	position.x = clamp(position.x, 0, screen_size.x)
	position.y = clamp(position.y, 0, screen_size.y)

func _on_area_entered(area):
	star.emit(area)
