from lib.vec2d import Vec2d

def get_bottom_right_most_point(points):
	lowest_point = points[0]

	for point in points:
		if point.y < lowest_point.y:
			lowest_point = point
		elif point.y == lowest_point.y:
			if point.x > lowest_point.x:
				lowest_point = point

	return lowest_point

def generate_convex_hull(points):
	lowest_point = get_bottom_right_most_point(points)
	print lowest_point

	return []