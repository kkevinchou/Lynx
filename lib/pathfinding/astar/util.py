from lib.vec2d import Vec2d

def line_segment_equal(line_a, line_b):
    return (line_a[0] == line_b[0] and line_a[1] == line_b[1]) or (line_a[0] == line_b[1] and line_a[1] == line_b[0])

def line_in_polygon(line, polygon):
    for edge in polygon.get_edges():
        if line_segment_equal(edge, line):
            return True
    return False

def polygons_intersect(polygon_a, polygon_b):
    for edge in polygon_a.get_edges():
        if intersect_polygon(edge, polygon_b):
            return True

    return False

def distance_between(node_a, node_b):
    point_a = Vec2d(node_a.x, node_a.y)
    point_b = Vec2d(node_b.x, node_b.y)

    return (point_a - point_b).get_length()

def intersect_polygons(line_segment, polygons):
    for polygon in polygons:
        if intersect_polygon(line_segment, polygon):
            return True
    return False

def intersect_polygon(line_segment, polygon):
    if line_in_polygon(line_segment, polygon):
        return False

    shared_points = 0
    for edge in polygon.get_edges():
        if shares_point(line_segment, edge):
            shared_points += 1

    # Both points in the line is in the polygon yet they're not on the same line segment
    # This is considered an intersection
    if shared_points > 2:
        return True

    for edge in polygon.get_edges():
        if line_intersect(line_segment, edge, True):
            return True

    return False

def within_epsilon(a, b, epsilon):
    delta = abs(a - b)
    return delta <= epsilon

def shares_point(line_a, line_b):
    return (line_a[0] == line_b[0]) or (line_a[1] == line_b[1]) or (line_a[0] == line_b[1]) or (line_a[1] == line_b[0])

def shares_point2(t_value_a, t_value_b):
    if (t_value_a in (0, 1)) and (t_value_b in (0, 1)):
        return True
    else:
        return False

def colinear(line_a, line_b):
    a_vec = (line_a[1] - line_a[0]).normalized()
    b_vec = (line_b[1] - line_b[0]).normalized()

    return within_epsilon(abs(a_vec.dot(b_vec)), 1, 0.01)

def line_intersect(line_a, line_b, ignore_overlapping=False):
    line_a_t_value = _compute_t_value(line_a, line_b)

    # Co Linear lines
    if ignore_overlapping and line_a_t_value is None:
        return False

    if (line_a_t_value < 0) or (line_a_t_value >  1):
        return False

    line_b_t_value = _compute_t_value(line_b, line_a)

    if (line_b_t_value < 0) or (line_b_t_value >  1):
        return False

    # Shares Point
    if shares_point2(line_a_t_value, line_b_t_value):
        return False

    if shares_point(line_a, line_b):
        if shares_point(line_a, line_b) != shares_point2(line_a_t_value, line_b_t_value):
            print line_a_t_value, line_b_t_value
        return False

    return True

def _compute_t_value(intersector, intersectee):
    intersectee_dir = intersectee[1] - intersectee[0]
    normal = Vec2d(intersectee_dir[1], -intersectee_dir[0])

    A = intersector[0]
    B = intersector[1]
    P = intersectee[0]

    denominator = (A - B).dot(normal)

    if denominator == 0:
        return None

    return (A - P).dot(normal) / denominator
