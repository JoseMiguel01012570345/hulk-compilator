extends Area2D

var id ="bottom"

func set_( pos , length , width ):
	
	global_position = pos + Vector2( 0 , 200)
	
	$collisionShape.shape.extents.x = width
	$collisionShape.shape.extents.y = length / 2
	pass


func _on_bottom_frontier_area_entered(area):
	if area.id == "bullet":
		area.queue_free()
		
	pass # Replace with function body.
