extends Camera3D

@export
var target: NodePath
@export
var enabled := true

# range of camera
@export_range(0, 3, 0.01)

# speed of camera
var speed := 3.0

# get camera target
func _process(delta):
	var target_node = get_node(target)
	if not enabled or not target_node:
		return
	
	# intorpolated camera
	var move_delta = speed * delta
	var target_transform = target_node.global_transform
	global_transform = global_transform.interpolate_with(target_transform, move_delta)
	
	# follow camera target
	if target_node is Camera3D and target_node.projection == projection:
		var new_near = lerp(near, target_node.near, move_delta)
		var new_far = lerp(far, target_node.far, move_delta)
		
		if target_node.projection == PROJECTION_ORTHOGONAL:
			set_orthogonal(lerp(size, target_node.size, move_delta), new_near, new_far)
		else:
			set_perspective(lerp(fov, target_node.fov, move_delta), new_near, new_far)
			
